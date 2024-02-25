from abc import ABC, abstractmethod

class Cipher(ABC):
    @abstractmethod
    def encrypt(self, plaintext: str) -> str:
        # Enkripsi plaintext
        pass

    @abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        # Dekripsi ciphertext
        pass

    def clean(self, text: str) -> str:
        # Hapus karakter selain huruf
        return ''.join([i for i in text if i.isalpha()])
    