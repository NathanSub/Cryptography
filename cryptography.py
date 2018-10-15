"""
cryptography.py
Author: Nathan Subrahmanian
Credit: N/A

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = input("Enter e to encrypt, d to decrypt, of q to quit: ")
if command != "q":
    message = input("Message: ")
    key = input("Key: ")
    for i in range(len(message)):
        associations.find(message[i])
        associations.find(key[i])
else:
    print("Goodbye!")
