from models.player import Player
import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Willem", "Rock")
        self.player2 = Player("Callum", "Paper")
        self.player3 = Player("Anthony", "Scissors")

    # @unittest.skip("delete this line to run the test")
    def test_player_has_name(self):
        self.assertEqual("Willem", self.player1.name)

    # @unittest.skip("delete this line to run the test")
    def test_player_has_choice(self):
        self.assertEqual("Paper", self.player2.choice)