from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message(message):
    public_key_file_path = "public_key.pem"
    with open(public_key_file_path, "rb") as public_key_file:
        public_key = RSA.import_key(public_key_file.read())

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode("utf-8"))
    return ciphertext

def decrypt_message(ciphertext):
    private_key_file_path = "private_key.pem"

    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode("utf-8")

print("\n **********************************************\n")
message="oussama lassoued"
message_cryption = encrypt_message(message)
print(message_cryption)

print("\n **********************************************\n")

message_decryption = decrypt_message(message_cryption)
print(message_decryption)