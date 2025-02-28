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

    def add_at_head(self, player_node) -> None:
        if self._is_empty():
            self._head = player_node
        else:
            player_node.next_node = self._head
            self._head.prev_node = player_node
            self._tail = self._head
            self._head = player_node

    def _is_empty(self) -> bool:
        return self._head is None and self._tail is None








