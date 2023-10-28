from Crypto.PublicKey import RSA

def generate_key_pair(key_size=2048):
    private_key_file_path = "private_key.pem"
    public_key_file_path = "public_key.pem"
    
    key = RSA.generate(key_size)

    private_key = key.export_key()
    with open(private_key_file_path, "wb") as private_key_file:
        private_key_file.write(private_key)

    public_key = key.publickey().export_key()
    with open(public_key_file_path, "wb") as public_key_file:
        public_key_file.write(public_key)




