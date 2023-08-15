import unittest
import tictactoe

class TestTicTacToe(unittest.TestCase):
    def test_clear(self):
        tictactoe.board_clear()
        for row in range(3):
            for col in range(3):
                self.assertEqual(tictactoe.board_spots[row][col], " ")
        self.assertEqual(tictactoe.board_width, 12)
        self.assertEqual(tictactoe.board_height, 5)
        self.assertEqual(tictactoe.player, "X")

    def test_set_spot(self):
        tictactoe.board_clear()
        self.assertTrue(tictactoe.board_set_spot(0, "X"))
        self.assertFalse(tictactoe.board_set_spot(0, "O"))

    def test_is_full(self):
        tictactoe.board_clear()
        self.assertFalse(tictactoe.board_is_full())
        for spot in range(9):
            tictactoe.board_set_spot(spot, "X")
        self.assertTrue(tictactoe.board_is_full())

    def test_winner(self):
        tictactoe.board_clear()
        winner, win_type, win_spot = tictactoe.board_get_winner()
        self.assertIsNone(winner)
        for player in ("X", "O"):
            # Horizontal
            for row in range(3):
                tictactoe.board_clear()
                tictactoe.board_set_spot(row * 3 + 0, player)
                tictactoe.board_set_spot(row * 3 + 1, player)
                tictactoe.board_set_spot(row * 3 + 2, player)
                winner, win_type, win_spot = tictactoe.board_get_winner()
                self.assertEqual(winner, player, "Horizontal %d" % (row))
                self.assertEqual(win_type, "h", "Horizontal %d type" % (row))
                self.assertEqual(win_spot, row, "Horizontal %d spot" % (row))
            # Vertical
            for col in range(3):
                tictactoe.board_clear()
                tictactoe.board_set_spot(col + 0, player)
                tictactoe.board_set_spot(col + 3, player)
                tictactoe.board_set_spot(col + 6, player)
                winner, win_type, win_spot = tictactoe.board_get_winner()
                self.assertEqual(winner, player, "Vertical %d" % (col))
                self.assertEqual(win_type, "v", "Vertical %d type" % (col))
                self.assertEqual(win_spot, col, "Vertical %d spot" % (col))
            # Diagonal left
            tictactoe.board_clear()
            tictactoe.board_set_spot(0, player)
            tictactoe.board_set_spot(4, player)
            tictactoe.board_set_spot(8, player)
            winner, win_type, win_spot = tictactoe.board_get_winner()
            self.assertEqual(winner, player, "Diagonal left %d" % (col))
            self.assertEqual(win_type, "d", "Diagonal left %d type" % (col))
            self.assertEqual(win_spot, "left", "Diagonal left %d spot" % (col))
            # Diagonal right
            tictactoe.board_clear()
            tictactoe.board_set_spot(2, player)
            tictactoe.board_set_spot(4, player)
            tictactoe.board_set_spot(6, player)
            winner, win_type, win_spot = tictactoe.board_get_winner()
            self.assertEqual(winner, player, "Diagonal right %d" % (col))
            self.assertEqual(win_type, "d", "Diagonal right %d type" % (col))
            self.assertEqual(win_spot, "right", "Diagonal right %d spot" % (col))

if __name__ == '__main__':
    unittest.main()