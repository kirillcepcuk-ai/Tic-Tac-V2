from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, BigInteger, JSON, Integer
from config import DATABASE_URL

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"
    channel_id = Column(String, primary_key=True)
    board = Column(JSON)
    turn = Column(BigInteger)
    players = Column(JSON)
    message_id = Column(String, nullable=True)

class PlayerStats(Base):
    __tablename__ = "player_stats"
    user_id = Column(BigInteger, primary_key=True)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    ties = Column(Integer, default=0)

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_pre_ping=True,
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
