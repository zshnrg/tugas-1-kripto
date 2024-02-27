from lib.cipher.affineCipher import affineCipher
from lib.cipher.autoKeyVigenere import autoKeyVigenere
from lib.cipher.productCipher import productCipher
from lib.cipher.vigenereCipher import vigenereCipher
from lib.cipher.extendedVigenere import extendedVigenere
from lib.cipher.playfairCipher import playfairCipher

def encryptCipher(
    cipher: str,
    plainText: str,
    key: str,
    a: int = 0,
    b: int = 0,
) -> str:
    if (cipher == "affine"):
        print("Computing affine cipher")
        cipher = affineCipher(a, b)
        return cipher.encrypt(plainText)
    elif (cipher == "autokey"):
        print("Computing autokey cipher")
        cipher = autoKeyVigenere(key)
        return cipher.encrypt(plainText)
    elif (cipher == "product"):
        print("Computing product cipher")
        cipher = productCipher(shifter=a, key=b)
        return cipher.encrypt(plainText)
    elif (cipher == "vigenere"):
        print("Computing vigenere cipher")
        cipher = vigenereCipher(key)
        return cipher.encrypt(plainText)
    elif (cipher == "extendedVigenere"):
        print("Computing extended vigenere cipher")
        cipher = extendedVigenere(key)
        return cipher.encrypt(plainText)
    elif (cipher == "playfair"):
        print("Computing playfair cipher")
        cipher = playfairCipher(key)
        return cipher.encrypt(plainText)
    else:
        return "Invalid cipher"
    
def decryptCipher(
    cipher: str,
    cipherText: str,
    key: str,
    a: int = 0,
    b: int = 0,
) -> str:
    if (cipher == "affine"):
        print("Computing affine cipher")
        cipher = affineCipher(a, b)
        return cipher.decrypt(cipherText)
    elif (cipher == "autokey"):
        print("Computing autokey cipher")
        cipher = autoKeyVigenere(key)
        return cipher.decrypt(cipherText)
    elif (cipher == "product"):
        print("Computing product cipher")
        cipher = productCipher(shifter=a, key=b)
        return cipher.decrypt(cipherText)
    elif (cipher == "vigenere"):
        print("Computing vigenere cipher")
        cipher = vigenereCipher(key)
        return cipher.decrypt(cipherText)
    elif (cipher == "extendedVigenere"):
        print("Computing extended vigenere cipher")
        cipher = extendedVigenere(key)
        return cipher.decrypt(cipherText)
    elif (cipher == "playfair"):
        print("Computing playfair cipher")
        cipher = playfairCipher(key)
        return cipher.decrypt(cipherText)
    else:
        return "Invalid cipher"
    
def fileHandler(file):
    content = []
    while True:
        byte = file.read(1)
        if not byte:
            break
        character = chr(ord(byte))
        content.append(character)
    return ''.join(content)
               
