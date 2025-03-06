from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode
from typing import Tuple, List


class PlayerHashMap:
    def __init__(self, size:int =10):
        self._size = size
        self.hash_table: List[PlayerList] = [PlayerList() for _ in range(self._size)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self._size
        else:
            return Player.hash(key) % self._size

    def display(self) -> List[str]:
        all_players = []

        for index, player_list in enumerate(self.hash_table):
            # check if player list has any node
            if player_list.head or player_list.tail:
                player_list_details = player_list.display()
                each_player_list= f"{index + 1}: "
                for player_detail in player_list_details:
                    each_player_list += player_detail + " | "

                all_players.append(each_player_list)

        return all_players

    def __getitem__(self, uid: str) -> Tuple[int, Player] | None:
        index = self.get_index(uid)
        player_node = self.hash_table[index].get_player_node_by_key(uid)
        return (index, player_node.player) if player_node else None

    def __setitem__(self, uid: str, name: str) -> None:
        player_tuple = self[uid]
        # update name value if the player is in the list
        if player_tuple:
            _, player = player_tuple
            player.name = name
        # If it isn't, create a player node and add the player node to the player list
        else:
            index = self.get_index(uid)
            player = Player(uid, name)
            player_node = PlayerNode(player)
            self.hash_table[index].add_at_tail(player_node)

    def __delitem__(self, key: str) -> None:
        index, player = self[key]
        if not player:
            raise KeyError("Player not found")
        else:
            self.hash_table[index].remove_node_by_key(key)

    def __len__(self) -> int:
        return sum(len(player_list) for player_list in self.hash_table)


if __name__ == "__main__":
    hashmap = PlayerHashMap()
    hashmap["1"] = "john"
    hashmap["2"] = "jane"
    print(hashmap.display())
    print(hashmap["2"])
    print(hashmap["1"])