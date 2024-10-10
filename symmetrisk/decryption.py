from cryptography.fernet import Fernet

with open("encrypted_message.enc", "rb") as encoded_file:
    message = encoded_file.read()

with open("secret.key", "rb") as key_file:
    key = key_file.read()
print(f"Nyckel: {key.decode()}")

cipher_suite = Fernet(key)

plain_text = cipher_suite.decrypt(message)
print(f"Dekrypterad text: {plain_text.decode()}")