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
                encryptnumb = associations.find(message[i]) + associations.find(key[i])
                print(associations[encryptnumb], end = '')
            print()
        if command == "d":
            for i in range(len(message)):
                encryptnumb = associations.find(message[i]) - associations.find(key[i])
                if encryptnumb < 0:
                    encryptnumb += associationslength
                print(associations[encryptnumb], end = '')
            print()
    elif command != "q": 
        print("Did not understand command, try again.")

print("Goodbye!")