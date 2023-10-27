from Crypto.PublicKey import RSA

def generate_key_pair(private_key_file_path, public_key_file_path, key_size=2048):
    # Génération de la paire de clés
    key = RSA.generate(key_size)

    # Sauvegarde de la clé privée dans un fichier
    private_key = key.export_key()
    with open(private_key_file_path, "wb") as private_key_file:
        private_key_file.write(private_key)

    # Sauvegarde de la clé publique dans un fichier
    public_key = key.publickey().export_key()
    with open(public_key_file_path, "wb") as public_key_file:
        public_key_file.write(public_key)

# Exemple d'utilisation de la fonction
generate_key_pair("private_key.pem", "public_key.pem")

f=open("private_key.pem","r")
for i in f : 
    print(i.strip("-----BEGIN RSA PRIVATE KEY-----"+"-----END RSA PRIVATE KEY-----"))

