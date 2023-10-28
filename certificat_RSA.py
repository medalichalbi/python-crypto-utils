from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import datetime
import os

def generate_key_pair_certif(private_key_file_path, public_key_file_path, key_size=2048):
    key = RSA.generate(key_size)

    private_key = key.export_key()
    with open(private_key_file_path, "wb") as private_key_file:
        private_key_file.write(private_key)

    public_key = key.publickey().export_key()
    with open(public_key_file_path, "wb") as public_key_file:
        public_key_file.write(public_key)

def generate_self_signed_certificate(private_key_file_path, cert_file_path, key_size=2048, valid_from=None, valid_to=None, serial_number=1, version=2):
    # Générer une nouvelle paire de clés RSA si elles n'existent pas déjà
    if not os.path.exists(private_key_file_path):
        generate_key_pair_certif(private_key_file_path, key_size)

    # Charger la clé privée pour signer le certificat
    with open(private_key_file_path, "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())

    # Créer un dictionnaire pour représenter les informations du certificat
    cert_data = {
        'subject': private_key.publickey(),
        'issuer': private_key.publickey(),
        'version': version,
        'serial_number': serial_number,
        'valid_from': valid_from or datetime.datetime.now(),
        'valid_to': valid_to or (datetime.datetime.now() + datetime.timedelta(days=365)),
    }

    # Signer le certificat avec la clé privée
    h = SHA256.new(str(cert_data).encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(h)
    cert_data['signature'] = signature

    # Enregistrer le contenu du certificat au format PEM dans le fichier
    with open(cert_file_path, "wb") as cert_file:
        cert_file.write(private_key.export_key(format='PEM'))

    print(f"Certificat auto-signé généré et enregistré dans '{cert_file_path}'.")

def encrypt_message_with_certificate(cert_file_path, message):
    with open(cert_file_path, "rb") as cert_file:
        cert_data = cert_file.read()
        public_key = RSA.import_key(cert_data)

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode("utf-8"))
    return ciphertext

generate_key_pair_certif("private_key_certif.pem","public_key_certif.pem")

generate_self_signed_certificate("private_key_certif.pem","cert_RSA.pem")

print("\n **********************************************\n")
message="oussama lassoued1"

x=encrypt_message_with_certificate("cert_RSA.pem",message)
print (f" {x}\n fin de message encrypt avec certif : ")
print("\n **********************************************\n")

