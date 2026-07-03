import asyncio
from typing import List, Optional
from sqlalchemy import select # type: ignore
from database import AsyncSessionLocal, Game as GameModel, PlayerStats # type: ignore

class GameRepository:
    _lock = asyncio.Lock()

    @staticmethod
    async def create_game(channel_id: str, players: List[int]) -> GameModel:
        async with GameRepository._lock:
            async with AsyncSessionLocal() as session:
                existing = await session.get(GameModel, channel_id)
                if existing:
                    await session.delete(existing)
                    await session.commit()
                game = GameModel(
                    channel_id=channel_id,
                    board=[" "]*9,
                    turn=players[0],
                    players=players
                )
                session.add(game)
                await session.commit()
                return game

    @staticmethod
    async def get_game(channel_id: str) -> Optional[GameModel]:
        async with AsyncSessionLocal() as session:
            return await session.get(GameModel, channel_id)

    @staticmethod
    async def update_game(game: GameModel) -> None:
        async with GameRepository._lock:
            async with AsyncSessionLocal() as session:
                existing = await session.get(GameModel, game.channel_id)
                if existing:
                    existing.board = game.board
                    existing.turn = game.turn
                    existing.message_id = game.message_id
                    await session.commit()

    @staticmethod
    async def delete_game(channel_id: str) -> None:
        async with GameRepository._lock:
            async with AsyncSessionLocal() as session:
                game = await session.get(GameModel, channel_id)
                if game:
                    await session.delete(game)
                    await session.commit()

    @staticmethod
    async def update_message_id(channel_id: str, message_id: int) -> None:
        async with GameRepository._lock:
            async with AsyncSessionLocal() as session:
                game = await session.get(GameModel, channel_id)
                if game:
                    game.message_id = str(message_id)
                    await session.commit()

    @staticmethod
    async def get_all_active_games() -> List[GameModel]:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(GameModel))
            return result.scalars().all()

    @staticmethod
    async def update_stats(user_id: int, result: str) -> None:
        async with GameRepository._lock:
            async with AsyncSessionLocal() as session:
                stats = await session.get(PlayerStats, user_id)
                if stats is None:
                    stats = PlayerStats(user_id=user_id, wins=0, losses=0, ties=0)
                    session.add(stats)
                if result == "win":
                    stats.wins += 1
                elif result == "loss":
                    stats.losses += 1
                elif result == "tie":
                    stats.ties += 1
                await session.commit()

    @staticmethod
    async def get_stats(user_id: int) -> Optional[PlayerStats]:
        async with AsyncSessionLocal() as session:
            return await session.get(PlayerStats, user_id)