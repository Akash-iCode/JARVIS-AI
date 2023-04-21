from encrypt import SecretEncryptor

# Ask the user for the secret values
secrets = {}
secrets['api_key'] = input("Enter the API key: ")
secrets['Email'] = input("Enter the mail ID : ")
secrets['Password'] = input("Enter the password: ")
secrets['anotherToken'] = input("Enter the another token: ")

# Create a SecretEncryptor instance with the encryption key
key = b'1234567890123456'
encryptor = SecretEncryptor(key)

# Encrypt and save the secrets
encrypted_secrets = encryptor.encrypt_secrets(secrets)
encryptor.save_secrets('secrets.txt', encrypted_secrets)