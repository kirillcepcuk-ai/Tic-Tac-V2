import discord # type: ignore
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore
from services.game_service import GameService # pyright: ignore[reportMissingImports]

class StatsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="stats", description="Показать свою статистику")
    async def stats(self, interaction: discord.Interaction) -> None:
        stats = await GameService.get_stats(interaction.user.id)
        if not stats:
            embed = discord.Embed(
                title="📊 Статистика",
                description=f"У {interaction.user.display_name} пока нет игр",
                color=0x3498DB
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        embed = discord.Embed(
            title=f"📊 Статистика {interaction.user.display_name}",
            color=0x3498DB
        )
        embed.add_field(name="🏆 Победы", value=stats.wins, inline=True)
        embed.add_field(name="💔 Поражения", value=stats.losses, inline=True)
        embed.add_field(name="🤝 Ничьи", value=stats.ties, inline=True)
        total = stats.wins + stats.losses + stats.ties
        if total > 0:
            winrate = round(stats.wins / total * 100, 1)
            embed.set_footer(text=f"Всего игр: {total} | Винрейт: {winrate}%")
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StatsCog(bot))