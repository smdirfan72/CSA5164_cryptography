def left_shift_one_bit(block, block_size):
    """ Left shift a block by one bit and handle overflow. """
    block = int.from_bytes(block, byteorder='big')
    shifted = block << 1
    if shifted >= (1 << block_size):
        shifted ^= CONSTANTS[block_size]
    return shifted.to_bytes(block_size // 8, byteorder='big')

def generate_subkeys(block_size):
    """ Generate K1 and K2 subkeys for a given block size. """
    # Create a block of all zeros
    zero_block = bytes([0] * (block_size // 8))
    
    # Simulate AES encryption of zero block to get L
    # In a real scenario, you would use a library to perform the encryption
    # Here we'll just simulate it
    L = zero_block
    
    # Generate K1
    K1 = left_shift_one_bit(L, block_size)
    
    # Generate K2
    K2 = left_shift_one_bit(K1, block_size)
    
    return K1, K2

# Define constants for different block sizes
CONSTANTS = {
    128: 0x87,
    64: 0x1B
}

def main():
    for block_size in [128, 64]:
        K1, K2 = generate_subkeys(block_size)
        print(f"Block Size: {block_size} bits")
        print(f"K1: {K1.hex()}")
        print(f"K2: {K2.hex()}")
        print()

if __name__ == "__main__":
    main()
