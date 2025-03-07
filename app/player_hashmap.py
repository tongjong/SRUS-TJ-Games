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

    def display(self) -> List[str]:
        all_players = []

        for index, player_list in enumerate(self._hash_table):
            # check if player list has any node
            if player_list.head or player_list.tail:
                info_list = player_list.display()
                players_of_each_play_list = f"{index}: "
                for info in info_list:
                    players_of_each_play_list += info + " | "
                all_players.append(players_of_each_play_list)

        return all_players

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

if __name__ == "__main__":
    hashmap = PlayerHashMap()
    hashmap["1"] = "john"
    hashmap["2"] = "joe"
    hashmap["3"] = "joe"
    hashmap["4"] = "joe"
    hashmap["5"] = "joe"
    hashmap["6"] = "joe"
    hashmap["10"] = "mary"
    hashmap["11"] = "mary"
    hashmap["12"] = "mary"
    hashmap["13"] = "mary"
    hashmap["14"] = "mary"
    hashmap["15"] = "mary"
    for each in hashmap.display():
        print(each)
    print(len(hashmap))