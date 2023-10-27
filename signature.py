from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def sign_message(private_key_file_path, message):
    # Charger la clé privée du fichier
    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    # Signature du message
    hash_obj = SHA256.new(message.encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    return signature

def verify_signature(public_key_file_path, message, signature):
    # Charger la clé publique du fichier
    with open(public_key_file_path, "rb") as public_key_file:
        public_key = RSA.import_key(public_key_file.read())

    # Vérification de la signature
    hash_obj = SHA256.new(message.encode("utf-8"))
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        return True  # La signature est valide
    except (ValueError, TypeError):
        return False 
print("\n **********************************************\n")
message="oussama lassoued"
signature = sign_message("private_key.pem",message)
print(signature)
print("\n **********************************************\n")

x="dali chalbi"

print(verify_signature("public_key.pem",message,signature))
print("\n **********************************************\n")
print(verify_signature("public_key.pem",x,signature))

