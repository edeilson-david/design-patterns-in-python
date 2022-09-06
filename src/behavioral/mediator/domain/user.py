
class User:

    def __init__(self, username: str):
        self._username = username

    @property
    def username(self) -> str:
        return self._username
