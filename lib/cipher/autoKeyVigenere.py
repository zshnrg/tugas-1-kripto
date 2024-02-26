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
        autoKey = self.key
        for i in range(len(plaintext)):
            if (i > len(self.key) - 1):
                autoKey += plaintext[i - len(self.key)]
            # Enkripsi dengan 256 karakter ASCII
            ciphertext += chr(((ord(plaintext[i]) + ord(autoKey[i])) % 256))
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        autoKey = self.key
        for i in range(len(ciphertext)):
            if (i > len(self.key) - 1):
                autoKey += plaintext[i - len(self.key)]
            # Dekripsi dengan 256 karakter ASCII
            plaintext += chr(((ord(ciphertext[i]) - ord(autoKey[i]) + 256) % 256))
        return plaintext