# crypto_utils.py
# pip install cryptography

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hmac
import os
import hashlib
import base64

# Fonction pour générer une clé symétrique aléatoire (AES 256)
def generate_symmetric_key():
    return os.urandom(32)  # 32 bytes for AES-256


# Fonction pour chiffrer des données avec AES (mode GCM)
def encrypt_data_aes(key, plaintext):
    iv = os.urandom(12)  # IV (initialization vector) for GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return (iv, ciphertext, encryptor.tag)  # Return IV, ciphertext, and GCM tag


# Fonction pour déchiffrer des données chiffrées avec AES (GCM)
def decrypt_data_aes(key, iv, ciphertext, tag):
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()


# Fonction pour hacher des données avec SHA-256
def hash_data_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode())
    return sha256_hash.hexdigest()


# Fonction pour générer une paire de clés RSA (clé privée et clé publique)
def generate_rsa_keypair(key_size=2048):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


# Fonction pour chiffrer des données avec RSA (clé publique)
def encrypt_data_rsa(public_key, plaintext):
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


# Fonction pour déchiffrer des données avec RSA (clé privée)
def decrypt_data_rsa(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()


# Fonction pour sérialiser une clé privée en format PEM
def serialize_private_key(private_key):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem


# Fonction pour sérialiser une clé publique en format PEM
def serialize_public_key(public_key):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem


# Fonction pour générer une clé dérivée d'un mot de passe avec PBKDF2
def derive_key_from_password(password, salt, iterations=100000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key


# Fonction pour calculer un HMAC pour des données avec une clé
def calculate_hmac(key, data):
    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(data.encode())
    return h.finalize()


# Fonction pour vérifier un HMAC
def verify_hmac(key, data, hmac_to_verify):
    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(data.encode())
    try:
        h.verify(hmac_to_verify)
        return True
    except Exception:
        return False


# Fonction pour encoder des données en base64
def encode_base64(data):
    return base64.b64encode(data).decode()


# Fonction pour décoder des données encodées en base64
def decode_base64(data):
    return base64.b64decode(data.encode())


