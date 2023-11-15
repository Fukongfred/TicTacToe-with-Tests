from tictactoe import HumanPlayer, BotPlayer, Game

def main():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Choose game mode (1: single player, 2: two players): ")
    player1 = HumanPlayer("X")
    player2 = BotPlayer("O") if mode == "1" else HumanPlayer("O")
    game = Game(player1, player2)
    game.play()

if __name__ == '__main__':
    main()
