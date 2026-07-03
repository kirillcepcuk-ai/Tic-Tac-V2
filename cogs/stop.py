import discord # type: ignore
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore
from services.game_service import GameService # type: ignore

class StopCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="stop", description="Завершить текущую игру")
    async def stop(self, interaction: discord.Interaction) -> None:
        channel_id = str(interaction.channel_id)
        result = await GameService.stop_game(channel_id)
        if result.get("error"):
            await interaction.response.send_message(f"❌ {result['error']}", ephemeral=True)
            return
        await interaction.response.send_message("⏹️ Игра завершена")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StopCog(bot))