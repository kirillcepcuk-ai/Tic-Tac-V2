import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.helpers import check_winner # type: ignore

def test_check_winner_row_x() -> None:
    board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert check_winner(board) == "X"

def test_check_winner_row_o() -> None:
    board = ["O", "O", "O", " ", " ", " ", " ", " ", " "]
    assert check_winner(board) == "O"

def test_check_winner_column() -> None:
    board = ["X", " ", " ", "X", " ", " ", "X", " ", " "]
    assert check_winner(board) == "X"

def test_check_winner_diagonal() -> None:
    board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
    assert check_winner(board) == "X"
    
def test_check_winner_tie() -> None:
    board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
    assert check_winner(board) == "tie"

def test_check_winner_no_winner() -> None:
    board = ["X", "O", " ", " ", "X", " ", " ", " ", "O"]
    assert check_winner(board) is None

def test_check_winner_empty() -> None:
    board = [" "]*9
    assert check_winner(board) is None

def test_check_winner_row_x_different() -> None:
    board = [" ", " ", " ", "X", "X", "X", " ", " ", " "]
    assert check_winner(board) == "X"

def test_check_winner_row_o_different() -> None:
    board = [" ", " ", " ", " ", " ", " ", "O", "O", "O"]
    assert check_winner(board) == "O"

def test_check_winner_column_o() -> None:
    board = [" ", "O", " ", " ", "O", " ", " ", "O", " "]
    assert check_winner(board) == "O"

def test_check_winner_diagonal_o() -> None:
    board = [" ", " ", "O", " ", "O", " ", "O", " ", " "]
    assert check_winner(board) == "O"