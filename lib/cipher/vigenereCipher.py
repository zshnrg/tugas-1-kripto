from lib.cipher.cipherInterface import Cipher

class vigenereCipher(Cipher):
    def __init__ (self) -> None:
        self.key = None

    def __init__ (self, key: str) -> None:
        self.key = key

    def setKey(self, key: str) -> None:
        # Set key dengan key yang diberikan
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        plaintext = self.clean(plaintext)

        # Enkripsi plaintext dengan key
        for i in range(len(plaintext)):
            if plaintext[i].isupper():
                ciphertext += chr(((ord(plaintext[i]) + ord(self.key[i % len(self.key)]) - 130) % 26) + 65)
            else:
                ciphertext += chr(((ord(plaintext[i]) + ord(self.key[i % len(self.key)]) - 194) % 26) + 97)
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        ciphertext = self.clean(ciphertext)

        # Dekripsi ciphertext dengan key
        for i in range(len(ciphertext)):
            if ciphertext[i].isupper():
                plaintext += chr(((ord(ciphertext[i]) - ord(self.key[i % len(self.key)]) + 26) % 26) + 65)
            else:
                plaintext += chr(((ord(ciphertext[i]) - ord(self.key[i % len(self.key)]) + 26) % 26) + 97)
        return plaintext
        