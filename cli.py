import logging, csv
from logic import TicTacToeLogic
from datetime import datetime

class TicTacToeCLI:
    def __init__(self, logic):
        self.logic = logic

    def play_game(self):
        player1_name = input("Enter Player 1 name: ")
        player2_name = input("Enter Player 2 name (or 'bot' for AI): ")

        log_file = 'logs/tictactoe_game_log.csv'
        fieldnames = ['Game Time', 'Player 1 Name', 'Player 2 Name', 'Draw', 'Winner']
        #Only run this once, to set header
        # with open(log_file, 'w', newline='') as csvfile:
        #     csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     csv_writer.writeheader()

        board = self.logic.make_empty_board()
        start_time = datetime.now()
        winner = None
        char = 'X'
        # logging.basicConfig(filename='logs/game.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)
        # logging.info('New Game begin')
        game_type = logic.select_game_type()

        while winner is None:
            print("-------------------------------------")
            logging.info("Turn Begins")
            print("Begin Turn!")
            print("It's", char, "turn!")

            # Log player names
            player = player1_name if char == 'X' else player2_name
            timestamp = datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
            move = ''


            self.logic.show_current_board(board=board)
            if self.logic.get_current_player() == 'X' or game_type == 2:
                print("Enter the row and column of the board you want to add the move to:")
                i = int(input("Enter the row number (Options- 1 | 2 | 3):"))
                j = int(input("Enter the column (Options- 1 | 2 | 3):"))

                board, is_illegal = self.logic.make_move(board=board, i=i, j=j)
                # if an illegal move happens, do not change the turn
                if not is_illegal:
                    winner = self.logic.get_winner(board)
            else:
                self.logic.make_bot_move(board=board)
                move = 'Bot'
            winner = self.logic.get_winner(board)

            if winner!= None:
                end_time = datetime.now()
                game_time = (end_time - start_time).total_seconds()

                player_winner = ' '

                if winner == 'X':
                    player_winner = player1_name
                elif winner == 'O' and game_type == 2:
                    player_winner = player2_name
                elif winner == 'O' and game_type == 1:
                    player_winner = 'Bot'


                with open(log_file, 'a', newline='') as csvfile:
                    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    csv_writer.writerow({'Game Time': game_time, 'Player 1 Name': player1_name, 'Player 2 Name': player2_name,
                                        'Draw': winner == 'Draw', 'Winner': player_winner})

            print("Winner",winner)
            if winner == 'Draw':
                print("Game Draw")
            else:
                logging.info("Winner")

if __name__ == '__main__':
    logic = TicTacToeLogic()
    cli = TicTacToeCLI(logic)
    cli.play_game()

