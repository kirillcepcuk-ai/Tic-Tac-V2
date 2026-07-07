import discord
from discord.ext import commands
import os
import logging
from logging.handlers import RotatingFileHandler
from services.game_service import GameService
from ui import TicTacToeView
from embeds import game_embed
from utils.render import get_player_names

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

file_handler = RotatingFileHandler(
    "bot.log",
    maxBytes=5_242_880,
    backupCount=5,
    encoding="utf-8"
)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

async def restore_active_games() -> None:
    games = await GameService.get_all_active_games()
    if not games:
        return
    logger.info(f"🔄 Восстанавливаем {len(games)} активных игр...")
    for game in games:
        try:
            channel = bot.get_channel(int(game.channel_id))
            if not channel:
                logger.warning(f"❌ Канал {game.channel_id} не найден")
                continue
            try:
                msg = await channel.fetch_message(int(game.message_id))
                if msg:
                    view = TicTacToeView(game.board, game.channel_id, game.turn)
                    player1_name, player2_name = await get_player_names(bot, game.players)
                    embed = game_embed(game.board, game.turn, player1_name, player2_name)
                    await msg.edit(embed=embed, view=view)
                    logger.info(f"✅ Восстановлена игра в канале {game.channel_id}")
            except discord.NotFound:
                logger.warning(f"❌ Сообщение {game.message_id} не найдено")
                await GameService.update_message_id(game.channel_id, None)
            except Exception as e:
                logger.error(f"❌ Ошибка восстановления: {e}")
        except Exception as e:
            logger.error(f"❌ Ошибка: {e}")

@bot.event
async def on_ready() -> None:
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and file != "__init__.py":
            await bot.load_extension(f"cogs.{file[:-3]}")
            logger.info(f"✅ Загружен {file}")
    await bot.tree.sync()
    logger.info(f"✅ {bot.user} запущен")
    logger.info("✅ Команды синхронизированы")
    await restore_active_games()

@bot.event
async def on_interaction(interaction: discord.Interaction) -> None:
    from events import on_interaction as handle_interaction
    await handle_interaction(interaction)

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
    logger.error(f"❌ Ошибка команды: {error}")
