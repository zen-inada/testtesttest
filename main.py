from typing import Tuple
from framework import Alg3D, Board   # ← サーバー側 framework.py を参照

class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        # とりあえず常に (2,2) を返すだけ
        return (2, 2)
