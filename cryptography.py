"""
cryptography.py
Author: Nathan Subrahmanian
Credit: https://www.youtube.com/watch?v=SZdQX4gbql0

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associationslength = len(associations)
command = "w"


while command != "q":
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if command == "e" or command == "d":
        message = input("Message: ")
        key = input("Key: ")
        if len(message) > len(key):
            key = len(message)*key
        nums=[]
        if command == "e":
            for i in range(len(message)): 
                thing = associations.find(message[i]) + associations.find(key[i])
                print(associations[thing], end = '')
            print()
        if command == "d":
            for i in range(len(message)):
                thing = associations.find(message[i]) - associations.find(key[i])
                if thing < 0:
                    thing += associationslength
                print(associations[thing], end = '')
            print()
    elif command != "q": 
        print("Did not understand command, try again.")

print("Goodbye!")