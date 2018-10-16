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
    if command == "e":
        for i in range(len(message)):
            messagenumb = associations.find(message[i])
            keynumb = associations.find(key[i])
            encryptnumb = (messagenumb+keynumb)
        
elif command == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
