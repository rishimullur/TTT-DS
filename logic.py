# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random

class TicTacToeLogic:
    def __init__(self):
        self.current_player = 'X'

    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def select_game_type(self):
        print("Choose Type of Game: 1. Single Player 2.Two-Player")
        game_type = int(input("Option:"))
        if game_type == 1:
            print("Single Player Mode selected!")
            return game_type
        elif game_type == 2:
            print("Two Player Mode Selected!")
            return game_type


# Main logic for the winner of a given board
    def get_winner(self,board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        for i in board:
            if i[0]==i[1]==i[2]=='X':
                print('X won')
                return 'X'
            elif i[0]==i[1]==i[2]=='O':
                print('O won')
                return 'O'

        for j in range(3):
        # print(board[0][j])
            if board[0][j]==board[1][j]==board[2][j]=='X':
                print('X won')
                return 'X'
            elif board[0][j]==board[1][j]==board[j]=='O':
                print('O won')
                return 'O'

        if board[0][0]==board[1][1]==board[2][2]=='X':
            print('X won')
            return 'X'
        elif board[0][0]==board[1][1]==board[2][2]=='0':
            print('O won')
            return 'O'
        
        if board[0][2] == board[1][1] == board[2][0] == 'X':
            return 'X'
        elif board[0][2] == board[1][1] == board[2][0] == 'O':
            return 'O'
        
        # Check for a draw
        for row in board:
            if None in row:
                return None
        return 'Draw'  

    def make_bot_move(self, board):
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        if available_moves:
            i, j = random.choice(available_moves)
            board[i][j] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("No available moves for the bot.")

    def other_player(self,player):
        """Given the character for a player, returns the other player."""
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def update_board(self,board,i,j,char):
        """Updates the playing board to account for the new move of a user"""
        #Making the row and column accept easier row/column values for users
        i = i-1
        j = j-1
        if i < 0 or j < 0:
            print("No such row or column")
            return board
        if i >=3 or j >=3:
            print("No such row or column")
            return board
        if board[i][j] == None:
            board[i][j] = char
            return board, False
        else:
            print("Illegal move!")
            return board, True

    def show_current_board(self,board):
        print(board[0])
        print(board[1])
        print(board[2])
    
    def get_current_player(self):
        return self.current_player
    
    def make_move(self, board, i, j):
        i = i-1
        j = j-1
        if i < 0 or j < 0:
            print("No such row or column")
            return board
        if i >=3 or j >=3:
            print("No such row or column")
            return board
        if board[i][j] is None:
            board[i][j] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return board, False  # Move successful
        else:
            print("Illegal move. Try again.")
            return board, True  # Move unsuccessful


