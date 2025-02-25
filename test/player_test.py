import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def test_uid_method_return_uid_value(self):
        player_1 = Player("1", "John")
        self.assertEqual(player_1.uid, "1")

    def test_name_method_return_name_value(self):
        player_1 = Player("1", "John")
        self.assertEqual(player_1.name, "John")