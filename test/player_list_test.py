import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.player_list = PlayerList()

        self.player_1 = Player("1", "John")
        self.player_node_1 = PlayerNode(self.player_1)

        self.player_2 = Player("2", "Mary")
        self.player_node_2 = PlayerNode(self.player_2)

    def test_add_at_head_when_player_list_empty(self):
        self.player_list.add_at_head(self.player_node_1)

        self.assertEqual(self.player_list.head, self.player_node_1)

    def test_add_at_head_when_player_list_not_empty(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)

        self.assertEqual(self.player_list.head, self.player_node_2)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertEqual(self.player_node_2.next_node, self.player_node_1)
        self.assertEqual(self.player_node_1.prev_node, self.player_node_2)


