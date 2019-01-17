#!python3
# Insecure password locker

from password_generator import passwordGenerator
import pyperclip
import time

file = open("locker.txt")
locker = {}
for line in file:
    (key,value) = line.split()
    locker[key] = value
file.close()

def write():
    file = open("locker.txt", "w")
    for (key, value) in locker.items():
        file.write(key + " " + value)
    file.close()

while(True):
    n = int(input("Enter your option\n1.Genearte the password\n2.Store the password\n3.Show All account\n"
                  "4.Retrive the password\n5.Update Password\n6.Delete account from locker\n7.Exit\n"))
    if(n==1):
        len = int(input("Enter Lenght of password\n"))
        passwordGenerator(len)
    elif(n==2):
        account = input("Enter Account\n")
        if account in locker:
            print("Account Already in Locker !!\n")
        else:
            password = input("Enter Password\n")
            locker[account] = password
            print("Locker update!\n")
        write()
    elif(n==3):
        if locker == {}:
            print("Locker is Empty !!\n")
        else:
            print("List of all account")
            print(list(locker.keys()))
    elif(n==4):
        account = input("Enter Account\n")
        if account in locker:
            print("Passsword '{}' copied for account '{}' \n".format(locker.get(account),account))
            pyperclip.copy(locker.get(account))
        else:
            print("Account not in locker !!\n")
    elif(n==5):
        account = input("Enter Account\n")
        if account in locker:
            password = input("Enter Password to Update\n")
            locker[account] = password
            print("Password Updated\n")
        else:
            print("Account not in locker !!\n")
        write()
    elif(n==6):
        account = input("Enter Account\n")
        if account in locker:
            confirm = input("Are you sure ? Enter your option y or n ?\n")
            if(confirm=='y' or confirm=='Y'):
                del locker[account]
                print("Deleted !!\n")
            else:
                print("Not Deleted")
        else:
            print("Account not in locker !!\n")
        write()
    elif(n==7):
        print("Terminated !!\n")
        break;
    else:
        print("Enter the correct option\n");
    time.sleep(1)

#TODO: Secure the locker with master password (Verify with laptop password)
#TODO: Encrypt the password
#TODO : Convert if-elif to switch case