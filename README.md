# 🎮 Tic-Tac-Toe Discord Bot

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.7.1-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/Rapptz/discord.py)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-CC0000?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Ruff](https://img.shields.io/badge/Ruff-000000?style=for-the-badge&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Pytest](https://img.shields.io/badge/Pytest-9.1-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/kirillcepcuk-ai/Tic-Tac-Toe-Discord-bot?style=for-the-badge)](https://github.com/kirillcepcuk-ai/Tic-Tac-Toe-Discord-bot/stargazers)
[![Forks](https://img.shields.io/github/forks/kirillcepcuk-ai/Tic-Tac-Toe-Discord-bot?style=for-the-badge)](https://github.com/kirillcepcuk-ai/Tic-Tac-Toe-Discord-bot/forks)

> Discord bot for playing Tic-Tac-Toe with PostgreSQL, SQLAlchemy 2.0, and clean architecture

---

## 📋 Commands

| Command | Description |
|---------|-------------|
| `/gamestart @opponent` | Start a new game |
| `/stop` | Stop current game |
| `/stats` | Show your statistics |
| `/help` | Show all commands |

---

## ⚡ Features
Play Tic-Tac-Toe with friends

Games survive bot restarts

Track your win/loss/tie stats

Docker support for easy deployment

---

## 🏗️ Project Structure
tic-tac-toe-bot/
├── main.py # Entry point
├── bot.py # Bot + game recovery
├── events.py # Button handlers
├── config.py # Configuration
├── database.py # Database models
├── embeds.py # Discord embeds
├── ui.py # UI components
├── Makefile # Development commands
├── docker-compose.yml # Docker orchestration
├── Dockerfile # Docker build
├── requirements.txt # Dependencies
├── cogs/ # Commands
│ ├── game.py # /gamestart
│ ├── help.py # /help
│ ├── stats.py # /stats
│ └── stop.py # /stop
├── services/ # Business logic
│ └── game_service.py
├── repositories/ # Database layer
│ └── game_repository.py
├── utils/ # Utilities
│ ├── helpers.py # check_winner
│ └── render.py # get_player_names
├── tests/ # Tests
│ └── test_helpers.py
└── migrations/ # Database migrations
└── versions/

---

## 🚀 Installation

### 📦 Local Setup

```bash
# Clone repository
git clone https://github.com/kirillcepcuk-ai/Tic-Tac-Toe-Discord-bot
cd Tic-Tac-Toe-Discord-bot

# Install dependencies
make install
# or
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Discord token

# Run migrations
make migrate

# Start bot
make run

### 🧪 Running Tests
make test
# or
pytest -v

## 🐳 Docker Setup
# Configure environment
cp .env.example .env

# Start containers
docker-compose up -d

# View logs
docker-compose logs -f bot

# Stop containers
docker-compose down

## 📝 License
MIT