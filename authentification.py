import sign_up
import maskpass
import os
from time import sleep

def authentificate():
    while True:
        email = input("Enter your email address: ")
        pwd = maskpass.askpass("Enter your password: ")
        f = open("user-credentials.txt", "r")
        if any (line.strip().split(":")[0] == email and line.strip().split(":")[1] == pwd for line in f):
            email_part = email.split("@")
            username = email_part[0]
            os.system("cls")
            print(f"Hello {username}! Welcome to our application!")
            sleep(2)
            return True
        print("Invalid email or password. Please enter 1 to try again, or enter 2 to create a new account")
        new_acc = input(": ")
        if new_acc == "1":
            os.system("cls")
            continue
        if new_acc == "2":
            os.system("cls")
            sign_up.email_validation()
            sign_up.password_validation()
            return True


