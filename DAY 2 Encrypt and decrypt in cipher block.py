# Convert binary string to integer
def bin_to_int(bin_str):
    return int(bin_str, 2)

# Convert integer to binary string with padding
def int_to_bin(value, length):
    return bin(value)[2:].zfill(length)

# S-DES Key Generation
def generate_sdes_keys(key):
    # Left circular shift by 1 bit (for simplicity)
    key_left_shifted = (key << 1 | key >> (len(bin(key))-3)) & 0b1111111111  # 10-bit key shift
    subkey1 = (key >> 1) & 0b11111  # Take left 5 bits
    subkey2 = (key_left_shifted >> 1) & 0b11111  # Take left 5 bits after shift
    return subkey1, subkey2

# Simplified DES (S-DES) encryption round (only one round for illustration)
def sdes_encrypt_block(block, key):
    # XOR the block with the subkey (for simplicity)
    return block ^ key

# S-DES CBC Mode Encryption
def cbc_encrypt(plaintext, key, iv):
    # Split the plaintext into 8-bit blocks
    blocks = [plaintext[i:i + 8] for i in range(0, len(plaintext), 8)]
    
    subkey1, subkey2 = generate_sdes_keys(key)  # Generate keys for encryption

    encrypted_blocks = []
    previous_block = iv  # Set IV as the first block for CBC mode
    
    for block in blocks:
        block_int = bin_to_int(block)  # Convert binary block to integer
        # XOR the block with the previous ciphertext (IV for the first block)
        xored_block = block_int ^ previous_block
        # Encrypt the xored block with S-DES using the first subkey
        encrypted_block = sdes_encrypt_block(xored_block, subkey1)
        encrypted_blocks.append(int_to_bin(encrypted_block, 8))  # Store the encrypted block
        previous_block = encrypted_block  # Update previous block for the next round

    return ''.join(encrypted_blocks)

# S-DES CBC Mode Decryption
def cbc_decrypt(ciphertext, key, iv):
    # Split the ciphertext into 8-bit blocks
    blocks = [ciphertext[i:i + 8] for i in range(0, len(ciphertext), 8)]
    
    subkey1, subkey2 = generate_sdes_keys(key)  # Generate keys for decryption

    decrypted_blocks = []
    previous_block = iv  # Set IV as the first block for CBC mode
    
    for block in blocks:
        block_int = bin_to_int(block)  # Convert binary block to integer
        # Decrypt the block with S-DES using the first subkey
        decrypted_block = sdes_encrypt_block(block_int, subkey1)  # Same operation for simplicity
        # XOR the decrypted block with the previous ciphertext (IV for the first block)
        xored_block = decrypted_block ^ previous_block
        decrypted_blocks.append(int_to_bin(xored_block, 8))  # Store the decrypted block
        previous_block = block_int  # Update previous block for the next round

    return ''.join(decrypted_blocks)

# Test data
binary_plaintext = '0000000100100011'  # Plaintext: 0000 0001 0010 0011
binary_key = '0111111101'  # Key: 01111 11101
binary_iv = '10101010'  # IV: 1010 1010

# Convert binary key and IV to integers
key_int = bin_to_int(binary_key)
iv_int = bin_to_int(binary_iv)

# Encrypt the plaintext using CBC mode
encrypted = cbc_encrypt(binary_plaintext, key_int, iv_int)
print(f"Encrypted ciphertext: {encrypted}")

# Decrypt the ciphertext back to plaintext using CBC mode
decrypted = cbc_decrypt(encrypted, key_int, iv_int)
print(f"Decrypted plaintext: {decrypted}")
