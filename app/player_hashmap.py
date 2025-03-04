from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode
from typing import Tuple, List


class PlayerHashMap:
    def __init__(self, size:int =10):
        self._size = size
        self._hash_table: List[PlayerList] = [PlayerList() for _ in range(self._size)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self._size
        else:
            return Player.hash(key) % self._size

    def __getitem__(self, uid: str) -> Tuple[int, Player] | None:
        index = self.get_index(uid)
        player_node = self._hash_table[index].get_player_node_by_key(uid)
        return (index, player_node.player) if player_node else None

    def __setitem__(self, uid: str, name: str) -> None:
        player_list = self._hash_table[self.get_index(uid)]
        player_node = player_list.get_player_node_by_key(uid)
        # update name value if the player is in the list
        if player_node:
            player_node.player.name = name
        # If it isn't, create a player node and add the player node to the player list
        else:
            new_player_node = PlayerNode(Player(uid, name))
            player_list.add_at_tail(new_player_node)

    def __delitem__(self, key: str) -> None:
        player_tuple = self[key]
        if not player_tuple:
            raise KeyError("Player not found")
        else:
            index = self.get_index(key)
            self._hash_table[index].remove_node_by_key(key)

    def __len__(self) -> int:
        return sum(len(player_list) for player_list in self._hash_table)

