from typing import List, Optional, Union
from config import WIN_COMBINATIONS # type: ignore

def check_winner(board: List[str]) -> Optional[Union[str, None]]:
    """
    Проверить, есть ли победитель на доске.

    Args:
        board: Список из 9 элементов ('X', 'O', ' ')

    Returns:
        'X' или 'O' если есть победитель,
        'tie' если ничья,
        None если игра продолжается
    """
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "tie"
    return None
