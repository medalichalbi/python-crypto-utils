from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_message(message):
    private_key_file_path = "private_key.pem"

    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(message)
    return plaintext.decode("utf-8")

