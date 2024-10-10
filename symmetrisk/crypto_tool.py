from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()
print(f"Nyckel: {key.decode()}")

cipher_suite = Fernet(key)

message = "Hemligt meddelande".encode()
cipher_text = cipher_suite.encrypt(message)
print(f"Krypterad text: {cipher_text}")

with open("encrypted_message.enc", "wb") as encoded_file:
    encoded_file.write(cipher_text)