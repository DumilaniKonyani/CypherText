from cryptography.fernet import Fernet

userText = str(input("Enter text to encrypt and decrypt: "))

key = Fernet.generate_key()

fernet = Fernet(key)

secret = fernet.encrypt(userText.encode())

print("Original Text: ", userText)
print("Encrypted Text: ", secret)

decText = fernet.decrypt(secret).decode()

print("decrypted Text: ", decText)
