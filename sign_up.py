import re
import string
import maskpass
import tkinter as tk
from tkinter import messagebox


def email_availibility(email):
  f = open("user-credentials.txt", "r")
  for line in f:
    if email == line.strip().split(":")[0]:
      print("Email address is already in use, Try again")
      return False
  return True
  
def email_validation():
  while True:
    email = input("Enter your email address: ")
    if email_availibility(email):
      regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
      if re.fullmatch(regex, email):
        f = open("user-credentials.txt", "a")
        f.write(email)
        return email
      else:
        print("Please enter a valid email address")

def password_validation():
  while True:
    pwd = maskpass.askpass()
    result = True
    special_characters = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    if len(pwd)>8 or len(pwd)<8:
      print("Password must contain only 8 caracters")
      result = False
    if not any (char.isupper() for char in pwd) : 
      print("Password must contain at least an uppercase letter")
      result = False
    if not any (char.islower() for char in pwd) : 
      print("Password must contain at least an lowercase letter")
      result = False
    if not any(char.isdigit() for char in pwd):
      #root = tk.Tk()
      #root.title("WARNING")
      #messagebox.showinfo(title="WARNING", message="Password must contain at least a number.")
      #root.mainloop()
      print("Password must contain at least a number")
      result = False   
    if not any(char in special_characters for char in pwd):
      print("Password should have at least one of the symbols: "+special_characters )
      result = False
    if result:
      print(pwd)
      f = open("user-credentials.txt", "a")
      f.write(":"+pwd+"\n")
      f.close()
      return pwd
    

  










