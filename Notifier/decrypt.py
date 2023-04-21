from Crypto.Cipher import AES
import base64

class SecretsDecryptor:
    def __init__(self, key=b'1234567890123456'):
        self.key = key
    
    def decrypt_secrets(self, filepath):
        # Load the encrypted secrets from the file
        encrypted_secrets = {}
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    idx = line.find('=')
                    k = line[:idx]
                    v = line[idx+1:]
                    encrypted_secrets[k] = v

        # Decrypt the values of the encrypted secrets dictionary and store them in a new dictionary
        secrets = {}
        for k, v in encrypted_secrets.items():
            cipher = AES.new(self.key, AES.MODE_ECB)
            encrypted_data = base64.b64decode(v.encode('utf-8'))
            decrypted_data = cipher.decrypt(encrypted_data).rstrip(b"\0").decode('utf-8')
            secrets[k] = decrypted_data

        # Return the decrypted dictionary
        return secrets
