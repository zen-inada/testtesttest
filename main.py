# === main.py（このファイルで「MyAI.get_move」以外は変更しないでください）===

from abc import ABC, abstractmethod
from typing import Tuple, List

Board = List[List[List[int]]]  # board[z][y][x]（0=空, 1=黒, 2=白）

# 変更禁止: 親インターフェース
class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        """(x, y) を返す。0 <= x < 4, 0 <= y < 4"""
        ...


# ここから自由にアルゴリズムを記入 ----------------------------------------
class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        """
        テスト用アルゴリズム:
        左上から順に、まだ石が置かれていない (z=0〜3 全層で空き) マスを探して返す。
        """
        for y in range(4):
            for x in range(4):
                # その座標に石が置けるか（全層空いているか簡易チェック）
                can_place = True
                for z in range(4):
                    if board[z][y][x] != 0:
                        can_place = False
                        break
                if can_place:
                    return (x, y)

        # 万が一全て埋まっていた場合は (0,0) を返す
        return (0, 0)
# ----------------------------------------------------------------------

# 変更禁止: サーバが呼ぶエントリポイント（削除・変更しない）
_ai = MyAI()

def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
