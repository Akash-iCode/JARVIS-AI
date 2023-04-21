from Crypto.Cipher import AES
import base64
import imaplib
import email

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
#secreKey
decryptor = SecretsDecryptor(key=b'1234567890123456' )

# Decrypt the secrets from the file
secrets = decryptor.decrypt_secrets('secrets.txt')

FROM_EMAIL = secrets["Email"]
FROM_PWD = secrets["Password"]
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993


class EmailReader:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(email_address, password)
        self.mail.select('inbox')
        
    def get_latest_emails(self, num_emails):
        self.mail.select('inbox')
        _, data = self.mail.search(None, 'UNSEEN')
        mail_ids = data[0].split()
        
        if not mail_ids:
            return "No Unread Mails"
        
        latest_emails = []
        for i in reversed(range(len(mail_ids)-num_emails, len(mail_ids))):
            _, data = self.mail.fetch(mail_ids[i], "(RFC822)")
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            latest_emails.append(email_message)
        return latest_emails
    
# email_reader = EmailReader('your_email_address@gmail.com', 'your_password')
# latest_emails = email_reader.get_latest_emails(5)

# if isinstance(latest_emails, str):
#     print(latest_emails)
# else:
#     for email in latest_emails:
        print('Subject:', email['Subject'])
        print('From:', email['From'])
        print('Date:', email['Date'])
        print('Body:', email.get_payload())
        print('-----------------------------')