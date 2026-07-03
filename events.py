import logging
import discord # type: ignore
from services.game_service import GameService # type: ignore
from embeds import game_embed, win_embed
from ui import TicTacToeView
from utils.render import get_player_names # pyright: ignore[reportMissingImports]

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
            await interaction.response.send_message("❌ Игра не найдена", ephemeral=True)
            return
        
        if interaction.user.id != game.turn:
            await interaction.response.send_message("❌ Сейчас не твой ход!", ephemeral=True)
            return
        
        await interaction.response.defer()
        
        result = await GameService.make_move(channel_id, cell_id, interaction.user.id)
        
        if result.get("error"):
            await interaction.followup.send(f"❌ {result['error']}", ephemeral=True)
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
        
    except Exception as e:
        logger.error(f"❌ Ошибка в обработчике: {e}", exc_info=True)
        try:
            await interaction.followup.send(f"❌ Произошла ошибка: {str(e)}", ephemeral=True)
        except:
            pass