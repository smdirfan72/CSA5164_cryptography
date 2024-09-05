from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Function to simulate error by modifying one byte in the ciphertext
def introduce_error(ciphertext):
    corrupted_ciphertext = bytearray(ciphertext)
    # Flip one bit in the first byte of the first block (C1)
    corrupted_ciphertext[0] ^= 0x01
    return bytes(corrupted_ciphertext)

# Get the 24-byte key and plaintext from the user
key = input("Enter a 24-byte hexadecimal key (48 hex digits): ")
key_bytes = bytes.fromhex(key)

if len(key_bytes) != 24:
    raise ValueError("Key must be exactly 24 bytes (48 hex characters).")

plaintext = input("Enter plaintext to encrypt: ")
plaintext_bytes = plaintext.encode()

# ECB Mode
# ----------------------
cipher_ecb = DES3.new(key_bytes, DES3.MODE_ECB)

# Padding the plaintext to be a multiple of 8 bytes
padded_plaintext = pad(plaintext_bytes, DES3.block_size)

# Encrypt the plaintext in ECB mode
ciphertext_ecb = cipher_ecb.encrypt(padded_plaintext)

# Introduce error in ECB ciphertext
corrupted_ciphertext_ecb = introduce_error(ciphertext_ecb)

# Decrypt the corrupted ECB ciphertext
try:
    decrypted_ecb = unpad(cipher_ecb.decrypt(corrupted_ciphertext_ecb), DES3.block_size)
    print(f"ECB Decrypted plaintext with error: {decrypted_ecb.decode()}")
except ValueError:
    print("ECB Decryption failed due to padding error.")

# CBC Mode
# ----------------------
# Generate a random 8-byte IV for CBC mode
iv = get_random_bytes(8)
cipher_cbc = DES3.new(key_bytes, DES3.MODE_CBC, iv)

# Encrypt the plaintext in CBC mode
ciphertext_cbc = cipher_cbc.encrypt(padded_plaintext)

# Introduce error in CBC ciphertext (first block)
corrupted_ciphertext_cbc = introduce_error(ciphertext_cbc)

# Decrypt the corrupted CBC ciphertext
cipher_cbc_decrypt = DES3.new(key_bytes, DES3.MODE_CBC, iv)
try:
    decrypted_cbc = unpad(cipher_cbc_decrypt.decrypt(corrupted_ciphertext_cbc), DES3.block_size)
    print(f"CBC Decrypted plaintext with error: {decrypted_cbc.decode()}")
except ValueError:
    print("CBC Decryption failed due to padding error.")
