import sign_up
import authentification
import hash
import dictionary_attack
import key_gen
import encryption
import decryption
import signature
import certificat_RSA
import os
import time
from art import *
import sys
from alive_progress import alive_bar






def main_menu():
    
    sys.stdout.write(text2art("PyCrypto\n\n"))

    print("\n\n1: Sign up\n")
    print("2: Log in\n")
    print("3: Exit\n")
    choice = input("Enter your choice: ")

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
            secondary_menu()
        case "3":
            exit()
        case _:
            os.system("cls")
            print("Please enter a valid choice!")
            time.sleep(2)
            os.system("cls")
            main_menu()

def secondary_menu():
    
    while True:
        sys.stdout.write(text2art("PyCrypto\n\n"))
        print("A- Give a word to hash (in invisible mode)\n")
        print("B- RSA Encryption\n")
        print("C- RSA Certificate\n")
        print("D- Logout\n")
        choice = input("Choose an option: ")
        match choice:
            case "A":
                os.system("cls")
                menu_A()
            case "B":
                os.system("cls")
                menu_B()
            case "C":
                os.system("cls")
                print("a")
            case "D":
                os.system("cls")
                main_menu()
            case _:
                os.system("cls")
                print("Please enter a valid choice !")
                time.sleep(2)
                os.system("cls")
                

def menu_A():
    word = input("Enter the word to hash: ")
    while True:  
        
        os.system("cls")
        sys.stdout.write(text2art("PyCrypto\n\n"))
        print("What do you want to do with the word?\n")
        print("a: Hash the word using SHA-256\n")
        print("b: Hash the word using bcrypt\n")
        print("c: Try a dictionary attack on the word\n")
        print("d: Return to main menu\n")
        choice = input("What is your next step: ")

        match choice:
            case "a":
                os.system("cls")
                hash.hash_sha256
                back_to_menu = input("\nPress any key to go back ")
            case "b":
                os.system("cls")
                hash.salt_bcrypt(word)
                back_to_menu = input("\nPress any key to go back ")
            case "c":
                os.system("cls")
                dictionary_attack.attack(word)
                back_to_menu = input("\nPress any key to go back ")
            case "d":
                secondary_menu()
            case _:
                print("Please enter a valid choice!")
                time.sleep(2)
                os.system("cls")

def menu_B():
    while True:
        os.system("cls")
        sys.stdout.write(text2art("PyCrypto\n\n"))
        print("a- Generate key pairs in a file\n")
        print("b- Encrypt a message of your choice using RSA\n")
        print("c- Decrypt the message (b)\n")
        print("d- Sign a message of your choice by RSA\n")
        print("e- Check message signature (d)\n")
        print("f- Return to main menu\n")
        choice = input("What is your next step: ")

        match choice:
            case "a":
                os.system("cls")
                key_gen.generate_key_pair()
                with alive_bar(100) as bar:
                    for i in range(100):
                        time.sleep(0.03)
                        bar() 
                print("\nRSA key pair generated successfully!")
                back_to_menu = input("\nPress any key to go back ")
            case "b":
                os.system("cls")
                message = input("Enter the message to encrypt: ")
                os.system("cls")
                encrypted_message = encryption.encrypt_message(message)
                print("Here is your encrypted message: ",encrypted_message)
                back_to_menu = input("\nPress any key to go back ")
            case "c":
                os.system("cls")
                """decrypted_message = decryption.decrypt_message(message)
                print("Here is your decrypted message: ",decrypted_message)
                back_to_menu = input("\nPress any key to go back ")"""
            case "d":
                os.system("cls")
                message_to_sign = input("Enter the message to sign: ")
                os.system("cls")
                signed_message = signature.sign_message(message_to_sign)
                print("Here is the signature of your message: ",signed_message)
                secondary_menu()
            case "e":
                signature.verify_signature(signed_message)
            case "f":
                os.system("cls")
                secondary_menu()
            case _:
                print("Please enter a valid choice!")
                time.sleep(2)
                os.system("cls")

'''
def menu_C():
    while True:
        sys.stdout.write(text2art("PyCrypto\n\n"))
        os.system("cls")
        print("C- RSA Certificate\n")
        print("\t a- Générer les paires de clés dans un fichier")
        print("\t b- Générer un certificat autosigné par RSA")
        print("\t c- Chiffrer un message de votre choix par ce certificat")
        print("\t d- Revenir au menu principal\n")
        choice = input("What is your next step: ")

        match choice:
            case "a":
                os.system("cls")
                back_to_menu = input("\nPress any key to go back ")
            case "b":
                os.system("cls")
                back_to_menu = input("\nPress any key to go back ")
            case "c":
                os.system("cls")
                back_to_menu = input("\nPress any key to go back ")
            case "d":
                secondary_menu()
            case _:
                print("Please enter a valid choice!")
                time.sleep(2)
                os.system("cls")
'''


while True:
    os.system("tput setaf 7; tput setaf 0; tput bold; tput cols 16 rows 52")
    os.system("stty size 120 60")
    os.system("cls")
    main_menu()

    