import logging
import discord # type: ignore
from services.game_service import GameService
from embeds import game_embed, win_embed
from ui import TicTacToeView
from utils.render import get_player_names

logger = logging.getLogger(__name__)

async def on_interaction(interaction: discord.Interaction) -> None:
    if interaction.type != discord.InteractionType.component:
        return
    custom_id = interaction.data.get("custom_id", "")
    if not custom_id.startswith("ttt_"):
        return
    logger.info(f"🔘 Нажата кнопка {custom_id} от {interaction.user.id}")

    try:
        _, channel_id, cell_id = custom_id.split("_")
        cell_id = int(cell_id)
        channel_id = str(interaction.channel_id)

        game = await GameService.get_game(channel_id)
        if not game:
            await interaction.response.send_message(
                "❌ Игра не найдена. Возможно, она уже завершена.",
                ephemeral=True
            )
            return

        if interaction.user.id != game.turn:
            await interaction.response.send_message(
                f"❌ Сейчас ход <@{game.turn}>, а не твой!",
                ephemeral=True
            )
            return

        await interaction.response.defer()

        result = await GameService.make_move(channel_id, cell_id, interaction.user.id)

        if result.get("error"):
            error_messages = {
                "game_not_found": "❌ Игра не найдена. Попробуй начать новую через `/gamestart`.",
                "not_your_turn": f"❌ Сейчас не твой ход!",
                "cell_taken": "❌ Эта клетка уже занята!",
                "game_finished": "❌ Эта игра уже завершена.",
            }
            await interaction.followup.send(
                error_messages.get(result["error"], f"❌ {result['error']}"),
                ephemeral=True
            )
            return

        board = result["board"]

        if result["status"] == "finished":
            winner = result["winner"]
            players = result["players"]
            embed = win_embed(winner, players[0], players[1])
            await interaction.edit_original_response(embed=embed, view=None)
            return

        turn = result["turn"]
        players = result["players"]

        player1_name, player2_name = await get_player_names(interaction.client, players)

        embed = game_embed(board, turn, player1_name, player2_name)
        view = TicTacToeView(board, channel_id, turn)
        await interaction.edit_original_response(embed=embed, view=view)

    except discord.Forbidden:
        logger.error(f"❌ Нет прав у бота в канале {interaction.channel_id}")
        await interaction.followup.send(
            "❌ У бота нет прав для выполнения этого действия.",
            ephemeral=True
        )
    except discord.NotFound:
        logger.error(f"❌ Ресурс не найден: {interaction.data.get('custom_id')}")
        await interaction.followup.send(
            "❌ Сообщение или компонент не найдены. Попробуй начать игру заново.",
            ephemeral=True
        )
    except Exception as e:
        logger.error(f"❌ Ошибка в обработчике: {e}", exc_info=True)
        await interaction.followup.send(
            "❌ Произошла техническая ошибка. Наша команда уже работает над этим!",
            ephemeral=True
        )
