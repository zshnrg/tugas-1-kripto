from lib.cipher.cipherInterface import Cipher

class playfairCipher(Cipher):
    def __init__(self) -> None:
        self.key = None
        self.matrix = None

    def __init__(self, key: str) -> None:
        self.key = key

    def setKey(self, key: str) -> None:
        # Set key dengan key yang diberikan
        self.key = key

    def generateMatrix(self) -> None:
        # Buat matriks 5x5 dengan key
        self.matrix = []
        key = self.key
        key = key.replace(" ", "")
        key = key.upper()
        key = key.replace("J", "I")
        key = "".join(dict.fromkeys(key))
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in key:
            alphabet = alphabet.replace(char, "")
        key += alphabet
        for i in range(0, 25, 5):
            self.matrix.append(list(key[i:i+5]))

    def findPosition(self, char: str) -> tuple:
        # Cari posisi karakter pada matriks
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return (i, j)
        return (-1, -1)
    
    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        plaintext = self.clean(plaintext)
        plaintext = plaintext.upper()
        plaintext = plaintext.replace("J", "I")
        self.generateMatrix()
        for i in range(0, len(plaintext), 2):
            char1 = plaintext[i]
            char2 = plaintext[i+1] if i+1 < len(plaintext) else "X"
            row1, col1 = self.findPosition(char1)
            row2, col2 = self.findPosition(char2)
            if row1 == row2:
                ciphertext += self.matrix[row1][(col1+1) % 5]
                ciphertext += self.matrix[row2][(col2+1) % 5]
            elif col1 == col2:
                ciphertext += self.matrix[(row1+1) % 5][col1]
                ciphertext += self.matrix[(row2+1) % 5][col2]
            else:
                ciphertext += self.matrix[row1][col2]
                ciphertext += self.matrix[row2][col1]
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        ciphertext = self.clean(ciphertext)
        ciphertext = ciphertext.upper()
        self.generateMatrix()
        for i in range(0, len(ciphertext), 2):
            char1 = ciphertext[i]
            char2 = ciphertext[i+1]
            row1, col1 = self.findPosition(char1)
            row2, col2 = self.findPosition(char2)
            if row1 == row2:
                plaintext += self.matrix[row1][(col1-1) % 5]
                plaintext += self.matrix[row2][(col2-1) % 5]
            elif col1 == col2:
                plaintext += self.matrix[(row1-1) % 5][col1]
                plaintext += self.matrix[(row2-1) % 5][col2]
            else:
                plaintext += self.matrix[row1][col2]
                plaintext += self.matrix[row2][col1]
        return plaintext
    