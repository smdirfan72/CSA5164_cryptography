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

# Example RSA encryption/decryption
def example_rsa():
    public_key, private_key = generate_key_pair(8)  # Use 8 bits for simplicity

    # Encrypt and decrypt a message
    plaintext_values = list(range(26))  # 'A' to 'Z'
    encrypted_values = [rsa_encrypt(p, public_key) for p in plaintext_values]
    decrypted_values = [rsa_decrypt(c, private_key) for c in encrypted_values]

    print("Plaintext values:", plaintext_values)
    print("Encrypted values:", encrypted_values)
    print("Decrypted values:", decrypted_values)

example_rsa()
