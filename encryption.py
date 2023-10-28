from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message(message):
    public_key_file_path = "public_key.pem"
    with open(public_key_file_path, "rb") as public_key_file:
        public_key = RSA.import_key(public_key_file.read())

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode("utf-8"))
    return ciphertext

