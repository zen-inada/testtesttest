from abc import ABC, abstractmethod
from typing import Tuple, List
import random

Board = List[List[List[int]]]  # board[z][y][x]（0=空, 1=黒, 2=白）

class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        """(x, y) を返す。0 <= x < 4, 0 <= y < 4"""
        ...

class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        # ハンドシェイク出力
        print("send_board")

        candidates = []
        for y in range(4):
            for x in range(4):
                # (x, y) の列に空きがあるか？
                if any(board[z][y][x] == 0 for z in range(4)):
                    score = self.evaluate_move(board, x, y)
                    candidates.append(((x, y), score))

        if not candidates:
            return (0, 0)

        # 最大スコアを持つ候補を抽出
        max_score = max(score for _, score in candidates)
        best_moves = [pos for pos, score in candidates if score == max_score]

        # 複数ある場合はランダムで決定
        return random.choice(best_moves)

    def evaluate_move(self, board: Board, x: int, y: int) -> int:
        """
        簡易評価関数:
        - 中央に近いほどプラス
        - 低い層に置けるほどプラス
        """
        # 中央への近さ（マンハッタン距離で）
        center_bonus = 3 - (abs(x - 1.5) + abs(y - 1.5))

        # 置ける高さを計算（下から最初に空いている層）
        z = next((z for z in range(4) if board[z][y][x] == 0), 3)
        height_bonus = (3 - z)  # 低いほど有利

        return int(center_bonus * 10 + height_bonus)

_ai = MyAI()

def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
