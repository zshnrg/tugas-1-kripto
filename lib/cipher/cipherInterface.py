from abc import ABC, abstractmethod

class Cipher(ABC):
    @abstractmethod
    def encrypt(self, plaintext: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        pass
