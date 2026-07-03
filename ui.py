from typing import List
import discord # type: ignore

class TicTacToeButton(discord.ui.Button):
    def __init__(self, cell_id: int, channel_id: str, label: str, disabled: bool, row: int):
        style_map = {
            "⬜": discord.ButtonStyle.green,
            "❌": discord.ButtonStyle.red,
            "⭕": discord.ButtonStyle.blurple
        }
        style = style_map.get(label, discord.ButtonStyle.grey)
        super().__init__(
            label=label,
            style=style,
            custom_id=f"ttt_{channel_id}_{cell_id}",
            disabled=disabled,
            row=row
        )

class TicTacToeView(discord.ui.View):
    def __init__(self, board: List[str], channel_id: str, turn: int = None):
        super().__init__(timeout=None)
        label_map = {" ": "⬜", "X": "❌", "O": "⭕"}
        
        for i, cell in enumerate(board):
            label = label_map.get(cell, "⬜")
            disabled = cell != " "
            self.add_item(TicTacToeButton(i, channel_id, label, disabled, i // 3))