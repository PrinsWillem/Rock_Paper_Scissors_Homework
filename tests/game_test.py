from models.game import Game
from models.player import Player
import unittest

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player1 = Player("Willem", "Rock")
        self.player2 = Player("Callum", "Paper")
        self.player3 = Player("Anthony", "Scissors")
        self.player4 = Player("Lewis", "Rock")

    # @unittest.skip("delete this line to run the test")
    def test_tie_game(self):
        winner = self.game.play(self.player1, self.player4)
        self.assertEqual(None, winner)

    # @unittest.skip("delete this line to run the test")
    def test_rock_beats_scissors(self):
        winner = self.game.play(self.player1, self.player3)
        self.assertEqual(self.player1.name, winner)

    # @unittest.skip("delete this line to run the test")
    def test_scissors_loses_to_rock(self):
        winner = self.game.play(self.player3, self.player1)
        self.assertEqual(self.player1.name, winner)

    # @unittest.skip("delete this line to run the test")
    def test_scissors_beats_paper(self):
        winner = self.game.play(self.player3, self.player2)
        self.assertEqual(self.player3.name, winner)

    # @unittest.skip("delete this line to run the test")
    def test_paper_loses_to_scissors(self):
        winner = self.game.play(self.player2, self.player3)
        self.assertEqual(self.player3.name, winner)

    # @unittest.skip("delete this line to run the test")
    def test_paper_beats_rock(self):
        winner = self.game.play(self.player2, self.player1)
        self.assertEqual(self.player2.name, winner)

    # @unittest.skip("delete this line to run the test")
    def test_rock_loses_to_paper(self):
        winner = self.game.play(self.player1, self.player2)
        self.assertEqual(self.player2.name, winner)