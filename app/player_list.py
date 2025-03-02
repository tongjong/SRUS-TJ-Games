from app.player_node import PlayerNode


class EmptyListException(Exception):
    pass

class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_at_head(self, player_node : PlayerNode) -> None:
        if self._is_empty():
            self._head = player_node
        else:
            player_node.next_node = self._head
            self._head.prev_node = player_node
            # when there is only one node in the list
            if not self._tail:
                self._tail = self._head
            self._head = player_node

    def add_at_tail(self, player_node : PlayerNode) -> None:
        if self._is_empty():
            self._tail = player_node
        else:
            self._tail.next_node = player_node
            player_node.prev_node = self._tail
            # when there is only one node in the list
            if not self._head:
                self._head = self._tail
            self._tail = player_node

    def remove_at_head(self) -> None :
        if self._is_empty():
            raise EmptyListException("Player list is empty.")
        # when there is only one node in the list
        elif not self._tail:
            self._head = None
        # when there are 2 nodes in the list
        elif self._head.next_node is self._tail:
            self._tail.prev_node = None
            self._tail.next_node = None
            # when removing at head, we do not modify the tail
            self._head = None
        else:
            new_head = self._head.next_node
            new_head.prev_node = None
            self._head = new_head

    def remove_at_tail(self) -> None :
        if self._is_empty():
            raise EmptyListException("Player list is empty.")
        # when there is only one node in the list
        elif not self._head:
            self._tail = None
        # when there are 2 nodes in the list
        elif self._tail.prev_node is self._head:
            self._head.next_node = None
            # when removing at tail, we do not modify the head
            self._tail = None
        else:
            new_tail = self._tail.prev_node
            new_tail.next_node = None
            self._tail = new_tail

    def remove_node_by_key(self, key: str) -> None:
        player_node = self._get_player_node_by_key(key)
        if self._head is player_node:
            self.remove_at_head()
        elif self._tail is player_node:
            self.remove_at_tail()
        else:
            node_before = player_node.prev_node
            node_after = player_node.next_node
            node_before.next_node = node_after
            node_after.prev_node = node_before

    def display(self, forward : bool= True) -> list[dict[str, str]]:
        player_nodes = []
        if forward:
            current_node = self._head
            while current_node:
                player_nodes.append({"uid": current_node.key, "name": current_node.player.name})
                current_node = current_node.next_node
        else:
            current_node = self._tail
            while current_node:
                player_nodes.append({"uid": current_node.key, "name": current_node.player.name})
                current_node = current_node.prev_node
        return player_nodes

    def _get_player_node_by_key(self, key) -> PlayerNode | None:
        current_node = self._head
        while current_node:
            if key == current_node.key:
                return current_node
            else:
                current_node = current_node.next_node
        return None

    def _is_empty(self) -> bool:
        return self._head is None and self._tail is None










