from app.player import Player


class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next_node = None
        self._prev_node = None

    @property
    def player(self):
        return self._player

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, player : Player):
        self._next_node = player

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, player : Player):
        self._prev_node = player

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"player: {self._player},next_node: {self._next_node},prev_node: {self._prev_node}"
