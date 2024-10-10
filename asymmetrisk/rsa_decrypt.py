from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private_key.pem", "rb") as private_file:
    private_key = RSA.import_key(private_file.read())

rsa_cipher = PKCS1_OAEP.new(private_key)

with open("encrypted_message.enc", "rb") as encoded_file:
    message = encoded_file.read()
print(f"Krypterad text {message[:30]}")

plain_text = rsa_cipher.decrypt(message)
print(f"Dekrypterad text: {plain_text.decode()}")