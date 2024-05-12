import unittest
from unittest.mock import patch
from kryziukai_nuliukai import TicTacToe, HumanPlayerFactory, ComputerPlayerFactory

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.human_factory = HumanPlayerFactory()
        self.computer_factory = ComputerPlayerFactory()


    def test_computer_vs_computer(self):
        game = TicTacToe(self.computer_factory)
        game.start_game()
        self.assertTrue(game.check_winner())

    def test_human_vs_human(self):
     with patch('builtins.input', side_effect=['0', '0', '1', '0', '0', '1', '1', '1', '0', '2']):
        game = TicTacToe(self.human_factory)
        game.start_game()
        self.assertTrue(game.check_winner())


    def test_human_vs_human(self):
     with patch('builtins.input', side_effect=['0', '0', '1', '0', '1', '1', '1', '1']):
        game = TicTacToe(self.human_factory)
        game.start_game()
        self.assertTrue(game.check_winner())


    

if __name__ == '__main__':
    unittest.main()
