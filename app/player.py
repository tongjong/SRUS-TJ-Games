class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'Unique Id: {self._uid}, Player Name: {self._name}'
    
