from Crypto.Cipher import AES
import base64

class SecretEncryptor:
    def __init__(self, key):
        self.key = key
        
    def encrypt_secrets(self, secrets):
        # Encrypt the values of the secrets dictionary and store them in a new dictionary
        encrypted_secrets = {}
        for k, v in secrets.items():
            cipher = AES.new(self.key, AES.MODE_ECB)
            padded_data = v.encode('utf-8') + (AES.block_size - len(v) % AES.block_size) * b"\0"
            encrypted_data = cipher.encrypt(padded_data)
            encrypted_secrets[k] = base64.b64encode(encrypted_data).decode('utf-8')

        return encrypted_secrets

    def save_secrets(self, filename, encrypted_secrets):
        # Save the encrypted secrets to a file
        with open(filename, 'w') as f:
            for k, v in encrypted_secrets.items():
                f.write(f"{k}={v}\n")
            print('Encryption successful. Encrypted data saved to', filename)
