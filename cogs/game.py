import discord # type: ignore
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore
from services.game_service import GameService # type: ignore
from ui import TicTacToeView # pyright: ignore[reportMissingImports]
from embeds import game_embed # pyright: ignore[reportMissingImports]

class GameCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="gamestart", description="Начать игру")
    async def gamestart(self, interaction: discord.Interaction, opponent: discord.Member) -> None:
        if opponent.bot or opponent.id == interaction.user.id:
            await interaction.response.send_message("❌ Нельзя играть с ботом или с собой", ephemeral=True)
            return

        await interaction.response.defer()

        channel_id = str(interaction.channel_id)
        players = [interaction.user.id, opponent.id]

        game_data = await GameService.create_game(channel_id, players)
        board = game_data["board"]
        turn = game_data["turn"]

        embed = game_embed(board, turn, interaction.user.display_name, opponent.display_name)
        view = TicTacToeView(board, channel_id, turn)
        
        msg = await interaction.followup.send(embed=embed, view=view)
        await GameService.update_message_id(channel_id, msg.id)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GameCog(bot))