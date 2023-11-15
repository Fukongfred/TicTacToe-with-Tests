import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, board):
        pass

class HumanPlayer(Player):
    def move(self, board):
        while True:
            try:
                move = input(f"{self.symbol}'s turn. Enter your move (row,col): ")
                row, col = map(int, move.split(","))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] is None:
                    return (row, col)
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter the move as row,col. Example: 1,2")

class BotPlayer(Player):
    def move(self, board):
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if board[row][col] is None:
                return (row, col)
              
class Game:
    def __init__(self, player1, player2):
        self.board = self.make_empty_board()
        self.current_player = player1
        self.other_player = player2

    def make_empty_board(self):
        return [[None, None, None] for _ in range(3)]

    def get_winner(self):
        board = self.board
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            return board[0][2]
        return None

    def display_board(self):
        for row in self.board:
            print("|".join([cell if cell is not None else " " for cell in row]))
            print("-" * 5)

    def play_turn(self, player):
        row, col = player.move(self.board)
        self.board[row][col] = player.symbol

    def switch_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def play(self):
        winner = None
        while winner is None:
            self.display_board()
            self.play_turn(self.current_player)
            winner = self.get_winner()
            if winner is None:
                self.switch_player()
        self.display_board()
        print(f"{winner} has won!")

if __name__ == '__main__':
    mode = input("Choose game mode (1: single player, 2: two players): ")
    player1 = HumanPlayer("X")
    player2 = BotPlayer("O") if mode == "1" else HumanPlayer("O")
    game = Game(player1, player2)
    game.play()
