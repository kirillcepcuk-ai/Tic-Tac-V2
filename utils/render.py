import discord # type: ignore
from typing import List, Tuple

async def get_player_names(client: discord.Client, players: List[int]) -> Tuple[str, str]:
    try:
        player1 = await client.fetch_user(players[0])
        player2 = await client.fetch_user(players[1])
        return player1.display_name, player2.display_name
    except discord.NotFound:
        return f"<@{players[0]}>", f"<@{players[1]}>"