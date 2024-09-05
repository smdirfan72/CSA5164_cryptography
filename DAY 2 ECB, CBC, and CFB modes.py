from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Padding method: adds a 1 bit followed by as many 0 bits as needed to fill the block
def custom_pad(data, block_size):
    pad_len = block_size - len(data) % block_size
    padding = b'\x80' + b'\x00' * (pad_len - 1)  # 1 bit (0x80) followed by zero bits
    return data + padding

# Function to remove padding
def custom_unpad(data):
    return data.rstrip(b'\x00').rstrip(b'\x80')

# Get inputs from the user
key = input("Enter a 24-byte hexadecimal key (48 hex digits): ")
key_bytes = bytes.fromhex(key)

if len(key_bytes) != 24:
    raise ValueError("Key must be exactly 24 bytes (48 hex characters).")

plaintext = input("Enter plaintext (multiple of block size or will be padded): ")
plaintext_bytes = plaintext.encode()

# 3DES block size is 8 bytes
block_size = 8

# Pad the plaintext using the custom padding method
padded_plaintext = custom_pad(plaintext_bytes, block_size)

# ECB Mode
print("\n----- ECB Mode -----")
cipher_ecb = DES3.new(key_bytes, DES3.MODE_ECB)
ciphertext_ecb = cipher_ecb.encrypt(padded_plaintext)
print(f"Ciphertext (ECB) in hex: {ciphertext_ecb.hex()}")
decrypted_ecb = custom_unpad(cipher_ecb.decrypt(ciphertext_ecb))
print(f"Decrypted (ECB): {decrypted_ecb.decode()}")

# CBC Mode
print("\n----- CBC Mode -----")
iv_cbc = get_random_bytes(block_size)  # Initialization vector for CBC
cipher_cbc = DES3.new(key_bytes, DES3.MODE_CBC, iv_cbc)
ciphertext_cbc = cipher_cbc.encrypt(padded_plaintext)
print(f"Ciphertext (CBC) in hex: {ciphertext_cbc.hex()}")
cipher_cbc_decrypt = DES3.new(key_bytes, DES3.MODE_CBC, iv_cbc)
decrypted_cbc = custom_unpad(cipher_cbc_decrypt.decrypt(ciphertext_cbc))
print(f"Decrypted (CBC): {decrypted_cbc.decode()}")

# CFB Mode
print("\n----- CFB Mode -----")
iv_cfb = get_random_bytes(block_size)  # Initialization vector for CFB
cipher_cfb = DES3.new(key_bytes, DES3.MODE_CFB, iv_cfb)
ciphertext_cfb = cipher_cfb.encrypt(padded_plaintext)
print(f"Ciphertext (CFB) in hex: {ciphertext_cfb.hex()}")
cipher_cfb_decrypt = DES3.new(key_bytes, DES3.MODE_CFB, iv_cfb)
decrypted_cfb = custom_unpad(cipher_cfb_decrypt.decrypt(ciphertext_cfb))
print(f"Decrypted (CFB): {decrypted_cfb.decode()}")
