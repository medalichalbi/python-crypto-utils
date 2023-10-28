from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def sign_message(message):
    private_key_file_path = "private_key.pem"
    
    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    hash_obj = SHA256.new(message.encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    return signature

def verify_signature( message, signature):
    public_key_file_path = "public_key.pem"

    with open(public_key_file_path, "rb") as public_key_file:
        public_key = RSA.import_key(public_key_file.read())

    hash_obj = SHA256.new(message.encode("utf-8"))
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        return True  
    except (ValueError, TypeError):
        return False 
    

print("\n **********************************************\n")
message="oussama lassoued"
signature = sign_message(message)
print(signature)
print("\n **********************************************\n")

x="dali chalbi"

print(verify_signature(message,signature))
print("\n **********************************************\n")
print(verify_signature(x,signature))

