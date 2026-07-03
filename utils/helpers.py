from typing import List, Optional, Union
from config import WIN_COMBINATIONS # type: ignore

def check_winner(board: List[str]) -> Optional[Union[str, None]]:
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "tie"
    return None