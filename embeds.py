from typing import List, Union
import discord # type: ignore

def game_embed(board: List[str], turn: int, player1: str, player2: str) -> discord.Embed:
    field = ""
    for i in range(0, 9, 3):
        row = board[i:i+3]
        field += " ".join([f"`{cell}`" for cell in row]) + "\n"
    
    embed = discord.Embed(
        title="🎮 Крестики-нолики",
        description=f"**Ход:** <@{turn}>\n\n{field}",
        color=0x9B59B6
    )
    embed.set_footer(text=f"❌ {player1} VS {player2} ⭕")
    return embed

def win_embed(winner: str, player1: int, player2: int) -> discord.Embed:
    if winner == "tie":
        return discord.Embed(
            title="🤝 Ничья!",
            color=0xF1C40F
        )
    
    winner_id = player1 if winner == "X" else player2
    return discord.Embed(
        title="🏆 Победа!",
        description=f"Победил: <@{winner_id}>",
        color=0xFFD700
    )