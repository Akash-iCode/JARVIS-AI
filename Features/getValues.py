from decrypt import SecretsDecryptor
# Create an instance of SecretsDecryptor with a custom key (optional)
decryptor = SecretsDecryptor(key=b'1234567890123456' )

# Decrypt the secrets from the file
secrets = decryptor.decrypt_secrets('secrets.txt')

# Print the decrypted secrets
print(secrets)


