from cipherInterface import Cipher
import math

class productCipher(Cipher):
    def __init__(self, key: int) -> None:
        self.key = key

    def setKey(self, key: int) -> None:
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        plaintext = self.clean(plaintext)
        row = math.ceil(len(plaintext) / self.key)
        
        # Subtitusi karakter plaintext dengan karakter pada posisi key
        for i in range(self.key):
            for j in range(row):
                if i + j * self.key < len(plaintext):
                    if plaintext[i + j * self.key].isupper():
                        ciphertext += chr(((ord(plaintext[i + j * self.key]) - 65 + row) % 26) + 65)
                    else:
                        ciphertext += chr(((ord(plaintext[i + j * self.key]) - 97 + row) % 26) + 97)
                else:
                    ciphertext += "z"
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        ciphertext = self.clean(ciphertext)
        col = math.ceil(len(ciphertext) / self.key)

        # Subtitusi karakter ciphertext dengan karakter pada posisi key
        for i in range(col):
            for j in range(self.key):
                if i + j * col < len(ciphertext):
                    if ciphertext[i + j * col].isupper():
                        plaintext += chr(((ord(ciphertext[i + j * col]) - 65 - col + 26) % 26) + 65)
                    else:
                        plaintext += chr(((ord(ciphertext[i + j * col]) - 97 - col + 26) % 26) + 97)

        return plaintext