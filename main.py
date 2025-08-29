from abc import ABC, abstractmethod
from typing import Tuple, List

Board = List[List[List[int]]]  # board[z][y][x]（0=空, 1=黒, 2=白）

class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        """(x, y) を返す。0 <= x < 4, 0 <= y < 4"""
        ...

class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        # ハンドシェイク
        print("send_board")

        best_score = -10**9
        best_pos = (0, 0)

        for y in range(4):
            for x in range(4):
                if any(board[z][y][x] == 0 for z in range(4)):
                    score = self.evaluate_move(board, x, y)
                    # 決定論的に優先順位をつける（スコア → y → x）
                    if (score > best_score) or (score == best_score and (y, x) < (best_pos[1], best_pos[0])):
                        best_score = score
                        best_pos = (x, y)

        return best_pos

    def evaluate_move(self, board: Board, x: int, y: int) -> int:
        """
        決定論的な簡易評価:
        - 中央に近いほど高得点
        - 低い層に置けるほど高得点
        """
        center_bonus = 3 - (abs(x - 1.5) + abs(y - 1.5))
        z = next((z for z in range(4) if board[z][y][x] == 0), 3)
        height_bonus = (3 - z)
        return int(center_bonus * 10 + height_bonus)

_ai = MyAI()

def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
