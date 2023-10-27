from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import datetime
import os
from key_gen import generate_key_pair

def generate_key_pair(private_key_file_path, public_key_file_path, key_size=2048):
    key = RSA.generate(key_size)

    private_key = key.export_key()
    with open(private_key_file_path, "wb") as private_key_file:
        private_key_file.write(private_key)

    public_key = key.publickey().export_key()
    with open(public_key_file_path, "wb") as public_key_file:
        public_key_file.write(public_key)

def generate_self_signed_certificate(private_key_file_path, public_key_file_path, cert_file_path, key_size=2048):
    if not (os.path.exists(private_key_file_path) and os.path.exists(public_key_file_path)):
        generate_key_pair(private_key_file_path, public_key_file_path, key_size)

    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    cert = {
        "subject": private_key.publickey(),
        "issuer": private_key.publickey(),
        "valid_from": datetime.datetime(2023, 1, 1),
        "valid_to": datetime.datetime(2023, 12, 31),
        "serial_number": 1,
        "version": 2
    }

    h = SHA256.new(str(cert).encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(h)
    cert["signature"] = signature

    with open(cert_file_path, "wb") as cert_file:
        cert_file.write(str(cert).encode("utf-8"))

def encrypt_message_with_certificate(cert_file_path, message):
    with open(cert_file_path, "rb") as cert_file:
        cert_data = cert_file.read()
        public_key = RSA.import_key(cert_data)

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode("utf-8"))
    return ciphertext

generate_self_signed_certificate("private_key.pem","public_key.pem","cert_RSA.pem")

print("\n **********************************************\n")
message="oussama lassoued"
message_certificat = encrypt_message_with_certificate("cert_RSA.pem",message)
print(message_certificat)

