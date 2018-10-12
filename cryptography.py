"""
cryptography.py
Author: Nathan Subrahmanian
Credit: N/A

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations.find(char)
associations[index]
input("Enter e to encrypt, d to decrypt, of q to quit: ")
message = input("Message: ")
input("Key: ")
if message == "q":
    print("Goodbye!")