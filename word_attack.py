def attack(word):
    f = open("pwd_dictionary.txt","r", encoding="utf8")
    if any (line.strip() == word for line in f):

        print("Word found")
        return True
    else : 
        print("Word not found")
        return False
