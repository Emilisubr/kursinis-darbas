from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row = int(input(f"{self.name}, pick a row (0-2): "))
                col = int(input(f"{self.name}, pick a column (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

class ComputerPlayer(Player):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        import random
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        return random.choice(empty_cells) if empty_cells else None

class TicTacToe:
    def __init__(self, player_factory):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.players = [player_factory.create_player("Player 1", 'X'),
                        player_factory.create_player("Player 2", 'O')]

    def start_game(self):
        print("Welcome to Tic Tac Toe!")
        print("Rules: Players take turns marking the spaces in a 3x3 grid.")
        print("The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins.")

        self.current_player = self.players[0]
        self.print_board()

        while True:
            move = self.current_player.make_move(self.board)
            if move:
                row, col = move
                self.board[row][col] = self.current_player.symbol
                if self.check_winner():
                    self.print_board()
                    print(f"{self.current_player.name} wins!")
                    break
                if self.check_tie():
                    self.print_board()
                    print("The game ended in a tie.")
                    break
                self.switch_players()
                self.print_board()
            else:
                print("The board is full. Game over.")
                break

    def print_board(self):
        print("\n  0 1 2")
        for i, row in enumerate(self.board):
            print(i, ' '.join(row))

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_tie(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_players(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self, name, symbol):
        pass

class HumanPlayerFactory(PlayerFactory):
    def create_player(self, name, symbol):
        return HumanPlayer(name, symbol)

class ComputerPlayerFactory(PlayerFactory):
    def create_player(self, name, symbol):
        return ComputerPlayer(name, symbol)

def main():
    while True:
        choice = input("Select an opponent: 1 for Human, 2 for Computer: ")
        if choice == '1':
            player_factory = HumanPlayerFactory()
            break
        elif choice == '2':
            player_factory = ComputerPlayerFactory()
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    game = TicTacToe(player_factory)
    game.start_game()

if __name__ == "__main__":
    main()