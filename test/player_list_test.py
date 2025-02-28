import unittest

from app.player import Player
from app.player_list import PlayerList, EmptyListException
from app.player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.player_list = PlayerList()

        self.player_1 = Player("1", "John")
        self.player_node_1 = PlayerNode(self.player_1)

        self.player_2 = Player("2", "Mary")
        self.player_node_2 = PlayerNode(self.player_2)

        self.player_3 = Player("3", "Bob")
        self.player_node_3 = PlayerNode(self.player_3)

    def test_add_at_head_when_player_list_empty(self):
        self.player_list.add_at_head(self.player_node_1)

        self.assertEqual(self.player_list.head, self.player_node_1)
        self.assertIsNone(self.player_list.tail)

    def test_add_at_head_when_player_list_has_one_node(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)

        self.assertEqual(self.player_list.head, self.player_node_2)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertEqual(self.player_node_2.next_node, self.player_node_1)
        self.assertEqual(self.player_node_1.prev_node, self.player_node_2)

    def test_add_at_head_when_player_list_has_more_than_one_node(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.add_at_head(self.player_node_3)

        self.assertEqual(self.player_list.head, self.player_node_3)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertIsNone(self.player_list.head.prev_node)
        self.assertIsNone(self.player_list.tail.next_node)
        self.assertEqual(self.player_node_2.next_node, self.player_node_1)
        self.assertEqual(self.player_node_2.prev_node, self.player_node_3)
        self.assertEqual(self.player_node_1.prev_node, self.player_node_2)
        self.assertEqual(self.player_node_3.next_node, self.player_node_2)

    def test_add_at_tail_when_player_list_empty(self):
        self.player_list.add_at_tail(self.player_node_1)

        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertIsNone(self.player_list.head)

    def test_add_at_tail_when_player_list_not_empty(self):
        self.player_list.add_at_tail(self.player_node_1)
        self.player_list.add_at_tail(self.player_node_2)

        self.assertEqual(self.player_list.tail, self.player_node_2)
        self.assertEqual(self.player_list.head, self.player_node_1)
        self.assertEqual(self.player_node_2.prev_node, self.player_node_1)
        self.assertEqual(self.player_node_1.next_node, self.player_node_2)

    def test_remove_at_head_when_player_list_empty(self):
        with self.assertRaises(EmptyListException) as ex:
            self.player_list.remove_at_head()

        self.assertEqual(type(ex.exception), EmptyListException)
        self.assertEqual(ex.exception.args[0], "Player list is empty.")

    def test_remove_at_head_when_player_list_has_one_player_node(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.remove_at_head()

        self.assertIsNone(self.player_list.head)
        self.assertIsNone(self.player_list.tail)

    def test_remove_at_head_when_player_list_has_two_player_nodes(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.remove_at_head()

        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertIsNone(self.player_list.tail.prev_node)
        self.assertIsNone(self.player_list.tail.next_node)
        self.assertIsNone(self.player_list.head)

    def test_remove_at_head_when_player_list_has_more_than_two_player_nodes(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.add_at_head(self.player_node_3)
        self.player_list.remove_at_head()

        self.assertEqual(self.player_list.head, self.player_node_2)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertIsNone(self.player_list.head.prev_node)

    def test_remove_at_tail_when_player_list_empty(self):
        with self.assertRaises(EmptyListException) as ex:
            self.player_list.remove_at_tail()

        self.assertEqual(type(ex.exception), EmptyListException)
        self.assertEqual(ex.exception.args[0], "Player list is empty.")

    def test_remove_at_tail_when_player_list_has_one_player_node(self):
        self.player_list.add_at_tail(self.player_node_1)
        self.player_list.remove_at_tail()

        self.assertIsNone(self.player_list.head)
        self.assertIsNone(self.player_list.tail)

    def test_remove_at_tail_when_player_list_has_two_player_nodes(self):
        self.player_list.add_at_tail(self.player_node_1)
        self.player_list.add_at_tail(self.player_node_2)
        self.player_list.remove_at_tail()

        self.assertEqual(self.player_list.head, self.player_node_1)
        self.assertIsNone(self.player_list.head.prev_node)
        self.assertIsNone(self.player_list.head.next_node)
        self.assertIsNone(self.player_list.tail)

    def test_remove_at_tail_when_player_list_has_more_than_two_player_nodes(self):
        self.player_list.add_at_tail(self.player_node_1)
        self.player_list.add_at_tail(self.player_node_2)
        self.player_list.add_at_tail(self.player_node_3)
        self.player_list.remove_at_tail()

        self.assertEqual(self.player_list.head, self.player_node_1)
        self.assertEqual(self.player_list.tail, self.player_node_2)
        self.assertIsNone(self.player_list.head.prev_node)
        self.assertIsNone(self.player_list.tail.next_node)

    def test_remove_node_by_key_when_node_is_the_head(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.add_at_head(self.player_node_3)
        self.player_list.remove_node_by_key("3")

        self.assertEqual(self.player_list.head, self.player_node_2)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertEqual(self.player_list.head.prev_node, None)

    def test_remove_node_by_key_when_node_is_the_tail(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.add_at_head(self.player_node_3)
        self.player_list.remove_node_by_key("1")

        self.assertEqual(self.player_list.head, self.player_node_3)
        self.assertEqual(self.player_list.tail, self.player_node_2)
        self.assertEqual(self.player_list.tail.next_node, None)

    def test_remove_node_by_key_when_node_is_in_the_middle(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.add_at_head(self.player_node_3)
        self.player_list.remove_node_by_key("2")

        self.assertEqual(self.player_list.head, self.player_node_3)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertEqual(self.player_list.head.next_node, self.player_node_1)
        self.assertEqual(self.player_list.tail.prev_node, self.player_node_3)

    def test_display_when_there_is_single_node_tail_and_forward_is_true(self):
        self.player_list.add_at_tail(self.player_node_1)
        player_nodes = self.player_list.display()

        self.assertEqual(len(player_nodes), 1)
        self.assertTrue(player_nodes[0].__contains__("1"))
        self.assertTrue(player_nodes[0].__contains__("John"))

    def test_display_when_there_is_single_node_head_and_forward_is_false(self):
        self.player_list.add_at_head(self.player_node_1)
        player_nodes = self.player_list.display(forward=False)

        self.assertEqual(len(player_nodes), 1)
        self.assertTrue(player_nodes[0].__contains__("1"))
        self.assertTrue(player_nodes[0].__contains__("John"))

    def test_display_when_there_are_more_than_single_node_and_forward_is_true(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.add_at_head(self.player_node_3)
        player_nodes = self.player_list.display()

        self.assertEqual(len(player_nodes), 3)
        self.assertTrue(player_nodes[0].__contains__("Player Name"))
        self.assertTrue(player_nodes[0].__contains__("3"))
        self.assertTrue(player_nodes[1].__contains__("2"))
        self.assertTrue(player_nodes[2].__contains__("John"))

    def test_display_when_there_are_more_than_single_node_and_forward_is_false(self):
        self.player_list.add_at_tail(self.player_node_1)
        self.player_list.add_at_tail(self.player_node_2)
        self.player_list.add_at_tail(self.player_node_3)
        player_nodes = self.player_list.display(forward=False)

        self.assertEqual(len(player_nodes), 3)
        self.assertTrue(player_nodes[0].__contains__("Unique Id"))
        self.assertTrue(player_nodes[0].__contains__("3"))
        self.assertTrue(player_nodes[1].__contains__("2"))
        self.assertTrue(player_nodes[2].__contains__("John"))







