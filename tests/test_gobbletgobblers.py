# coding=utf-8
import unittest
import gobbletgobblers as game


class TestState(unittest.TestCase):
    # 初期化のテスト
    # 以下の条件で正しく初期化ができる
    #   - 空
    #   - smallのみ
    #   - largeのみ
    #   - smallとlargeの重なりなし
    #   - smallとlargeの重なりあり
    #   - smallとlargeの重なりあり色重なりあり
    def test___init__(self):
        patterns = [
            # 空
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0])),

            # smallのみ
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0])),

            # largeのみ
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ox-
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0])),

            # small, large重なりなし
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ox-
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0])),

            # small, large重なりあり
            #  small
            #   ox-
            #   ---
            #   ox-
            #  large
            #   ---
            #   ox-
            #   ox-
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ox-
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]),
             ([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0])),

            # # small, large重なりあり色重なり
            #  small
            #   oxo
            #   --x
            #   ox-
            #  large
            #   --o
            #   oxx
            #   ox-
            #    ↓
            #
            # visible
            #   oxo
            #   oxx
            #   ox-
            (([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0]),
             ([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 1, 0])),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # my_xx_pieces, enemy_xx_pieces, ... , enemy_xx_pieces
            actual = state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces, state.my_visible_pieces, state.enemy_visible_pieces
            self.assertEqual(expect, actual)

    # コマのカウントのテスト
    # 以下の条件で正しくカウントができる
    # - 0つ
    # - 1つ
    # - 2つ
    # - 9つ
    def test_piece_count(self):
        patterns = [
            # 0つ
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], 0),
            # piece
            #  ---
            #  ---
            #  ---

            # 1つ
            ([1, 0, 0, 0, 0, 0, 0, 0, 0], 1),
            # piece
            #  o--
            #  ---
            #  ---

            # 2つ
            ([0, 0, 1, 0, 1, 0, 0, 0, 0], 2),
            # piece
            #  --o
            #  -o-
            #  ---

            # 9つ
            ([1, 1, 1, 1, 1, 1, 1, 1, 1], 9),
            # piece
            #  ooo
            #  ooo
            #  ooo
        ]
        for input_param, expect_param in patterns:
            pieces = input_param
            state = game.State()
            expect = expect_param  # num of pieces
            actual = state.piece_count(pieces)
            self.assertEqual(expect, actual)

    # 勝敗判定のテスト
    # 以下の条件で正しく負けを判定できる
    # - visible上で(ここではsmallで)
    #   - 負けていない(空)
    #   - 負けていない(oなし、x揃わず)
    #   - 負けていない(o,x揃わず)
    #   - 勝っている(oが揃う,x揃わず=負けていない)
    #   - 縦並び(0,3,6)
    #   - 縦並び(1,4,7)
    #   - 縦並び(2,5,8)
    #   - 横並び(0,1,2)
    #   - 横並び2(3,4,5)
    #   - 横並び3(6,7,8)
    #   - 斜め並び1(0,4,8)
    #   - 斜め並び2(2,4,6)
    def test_is_lose(self):
        patterns = [
            # 負けていない(空)
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None), False),

            # 負けていない(oなし、x揃わず)
            #  small
            #   -x-
            #   x-x
            #   -x-
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   -x-
            #   x-x
            #   -x-
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0], None, None), False),

            # 負けていない(o,x揃わず)
            #  small
            #   xox
            #   xox
            #   oxo
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   xox
            #   xox
            #   oxo
            (([0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1, 0, 1, 0], None, None), False),

            # 勝っている(oが揃う,x揃わず=負けていない)
            #  small
            #   xox
            #   ooo
            #   xox
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #  small
            #   xox
            #   ooo
            #   xox
            (([0, 1, 0, 1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0, 1, 0, 1], None, None), False),

            # 縦並び(0,3,6)
            #  small
            #   x--
            #   x--
            #   x--
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   x--
            #   x--
            #   x--
            ((None, [1, 0, 0, 1, 0, 0, 1, 0, 0], None, None), True),

            # 縦並び(1,4,7)
            #  small
            #   -x-
            #   -x-
            #   -x-
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   -x-
            #   -x-
            #   -x-
            ((None, [0, 1, 0, 0, 1, 0, 0, 1, 0], None, None), True),

            # 縦並び(2,5,8)
            #  small
            #   --x
            #   --x
            #   --x
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   --x
            #   --x
            #   --x
            ((None, [0, 0, 1, 0, 0, 1, 0, 0, 1], None, None), True),

            # 横並び(0,1,2)
            #  small
            #   xxx
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   xxx
            #   ---
            #   ---
            ((None, [1, 1, 1, 0, 0, 0, 0, 0, 0], None, None), True),

            # 横並び(3,4,5)
            #  small
            #   ---
            #   xxx
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   xxx
            #   ---
            ((None, [0, 0, 0, 1, 1, 1, 0, 0, 0], None, None), True),

            # 横並び(6,7,8)
            #  small
            #   ---
            #   ---
            #   xxx
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   xxx
            ((None, [0, 0, 0, 0, 0, 0, 1, 1, 1], None, None), True),

            # 斜め並び1(0,4,8)
            #  small
            #   x--
            #   -x-
            #   --x
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   x--
            #   -x-
            #   --x
            ((None, [1, 0, 0, 0, 1, 0, 0, 0, 1], None, None), True),

            # 斜め並び2(2,4,6)
            #  small
            #   --x
            #   -x-
            #   x--
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   --x
            #   -x-
            #   x--
            ((None, [0, 0, 1, 0, 1, 0, 1, 0, 0], None, None), True),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # True or False
            actual = state.is_lose()
            self.assertEqual(expect, actual)

    # 引き分け判定のテスト
    # 以下の条件で正しく引き分けを判定できる
    # - 使用されたコマの合計が9つより少ない(引き分けじゃない)
    #   - 空
    #   - 8つ
    # - 使用されたコマの合計が9つ以上(引き分け)
    #   - 9つ
    #   - 10つ
    def test_is_draw(self):
        patterns = [
            # 空
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None), False),

            # 8つ
            #  small
            #   oxo
            #   x-x
            #   oxo
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   oxo
            #   x-x
            #   oxo
            (([1, 0, 1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], None, None), False),

            # 9つ
            #  small
            #   xox
            #   oox
            #   xxo
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   xox
            #   oox
            #   xxo
            (([0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1, 1, 1, 0], None, None), True),

            # 10つ
            #  small
            #   xox
            #   oox
            #   xxo
            #  large
            #   ---
            #   -o-
            #   ---
            #    ↓
            #
            # visible
            #   xox
            #   oox
            #   xxo
            (([0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], None), True),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # True or False
            actual = state.is_done()
            self.assertEqual(expect, actual)

    # 合法手探索のテスト
    # - 空いているマスにはおける
    # - 同じ大きさのコマがあるところにはおけない(small)
    # - 同じ大きさのコマがあるところにはおけない(large)
    # - largeがあるマスにsmallはおけない, smallがあるマスにlargeはおける(small, large重なりなし)
    # -  largeがあるマスにsmallはおけない, smallがあるマスにlargeはおける(small, large重なりあり)
    def test_legal_actions(self):
        patterns = [
            # 空いているマスにはおける
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),

            # 同じ大きさのコマがあるところにはおけない(small)
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], None, None),
             [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),

            # 同じ大きさのコマがあるところにはおけない(large)
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ox-
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            ((None, None, [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]),
             [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17]),

            # largeがあるマスにsmallはおけない, smallがあるマスにlargeはおける(small, large重なりなし)
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ox-
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]), [2, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17]),

            # largeがあるマスにsmallはおけない, smallがあるマスにlargeはおける(small, large重なりあり)
            #  small
            #   ox-
            #   ---
            #   ox-
            #  large
            #   ---
            #   ox-
            #   ox-
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ox-
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]), [2, 5, 8, 9, 10, 11, 14, 17])
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # expect_param == [0, 1, 2, 3, ... , 16, 17]
            actual = state.legal_actions()
            self.assertEqual(expect, actual)

    # my_xx_piece, enemy_xx_piece (visible除く)をタプルで取得する関数のテスト
    # 空
    # small, large それぞれのコマあり
    def test_get_pieces_for_tuple(self):
        patterns = [
            # 空
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None),
             ((0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0),
              (0, 0, 0, 0, 0, 0, 0, 0, 0))),

            # 空
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None),
             ((0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0),
              (0, 0, 0, 0, 0, 0, 0, 0, 0))),

            # small, large それぞれのコマあり
            #  small
            #   o-x
            #   o-x
            #   ---
            #  large
            #   ---
            #   x-o
            #   x-o
            #    ↓
            #
            # visible
            #   ---
            #   x-o
            #   x-o
            (([1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1],
              [0, 0, 0, 1, 0, 0, 1, 0, 0]),
             ((1, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 1),
              (0, 0, 0, 1, 0, 0, 1, 0, 0))),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # expect_param == string
            actual = state.get_pieces_for_tuple()
            self.assertEqual(expect, actual)

    # get_pieces_for_binaryのテスト
    # 以下の条件で適切にビット変換できているか確かめる
    # - 空
    # - my_small_piecesで構成される盤面
    # - enemy_small_piecesで構成される盤面
    # - my_large_piecesで構成される盤面
    # - enemy_large_piecesで構成される盤面
    # - my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_piecesで構成される盤面
    def test_get_pieces_for_binary(self):
        patterns = [
            # 空
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None), 0),

            # my_small_piecesで構成される盤面
            #  small
            #   o--
            #   oo-
            #   ooo
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   o--
            #   oo-
            #   ooo
            (([1, 0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], None, None),
             0b111_011_001_000_000_000_000_000_000_000_000_000),

            # enemy_small_piecesで構成される盤面
            #  small
            #   x--
            #   xx-
            #   xxx
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   x--
            #   xx-
            #   xxx
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1, 1], None, None),
             0b000_000_000_111_011_001_000_000_000_000_000_000),

            # my_large_piecesで構成される盤面
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   o--
            #   oo-
            #   ooo
            #    ↓
            #
            # visible
            #   o--
            #   oo-
            #   ooo
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]), 0b000_000_000_000_000_000_111_011_001_000_000_000),

            # enemy_large_piecesで構成される盤面
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   x--
            #   xx-
            #   xxx
            #    ↓
            #
            # visible
            #   x--
            #   xx-
            #   xxx
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 1, 0, 1, 1, 1]), 0b000_000_000_000_000_000_000_000_000_111_011_001),

            # my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_piecesで構成される盤面
            #  small
            #   ox-
            #   ---
            #   ox-
            #  large
            #   ---
            #   ox-
            #   ox-
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ox-
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]), 0b001_000_001_010_000_010_001_001_000_010_010_000),

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # bit化した盤面
            actual = state.get_pieces_for_binary()
            self.assertEqual(expect, actual)

    # 表示のテスト
    # 以下の条件で正しく表示ができる
    #   - 空
    #   - smallのみ
    #   - largeのみ
    #   - smallとlargeの重なりなし
    #   - smallとlargeの重なりあり
    #   - smallとlargeの重なりあり色重なりあり
    def test___str__(self):
        patterns = [
            # 空
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None),
             " small\n"
             "  ---\n"
             "  ---\n"
             "  ---\n  "
             "\r large\n"
             "  ---\n"
             "  ---\n"
             "  ---\n  "
             "\r   ↓\n"
             "\n"
             "visible\n"
             "  ---\n"
             "  ---\n"
             "  ---\n  "),

            # smallのみ
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], None, None),
             " small\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "
             "\r large\n"
             "  ---\n"
             "  ---\n"
             "  ---\n  "
             "\r   ↓\n"
             "\n"
             "visible\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "),

            # largeのみ
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ox-
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            ((None, None, [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]),
             " small\n"
             "  ---\n"
             "  ---\n"
             "  ---\n  "
             "\r large\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "
             "\r   ↓\n"
             "\n"
             "visible\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "),

            # small, large重なりなし
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ox-
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]),
             " small\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "
             "\r large\n"
             "  ---\n"
             "  ox-\n"
             "  ---\n  "
             "\r   ↓\n"
             "\n"
             "visible\n"
             "  ox-\n"
             "  ox-\n"
             "  ---\n  "),

            # small, large重なりあり
            #  small
            #   ox-
            #   ---
            #   ox-
            #  large
            #   ---
            #   ox-
            #   ox-
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ox-
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]),
             " small\n"
             "  ox-\n"
             "  ---\n"
             "  ox-\n  "
             "\r large\n"
             "  ---\n"
             "  ox-\n"
             "  ox-\n  "
             "\r   ↓\n"
             "\n"
             "visible\n"
             "  ox-\n"
             "  ox-\n"
             "  ox-\n  "),

            # small, large重なりあり色重なり
            #  small
            #   oxo
            #   --x
            #   ox-
            #  large
            #   --o
            #   oxx
            #   ox-
            #    ↓
            #
            # visible
            #   oxo
            #   oxx
            #   ox-
            (([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0]),
             " small\n"
             "  oxo\n"
             "  --x\n"
             "  ox-\n  "
             "\r large\n"
             "  --o\n"
             "  oxx\n"
             "  ox-\n  "
             "\r   ↓\n"
             "\n"
             "visible\n"
             "  oxo\n"
             "  oxx\n"
             "  ox-\n  "),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # expect_param == string
            actual = str(state)
            self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
