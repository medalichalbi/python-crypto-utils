import hashlib
import bcrypt
import maskpass

def hash_sha256(word):
    hashed_word = hashlib.sha256(word.encode()).hexdigest()
    print("The hash of the word " +word+ " using the SHA-256 algorithm is: "+hashed_word)
    return hashed_word

def salt_bcrypt(word):
    salt_word = bcrypt.gensalt()
    print("The hash of the word " +word+" by generating a salt (bcrypt) is: "+bcrypt.hashpw(word.encode(),salt_word).decode())    
    return salt_word
