"""
cryptography.py
Author: Nathan Subrahmanian
Credit: https://www.youtube.com/watch?v=SZdQX4gbql0

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = "z"

while command != "q":
    command = input("Enter e to encrypt, d to decrypt, of q to quit: ")
    if command == "e" or command == "d":
        message = input("Message: ")
        key = input("Key: ")
        keyword = key
        if len(message) > len(key):
            keyword = key*len(message)
        else:
            keyword = keyword
        nums = []
        if command == "e":
            for i in range(len(message)):
                encryptnumb = (associations.find(message[i]) + associations.find(keyword[i]))
                nums.append(encryptnumb)
            for x in nums:
                print(associations[x], end = '')
            print()
        if command == "d":
            for i in range(len(message)):
                decryptnumb = (associations.find(message[i]) - associations.find(keyword[i]))
                nums.append(decryptnumb)
            for x in nums:
                print(associations[x], end = '')
    elif command != "q":
        print("Did not understand command, try again.")
    
print("Goodbye!")
    
## USE LOOP ##
