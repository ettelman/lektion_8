from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("public_key.pem", "rb") as public_file:
    public_key = RSA.import_key(public_file.read())

rsa_cipher = PKCS1_OAEP.new(public_key)

message = "Hemligt meddelande".encode()
cipher_text = rsa_cipher.encrypt(message)

with open("encrypted_message.enc", "wb") as encoded_file:
    encoded_file.write(cipher_text)
print("Krypterat meddelande sparat i 'encrypted_message.enc")