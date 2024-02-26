from lib.cipher.affineCipher import affineCipher
from lib.cipher.autoKeyVigenere import autoKeyVigenere
from lib.cipher.productCipher import productCipher

def encryptCipher(
    cipher: str,
    plaintext: str,
    key: str,
    m: int = 0,
    b: int = 0,
) -> str:
    if (cipher == "affine"):
        print("Computing affine cipher")
        cipher = affineCipher(m, b)
        return cipher.encrypt(plaintext)
    elif (cipher == "autokey"):
        print("Computing autokey cipher")
        cipher = autoKeyVigenere(key)
        return cipher.encrypt(plaintext)
    elif (cipher == "product"):
        print("Computing product cipher")
        cipher = productCipher(int(key))
        return cipher.encrypt(plaintext)
    else:
        return "Invalid cipher"
    
def decryptCipher(
    cipher: str,
    ciphertext: str,
    key: str,
    m: int = 0,
    b: int = 0,
) -> str:
    if (cipher == "affine"):
        print("Computing affine cipher")
        cipher = affineCipher(int(m), int(b))
        return cipher.decrypt(ciphertext)
    elif (cipher == "autokey"):
        print("Computing autokey cipher")
        cipher = autoKeyVigenere(key)
        return cipher.decrypt(ciphertext)
    elif (cipher == "product"):
        print("Computing product cipher")
        cipher = productCipher(int(key))
        return cipher.decrypt(ciphertext)
    else:
        return "Invalid cipher"
    
def fileHandler(file):
    # Transform the file into a string of bytes including the header
    return file.read()
