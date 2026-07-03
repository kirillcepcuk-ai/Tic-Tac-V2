import discord # type: ignore
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore

class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="Список команд")
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="📋 Команды",
            description="/gamestart @оппонент — начать игру\n/help — список команд",
            color=0x3498DB
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HelpCog(bot))