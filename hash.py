import hashlib
import bcrypt
import maskpass

def hash_sha256(word):
    hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
    print(word + " = " +hashed_word)
    

def salt_bcrypt(word):
    salt = bcrypt.gensalt()
    print(word +" = "+bcrypt.hashpw(word.encode(),salt).decode())    