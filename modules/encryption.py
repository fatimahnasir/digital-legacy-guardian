from cryptography.fernet import Fernet

def encrypt_data(text):

    key = Fernet.generate_key()

    cipher = Fernet(key)

    encrypted = cipher.encrypt(
        text.encode()
    )

    return key.decode(), encrypted.decode()


def decrypt_data(key, encrypted_text):

    cipher = Fernet(
        key.encode()
    )

    decrypted = cipher.decrypt(
        encrypted_text.encode()
    )

    return decrypted.decode()