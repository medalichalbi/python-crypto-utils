from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from key_gen import generate_key_pair
import datetime
import os

def generate_self_signed_certificate():
    private_key_file_path = "private_key.pem"
    cert_file_path = "cert_RSA.pem"
    valid_from= valid_to = None
   
    if not os.path.exists(private_key_file_path):
        generate_key_pair(private_key_file_path, 2048)

    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    cert_data = {
        'subject': private_key.publickey(),
        'issuer': private_key.publickey(),
        'version': 2,
        'serial_number': 1,
        'valid_from': valid_from or datetime.datetime.now(),
        'valid_to': valid_to or (datetime.datetime.now() + datetime.timedelta(days=365)),
    }

    h = SHA256.new(str(cert_data).encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(h)
    cert_data['signature'] = signature

    with open(cert_file_path, "wb") as cert_file:
        cert_file.write(private_key.export_key(format='PEM'))

    print(f"Certificat auto-signé généré et enregistré dans '{cert_file_path}'.")

def encrypt_message_with_certificate(message):
    cert_file_path = "cert_RSA.pem"
    with open(cert_file_path, "rb") as cert_file:
        cert_data = cert_file.read()
        public_key = RSA.import_key(cert_data)

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode("utf-8"))
    return ciphertext

generate_self_signed_certificate()

print("\n **********************************************\n")
message="oussama lassoued1"

x=encrypt_message_with_certificate(message)
print (f" {x}\n fin de message encrypt avec certif : ")
print("\n **********************************************\n")

