import unittest
from logic import TicTacToeLogic
from cli import TicTacToeCLI


class TestLogic(unittest.TestCase):

#   Check for draw conditions
    def test_get_winner_DRAW(self):
        board = [
            ['X', 'X', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(TicTacToeLogic.get_winner(self, board), 'Draw')

    def test_get_winner_horizontal(self):
        board_1 = [
            ['X', 'X', 'X'],
            ['O', 'O', 'X'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(TicTacToeLogic.get_winner(self, board_1), 'X')

    def test_get_winner(self):
        board_1 = [
            ['O', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(TicTacToeLogic.get_winner(self, board_1), 'X')

    def test_get_winer_lower(self):
        board_1 = [
            ['O', 'O', 'X'],
            ['X', 'X', 'X'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(TicTacToeLogic.get_winner(self, board_1), 'X')


# After one player plays, the other player has a turn
    def test_other_player(self):
        player = 'O'
        self.assertEqual(TicTacToeLogic.other_player(self,player=player),'X')

        
    def test_update_board(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', None],
        ]
        test_case_board = ([['X', 'X', 'O'],[None, 'X', None],[None, 'O', None]],False)
        self.assertEqual(TicTacToeLogic.update_board(self, board,i=1,j=2,char='X'),test_case_board)

# Players can play only in viable spots
    def test_illegal_update_board(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', None],
        ]
        #Assert for illegal Move
        test_case_board = ([['X', None, 'O'],[None, 'X', None],[None, 'O', None]],True)
        self.assertEqual(TicTacToeLogic.update_board(self, board,i=1,j=1,char='X'),test_case_board)

# The game is initialized with an empty board
    def test_intialized_empty(self):
        board = [[None, None, None],
            [None, None, None],
            [None, None, None],]
        self.assertEqual(TicTacToeLogic.make_empty_board(self),board)

if __name__ == '__main__':
    unittest.main()
