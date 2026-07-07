from bot import bot
from config import TOKEN
import asyncio
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except KeyboardInterrupt:
        logger.info("⏹️ Бот остановлен пользователем")
        asyncio.run(bot.close())
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        asyncio.run(bot.close())
