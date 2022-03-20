import random
import string
import secrets
import os
import getpass


def clean():
    if(os.name == "posix"):
        os.system("clear")
    elif(os.name == "nt"):
        os.system("cls")

if(os.name == "posix"):
    op = "Linux"
elif(os.name == "nt"):
    op = "Windows"

def menu():
    clean()
    print("     Password menu")
    print("     User: " + getpass.getuser() + "     OS: " + op)
    print()
    print("[1] Weak password    Weak generation")
    print("[2] Strong password  Weak generation")
    print("[3] Weak password    Strong generation")
    print("[4] Strong password  Stron generation")
    print("[0] Exit the program")
    
weak = string.ascii_lowercase + string.ascii_uppercase + string.digits
strong = string.ascii_lowercase + string.ascii_uppercase + string.digits  + string.punctuation
    
def option1():
    lenght = int(input("Enter the lenght: "))
    passw = random.sample(weak,lenght)
    cleanPassw = "".join(passw) 
    print("Your password: " + cleanPassw)
   
def option2():
    lenght = int(input("Enter the lenght: "))
    passw = random.sample(strong,lenght)
    cleanPassw = "".join(passw) 
    print("Your password: " + cleanPassw)
    
def option3():
    lenght = int(input("Enter the lenght: "))
    cleanPassw = "".join(secrets.choice(weak) for i in range(lenght))
    print("Your password: " + cleanPassw)
    
def option4():
    lenght = int(input("Enter the lenght: "))
    cleanPassw = "".join(secrets.choice(strong) for i in range(lenght))
    print("Your password: " + cleanPassw)
        
menu()
option = int(input("Enter your choice: "))

while option != 0:
    if option == 1:
        clean()
        option1()
    elif option == 2:
        clean()
        option2()
    elif option == 3:
        clean()
        option3()
    elif option == 4:
        clean()
        option4()
    else:
        print("Invalid option")
        
    print("Enter to continue")
    input()
    print()
    menu()
    option = int(input("Enter your choice: "))

print("Chiao")