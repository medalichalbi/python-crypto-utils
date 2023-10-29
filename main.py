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
import msvcrt as m



def menu():
    
    sys.stdout.write(text2art("\tPyCrypto\n\n"))

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
            main_menu()
        case "3":
            exit()
        case _:
            os.system("cls")
            print("Please enter a valid choice!")
            time.sleep(2)
            os.system("cls")
            main_menu()

def main_menu(): 
    while True:
        sys.stdout.write(text2art("PyCrypto\n\n"))
        print("A- Give a word to hash (in invisible mode)\n")
        print("\ta- Hash the word using SHA-256\n")
        print("\tb- Hash the word using bcrypt\n")
        print("\tc- Try a dictionary attack on the word\n")
        print("\td- Return to main menu\n")
        print("B- RSA Encryption\n")
        print("\ta- Generate key pairs in a file\n")
        print("\tb- Encrypt a message of your choice using RSA\n")
        print("\tc- Decrypt the message (b)\n")
        print("\td- Sign a message of your choice by RSA\n")
        print("\te- Check message signature (d)\n")
        print("\tf- Return to main menu\n")
        print("C- RSA Certificate\n")
        print("\t a- Generate key pairs in a file\n")
        print("\t b- Generate a self-signed certificate by RSA\n")
        print("\t c- Encrypt a message of your choice using this certificate\n")
        print("\t d- Return to main menu\n")
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
                menu_C()
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
        print("a- Hash the word using SHA-256\n")
        print("b- Hash the word using bcrypt\n")
        print("c- Try a dictionary attack on the word\n")
        print("d- Return to main menu\n")
        choice = input("Choose an option: ")

        match choice:
            case "a":
                os.system("cls")
                alivebar()
                hash.hash_sha256(word)
                wait()
            case "b":
                os.system("cls")
                alivebar()
                hash.salt_bcrypt(word)
                wait()
            case "c":
                os.system("cls")
                dictionary_attack.attack(word)
                wait()
            case "d":
                main_menu()
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
                alivebar()
                print("\nRSA key pair generated successfully!")
                wait()
            case "b":
                os.system("cls")
                message = input("Enter the message to encrypt: ")
                os.system("cls")
                alivebar()
                encrypted_message = encryption.encrypt_message(message)
                print("Here is your encrypted message: ",encrypted_message)
                wait()
            case "c":
                os.system("cls")
                decrypted_message = decryption.decrypt_message(message)
                os.system("cls")
                alivebar()
                print("Here is your decrypted message: ",decrypted_message)
                wait()
            case "d":
                os.system("cls")
                message_to_sign = input("Enter the message to sign: ")
                os.system("cls")
                alivebar()
                signed_message = signature.sign_message(message_to_sign)
                print("Here is the signature of your message: ",signed_message)
                wait()
            case "e":
                os.system("cls")
                alivebar()
                signature.verify_signature(message_to_sign,signed_message)
                wait()
            case "f":
                os.system("cls")
                main_menu()
            case _:
                print("Please enter a valid choice!")
                time.sleep(2)
                os.system("cls")

def menu_C():
    while True:
        os.system("cls")
        sys.stdout.write(text2art("PyCrypto\n\n"))
        print("a- Generate key pairs in a file\n")
        print("b- Generate a self-signed certificate by RSA\n")
        print("c- Encrypt a message of your choice using this certificate\n")
        print("d- Return to main menu\n")
        choice = input("What is your next step: ")

        match choice:
            case "a":
                os.system("cls")
                key_gen.generate_key_pair()
                alivebar()
                print("\nRSA key pair generated successfully!")
                wait()
            case "b":
                os.system("cls")
                certificat_RSA.generate_self_signed_certificate()
                os.system("cls")
                alivebar()
                
                print("Certificate generated successfully.")
                wait()
            case "c":
                os.system("cls")
                message = input("Enter the message to encrypt: ")
                os.system("cls")
                alivebar()
                
                encrypted_message = certificat_RSA.encrypt_message_with_certificate(message)
                print("Here is your encrypted message: ",encrypted_message)
                wait()
            case "d":
                os.system("cls")
                main_menu()
            case _:
                print("Please enter a valid choice!")
                time.sleep(2)
                os.system("cls")

def wait():
    print("\n\nPress any key to continue...")
    m.getch()

def alivebar():
    with alive_bar(100) as bar:
        for i in range(100):
            time.sleep(0.03)
            bar() 
    os.system("cls")

while True:
    os.system("cls")
    main_menu()

    