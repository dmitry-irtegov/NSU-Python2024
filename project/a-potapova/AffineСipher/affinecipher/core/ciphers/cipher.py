import abc


class Cipher(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def keygen(**args):
        pass

    @abc.abstractmethod
    def set_key(self, key):
        pass

    @staticmethod
    def encrypt(text, key=None) -> str:
        pass

    @staticmethod
    def decrypt(text: str, key=None) -> str:
        pass
