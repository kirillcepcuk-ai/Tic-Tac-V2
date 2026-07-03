# 🎮 Tic-Tac-Toe Discord Bot

## 📊 Tech Stack

| Technology | Badge |
|------------|-------|
| Python 3.13 | [![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) |
| discord.py 2.7.1 | [![Discord.py](https://img.shields.io/badge/discord.py-2.7.1-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/Rapptz/discord.py) |
| PostgreSQL 16 | [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) |
| SQLAlchemy 2.0 | [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-CC0000?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/) |
| Docker 20.10 | [![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) |
| Ruff | [![Ruff](https://img.shields.io/badge/Ruff-000000?style=for-the-badge&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff) |
| Pytest 9.1 | [![Pytest](https://img.shields.io/badge/Pytest-9.1-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/) |
| License MIT | [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE) |


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

- Play Tic-Tac-Toe with friends
- Games survive bot restarts
- Track your win/loss/tie stats
- Docker support for easy deployment

---

## 🏗️ Project Structure
```
tic-tac-toe-bot/
├── main.py
├── bot.py
├── events.py
├── config.py
├── database.py
├── embeds.py
├── ui.py
├── conftest.py
├── Makefile
├── docker-compose.yml
├── Dockerfile
├── alembic.ini
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── cogs/
│ ├── init.py
│ ├── game.py
│ ├── help.py
│ ├── stats.py
│ └── stop.py
├── services/
│ ├── init.py
│ └── game_service.py
├── repositories/
│ ├── init.py
│ └── game_repository.py
├── utils/
│ ├── init.py
│ ├── helpers.py
│ └── render.py
├── tests/
│ ├── init.py
│ └── test_helpers.py
└── migrations/
├── env.py
├── script.py.mako
└── versions/
└── .gitkeep
```

## 🚀 Installation

### Local Setup

```bash
# Clone repository
git clone https://github.com/kirillcepcuk-ai/Tic-Tac-V2
cd Tic-Tac-V2

# Install dependencies
make install
# or
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Discord token

# Run migrations
make migrate
# or
alembic upgrade head

# Start bot
make run
# or
python main.py
```

### Docker Setup

```bash
# Configure environment
cp .env.example .env

# Start containers
docker-compose up -d

# View logs
docker-compose logs -f bot

# Stop containers
docker-compose down
```

### 🧪 Running Tests

```bash
make test
# or
pytest -v
```

### 🎯 Make Commands

```bash
make install    # Install dependencies
make migrate    # Run database migrations
make run        # Start bot
make test       # Run tests
make format     # Format code with Ruff
make clean      # Clean cache files
```

📝 License
MIT
