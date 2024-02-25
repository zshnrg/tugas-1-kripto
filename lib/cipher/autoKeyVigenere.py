from cipherInterface import Cipher

class autoKeyVigenere(Cipher):
    def __init__(self) -> None:
        self.key = None

    def __init__(self, key: str) -> None:
        self.key = key

    def setKey(self, key: str) -> None:
        # Set key dengan key yang diberikan
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        # Enkripsi plaintext dengan key yang sudah ditentukan
        ciphertext = ""
        plaintext = self.clean(plaintext)
        autoKey = self.key
        for i in range(len(plaintext)):
            if (i > len(self.key) - 1):
                autoKey += plaintext[i - len(self.key)]
            if plaintext[i].isupper():
                ciphertext += chr(((ord(plaintext[i]) - 65 + ord(autoKey[i]) - 65) % 26) + 65)
            else:
                ciphertext += chr(((ord(plaintext[i]) - 97 + ord(autoKey[i]) - 97) % 26) + 97)
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        ciphertext = self.clean(ciphertext)
        autoKey = self.key
        for i in range(len(ciphertext)):
            if (i > len(self.key) - 1):
                autoKey += plaintext[i - len(self.key)]
            if ciphertext[i].isupper():
                plaintext += chr(((ord(ciphertext[i]) - 65 - (ord(autoKey[i]) - 65) + 26) % 26) + 65)
            else:
                plaintext += chr(((ord(ciphertext[i]) - 97 - (ord(autoKey[i]) - 97) + 26) % 26) + 97)
        return plaintext