from lib.cipher.cipherInterface import Cipher

class affineCipher(Cipher):
    def __init__(self) -> None:
        self.m = None
        self.b = None
        self.n = 26
        self.m_inverse = None
    
    def __init__(self, m_key: int, b_key: int, n_key=26) -> None:
        # Error handling untuk m_key, b_key, dan n_key apabila bukan integer
        if not isinstance(m_key, int) or not isinstance(b_key, int):
            raise ValueError("m_key and b_key must be integers")

        # Error handling untuk m_key tidak relatif prima dengan n_key = 26
        if (m_key % 2 == 0) or (m_key % 13 == 0):
            raise ValueError("m_key and n_key must be relatively prime")

        m_inverse = 1
        while True:
            if (m_key * m_inverse) % n_key == 1:
                break
            m_inverse += 1

        self.m = m_key
        self.m_inverse = m_inverse
        self.b = b_key
        self.n = n_key

    def setKey(self, m_key: int, b_key: int, n_key=26) -> None:
        # Error handling untuk m_key, b_key, dan n_key apabila bukan integer
        if not isinstance(m_key, int) or not isinstance(b_key, int) or not isinstance(n_key, int):
            raise ValueError("m_key, b_key, and n_key must be integers")

        # Error handling untuk m_key tidak relatif prima dengan n_key = 26
        if (m_key % 2 == 0) or (m_key % 13 == 0):
            raise ValueError("m_key and n_key must be relatively prime")

        m_inverse = 1
        while True:
            if (m_key * m_inverse) % n_key == 1:
                break
            m_inverse += 1

        self.m = m_key
        self.m_inverse = m_inverse
        self.b = b_key
        self.n = n_key

    def setKey(self, m_key: int) -> None:
        # Error handling untuk m_key apabila bukan integer
        if not isinstance(m_key, int):
            raise ValueError("m_key must be an integer")

        # Mencari nilai b_key yang relatif prima dengan m_key
        m_inverse = 1
        while True:
            if (m_key * m_inverse) % self.n == 1:
                break
            m_inverse += 1
        
        self.m = m_key
        self.m_inverse = m_inverse
    
    def encrypt(self, plaintext: str) -> str:
        cipherText = ""
        plaintext = self.clean(plaintext)
        for char in plaintext:
            if char.isupper():
                cipherText += chr(((self.m * (ord(char) - 65) + self.b) % self.n) + 65)
            else:
                cipherText += chr(((self.m * (ord(char) - 97) + self.b) % self.n) + 97)
        return cipherText

    def decrypt(self, ciphertext: str) -> str:
        plainText = ""
        ciphertext = self.clean(ciphertext)
        for char in ciphertext:
            if char.isupper():
                plainText += chr(((self.m_inverse * (ord(char) - 65 - self.b)) % self.n) + 65)
            else:
                plainText += chr(((self.m_inverse * (ord(char) - 97 - self.b)) % self.n) + 97)
        return plainText