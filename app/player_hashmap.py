from app.player import Player
from app.player_list import PlayerList
import random

from app.player_node import PlayerNode


class PlayerHashMap:
    def __init__(self, size:int =10):
        self._size = size
        self.hash_table: list[PlayerList] = [PlayerList() for _ in range(self._size)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self._size
        else:
            return Player.hash(key) % self._size

    def __getitem__(self, uid: str) -> Player | None:
        index = self.get_index(uid)
        player_node = self.hash_table[index].get_player_node_by_key(uid)
        return player_node.player if player_node else None

    def __setitem__(self, uid: str, name: str) -> None:
        player = self.__getitem__(uid)
        # update name value if the player is in the list
        if player:
            player.name = name
        # If it isn't, create a player node and add the player node to the player list
        else:
            index = self.get_index(uid)
            player = Player(uid, name)
            player_node = PlayerNode(player)
            self.hash_table[index].add_at_tail(player_node)

    def __delitem__(self, key: str) -> None:
        player = self.__getitem__(key)
        if not player:
            raise KeyError("Player not found")
        else:
            index = self.get_index(key)
            self.hash_table[index].remove_node_by_key(key)

    def __len__(self) -> int:
        return sum(len(player_list) for player_list in self.hash_table)
