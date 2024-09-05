from sympy import mod_inverse, isprime
import random

def generate_prime(bits):
    """Generate a prime number with the given number of bits."""
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

def generate_key_pair(bits):
    """Generate RSA public and private key pair."""
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)

def rsa_encrypt(plaintext, public_key):
    """Encrypt the plaintext with the given public key."""
    e, n = public_key
    return pow(plaintext, e, n)

def rsa_decrypt(ciphertext, private_key):
    """Decrypt the ciphertext with the given private key."""
    d, n = private_key
    return pow(ciphertext, d, n)

# Generate original key pair
public_key, private_key = generate_key_pair(8)  # Use 8 bits for simplicity

# Encrypt and decrypt a message
message = 42
ciphertext = rsa_encrypt(message, public_key)
decrypted_message = rsa_decrypt(ciphertext, private_key)

print(f"Original Message: {message}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")

# Simulate private key leak scenario
print("\nSimulating private key leak...")

# Generate a new key pair
new_public_key, new_private_key = generate_key_pair(8)  # Use 8 bits for simplicity

print(f"New Public Key: {new_public_key}")
print(f"New Private Key: {new_private_key}")

# Note: The old private key is still compromised, and old ciphertexts can be decrypted with it.
