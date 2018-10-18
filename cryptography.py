"""
cryptography.py
Author: Nathan Subrahmanian
Credit: Partner

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = input("Enter e to encrypt, d to decrypt, of q to quit: ")

if command == "e" or command == "d":
    message = input("Message: ")
    key = input("Key: ")
    if len(message) > len(key):
        
    nums = []
    if command == "e":
        for i in range(len(message)):
            encryptnumb = (associations.find(message[i]) + associations.find(key[i]))
            nums.append(encryptnumb)
        for x in nums:
            print(associations[x], end = '')
    if command == "d":
        for i in range(len(message)):
            decryptnumb = (associations.find(message[i]) - associations.find(key[i]))
            nums.append(decryptnumb)
        for x in nums:
            print(associations[x], end = '')
    
        
elif command == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
