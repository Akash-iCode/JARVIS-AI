from encrypt import SecretEncryptor

# Ask the user for the secret values
secrets = {}
secrets['api_key'] = "N9x4g6/llGBaW0E42MkoQZ9mJoYVKn/tqMdOeRQ+fYqGhs7dBiwX8g=="
secrets['wakeWords'] = ["jarvis", "hey google", "alexa", "hey siri", "ok google"]

# Create a SecretEncryptor instance with the encryption key
key = b'1234567890123456'
encryptor = SecretEncryptor(key)

# Encrypt and save the secrets
encrypted_secrets = encryptor.encrypt_secrets(secrets)
encryptor.save_secrets('porcupineAccess.txt', encrypted_secrets)