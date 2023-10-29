from hashlib import sha256
from datetime import datetime
import hash

def attack(word):
    hashed_word = hash.hash_sha256(word)
    t = datetime.now()
    n = 0
    f = open("dictionary.txt", "r", encoding="utf8")
    for line in f:
        line = line.strip()
        n+=1
        if sha256(line.encode()).hexdigest() == hashed_word:
            print("\nWord found!\n")
            print(n, "word tested in", (datetime.now() - t).total_seconds(), "seconds")
            f.close()
            return True
    print("Word not found! No hash matches your hash")