from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message(public_key_file_path, message):
    # Charger la clé publique du fichier
    with open(public_key_file_path, "rb") as public_key_file:
        public_key = RSA.import_key(public_key_file.read())

    # Chiffrement du message
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode("utf-8"))
    return ciphertext

def decrypt_message(private_key_file_path, ciphertext):
    # Charger la clé privée du fichier
    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    # Déchiffrement du message
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode("utf-8")

print("\n **********************************************\n")
message="oussama lassoued"
message_cryption = encrypt_message("public_key.pem",message)
print(message_cryption)

print("\n **********************************************\n")

message_decryption = decrypt_message("private_key.pem",message_cryption)
print(message_decryption)