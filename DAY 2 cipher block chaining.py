from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Get inputs from the user
key = input("Enter a 24-byte hexadecimal key (48 hex digits): ")
key_bytes = bytes.fromhex(key)

# Ensure the key length is 24 bytes for 3DES
if len(key_bytes) != 24:
    raise ValueError("Key must be exactly 24 bytes (48 hex characters).")

plaintext = input("Enter plaintext to encrypt: ")
plaintext_bytes = plaintext.encode()

# Generate a random 8-byte (64-bit) IV for CBC mode
iv = get_random_bytes(8)

# Create a 3DES cipher object in CBC mode
cipher = DES3.new(key_bytes, DES3.MODE_CBC, iv)

# Pad the plaintext to be a multiple of 8 bytes, as required by 3DES
padded_plaintext = pad(plaintext_bytes, DES3.block_size)

# Encrypt the padded plaintext
ciphertext = cipher.encrypt(padded_plaintext)

# Print the results
print(f"IV (Initialization Vector): {iv.hex()}")
print(f"Ciphertext (in hex): {ciphertext.hex()}")
