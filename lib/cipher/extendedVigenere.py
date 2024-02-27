from lib.cipher.cipherInterface import Cipher   

class extendedVigenere(Cipher):
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        ciphertext = ""
        key_length = len(self.key)
        for i in range(len(plaintext)):
            key_index = i % key_length
            key_char = ord(self.key[key_index])
            plaintext_char = ord(plaintext[i])
            encrypted_char = (plaintext_char + key_char) % 256
            ciphertext += chr(encrypted_char)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        key_length = len(self.key)
        for i in range(len(ciphertext)):
            key_index = i % key_length
            key_char = ord(self.key[key_index])
            ciphertext_char = ord(ciphertext[i])
            decrypted_char = (ciphertext_char - key_char) % 256
            plaintext += chr(decrypted_char)
        return plaintext
    