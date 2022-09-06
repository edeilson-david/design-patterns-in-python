import string
import random


class PasswordGenerator:

    @staticmethod
    def generate() -> str:
        prefix = PasswordGenerator._get(string.ascii_uppercase, 1)
        suffix = PasswordGenerator._get(string.digits, 4)
        return prefix + suffix

    @staticmethod
    def _get(chars: str, size: int = 1) -> str:
        return ''.join(random.choices(chars, k=size))
