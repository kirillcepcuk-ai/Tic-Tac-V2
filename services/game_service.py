from typing import List, Dict, Any, Optional
from repositories.game_repository import GameRepository # type: ignore
from utils.helpers import check_winner # type: ignore

class GameService:
    @staticmethod
    async def get_game(channel_id: str) -> Optional[Any]:
        return await GameRepository.get_game(channel_id)

    @staticmethod
    async def create_game(channel_id: str, players: List[int]) -> Dict[str, Any]:
        game = await GameRepository.create_game(channel_id, players)
        return {
            "board": game.board,
            "turn": game.turn,
            "players": game.players
        }

    @staticmethod
    async def make_move(channel_id: str, cell_id: int, user_id: int) -> Dict[str, Any]:
        game = await GameRepository.get_game(channel_id)
        if not game:
            return {"error": "game_not_found"}
        board = game.board.copy()
        turn = game.turn
        players = game.players
        if user_id != turn:
            return {"error": "not_your_turn"}
        if board[cell_id] != " ":
            return {"error": "cell_taken"}
        symbol = "X" if turn == players[0] else "O"
        board[cell_id] = symbol
        winner = check_winner(board)
        if winner:
            await GameRepository.delete_game(channel_id)
            if winner == "X":
                await GameRepository.update_stats(players[0], "win")
                await GameRepository.update_stats(players[1], "loss")
            elif winner == "O":
                await GameRepository.update_stats(players[1], "win")
                await GameRepository.update_stats(players[0], "loss")
            else:
                await GameRepository.update_stats(players[0], "tie")
                await GameRepository.update_stats(players[1], "tie")
            return {
                "status": "finished",
                "winner": winner,
                "board": board,
                "players": players
            }
        if " " not in board:
            await GameRepository.delete_game(channel_id)
            await GameRepository.update_stats(players[0], "tie")
            await GameRepository.update_stats(players[1], "tie")
            return {
                "status": "finished",
                "winner": "tie",
                "board": board,
                "players": players
            }
        turn = players[1] if turn == players[0] else players[0]
        game.board = board
        game.turn = turn
        await GameRepository.update_game(game)
        return {
            "status": "continue",
            "board": board,
            "turn": turn,
            "players": players
        }

    @staticmethod
    async def update_message_id(channel_id: str, message_id: int) -> None:
        await GameRepository.update_message_id(channel_id, message_id)

    @staticmethod
    async def get_all_active_games() -> List[Any]:
        return await GameRepository.get_all_active_games()

    @staticmethod
    async def stop_game(channel_id: str) -> Dict[str, Any]:
        game = await GameRepository.get_game(channel_id)
        if not game:
            return {"error": "Активная игра не найдена"}
        
        players = game.players
        await GameRepository.delete_game(channel_id)
        
        await GameRepository.update_stats(players[0], "loss")
        await GameRepository.update_stats(players[1], "loss")
        
        return {"status": "stopped"}

    @staticmethod
    async def get_stats(user_id: int) -> Optional[Any]:
        return await GameRepository.get_stats(user_id)