from cryptography.fernet import Fernet

# function to generate a user password
password = int(input("Enter your number: "))

code = Fernet.generate_key()

fernet = Fernet(code)

encryptedMessage = fernet.encrypt(password.encode())

print("Original Code: ", password)
print("Encrypted Code: ", encryptedMessage)


decryptMessage = fernet.decrypt(password).decode()