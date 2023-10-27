import sign_up
import authentification
import hash
import word_attack
import os
import time


def main_menu():
    print("1- Create an account\n")
    print("2- Authentification\n")
    print("3- Exit")

def menu_A():
    print("\t a- Hash the word by sha256")
    print("\t b- Hash the word by generating a salt (bcrypt)")
    print("\t c- Attack the inserted word using a dictionary")
    print("\t d- Return to main menu\n")

def menu_B():
    os.system("cls")
    print("\t a- Generate key pairs in a file")
    print("\t b- Encrypt a message of your choice using RSA")
    print("\t c- Decrypt the message (b)")
    print("\t d- Sign a message of your choice by RSA")
    print("\t e- Check message signature (d)")
    print("\t f- Return to main menu\n")

def menu_C():
    print("\t a- Générer les paires de clés dans un fichier")
    print("\t b- Générer un certificat autosigné par RSA")
    print("\t c- Chiffrer un message de votre choix par ce certificat")
    print("\t d- Revenir au menu principal\n")


while True:
    os.system("color 0a")
    main_menu()
    choice = input("Enter 1,2 or 3: ")
    match choice:
        case "1":
            os.system("cls")
            sign_up.email_validation()
            sign_up.password_validation()
            os.system("cls")
            print("Thanks for registering! You can now sign in")
            time.sleep(2)
            os.system("cls")
        case "2":
            os.system("cls")
            authentification.authentificate()
            os.system("cls")
            print("You are successfully logged in")
            time.sleep(2)
            os.system("cls")
            print("A- Enter a word to hash\n")
            menu_A()
            print("B- RSA Encryption\n")
            menu_B()
            print("C- RSA Certificate\n")
            menu_C()

            ch = input("Enter A,B or C: ")
            if ch == "A":
                os.system("cls")
                word = input("Enter the word to hash: ")
                os.system("cls")
                menu_A()
                x = input("Which one you want to try: ")
                if x == "a":
                    os.system("cls")
                    hash.hash_sha256(word)
                    back_to_A = input("\nEnter A to go back: ")
                    if back_to_A == "A":
                        menu_A()
                if x == "b":
                    os.system("cls")
                    hash.salt_bcrypt(word)
                    back_to_A = input("\nEnter A to go back: ")
                    if back_to_A == "A":
                        menu_A()
                if x == "c":
                    os.system("cls")
                    print("Please wait ...")
                    time.sleep(5)
                    os.system("cls")
                    word_attack.attack(word)
                    back_to_A = input("\nEnter A to go back: ")
                    if back_to_A == "A":
                        menu_A()

                if x == "d":
                    main_menu()

            """elif ch == "B":
                
                y = input("Enter your choice: ")
                if y == "a":

                if y == "b":

                if y == "c":

                if y == "d":

                if y == "e":

                if y == "f":
                    main_menu()
                else:
                    print("Invalid choice ! Try again")
                    time.sleep(2)
                    os.system("cls")"""
            
"""            elif ch == "C":
                os.system("cls")        
        case "3":
            exit()
        case default:
            print("Please enter a valid choice !")"""





