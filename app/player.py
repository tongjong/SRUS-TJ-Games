import random


class Player:
    random.seed(20)
    pearson_table = list(range(256))
    random.shuffle(pearson_table)

    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def hash(cls, key: str) -> int:
        byte_values = bytes(key, encoding='utf8')
        _hash = 0
        for each_byte in byte_values:
            _hash = cls.pearson_table[_hash ^ each_byte]
        return _hash

    def __hash__(self) -> int:
        return self._pearson_hash(self._uid)

    def __str__(self):
        return f'Unique Id: {self.uid}, Player Name: {self.name}'

    def _pearson_hash(self, key) -> int:
        byte_values = bytes(key, encoding='utf8')
        _hash = 0
        for each_byte in byte_values:
            _hash = self.pearson_table[_hash ^ each_byte]
        return _hash
