import random

from cipherInterface import Cipher

class oneTimePad(Cipher):
    def __init__(self) -> None:
        self.key = self.generateKey()

    def generateKey(self, length=100) -> None:
        # Generate random key dengan panjang 100 karakter
        self.key = ""
        for i in range(length):
            self.key += chr(random.randint(0, 255))

    def setKey(self, key: str) -> None:
        # Set key dengan key yang diberikan
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        # Enkripsi plaintext dengan key yang sudah ditentukan
        ciphertext = ""
        for i in range(len(plaintext)):
            # Tambahkan ord dari karakter plaintext dengan ord dari karakter key pada posisi i % len(key)
            # Key berulang apabila panjangnya kurang dari panjang plaintext
            ciphertext += chr(ord(plaintext[i]) + ord(self.key[i % len(self.key)]))
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        for i in range(len(ciphertext)):
            # Kurangkan ord dari karakter ciphertext dengan ord dari karakter key pada posisi i % len(key)
            # Key berulang apabila panjangnya kurang dari panjang ciphertext
            plaintext += chr(ord(ciphertext[i]) - ord(self.key[i % len(self.key)]))
        return plaintext