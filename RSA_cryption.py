from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    return private_key, public_key


def encrypt_with_public_key(public_key, message):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def encrypt_with_private_key(private_key, message):
    ciphertext = private_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def decrypt_with_public_key(public_key, ciphertext):
    decrypted_message = public_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message


def decrypt_with_private_key(private_key, ciphertext):
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message


if __name__ == '__main__':
    # Sinh khóa công khai và khóa bí mật
    private_key, public_key = generate_rsa_key_pair()

    # Mã hóa bằng khóa công khai
    message = b"Hello, RSA!"
    ciphertext = encrypt_with_public_key(public_key, message)

    # Giải mã bằng khóa bí mật
    decrypted_message = decrypt_with_private_key(private_key, ciphertext)


    print("Plaintext:", decrypted_message.decode())
