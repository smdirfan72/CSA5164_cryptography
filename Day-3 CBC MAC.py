def xor_blocks(block1, block2):
    """ XOR two blocks of data. """
    return bytes([b1 ^ b2 for b1, b2 in zip(block1, block2)])

def cbc_mac(key, message):
    """ Compute a simple CBC-MAC of a message using XOR. """
    block_size = len(key)
    
    # Pad message to be a multiple of block size
    if len(message) % block_size != 0:
        padding_length = block_size - (len(message) % block_size)
        message += bytes([padding_length] * padding_length)
    
    # Initialize CBC-MAC with zero IV
    iv = bytes([0] * block_size)
    prev_block = iv
    
    # Process the message block-by-block
    mac = iv
    for i in range(0, len(message), block_size):
        block = message[i:i + block_size]
        block = xor_blocks(block, prev_block)
        prev_block = block
        mac = block
    
    return mac

def main():
    # Key and message
    key = bytes([0] * 16)  # Example key (16 bytes)
    X = b'This is a test message.'[:16]  # Message block (must be exactly one block)
    
    # Compute CBC-MAC for X
    T = cbc_mac(key, X)
    print(f'Key: {key.hex()}')
    print(f'Original Message Block X: {X.hex()}')
    print(f'MAC T: {T.hex()}')
    
    # Create the two-block message
    X_xor_T = xor_blocks(X, T)
    two_block_message = X + X_xor_T
    
    # Compute CBC-MAC for the two-block message
    mac_two_block = cbc_mac(key, two_block_message)
    print(f'Two-Block Message: {two_block_message.hex()}')
    print(f'MAC for Two-Block Message: {mac_two_block.hex()}')

if __name__ == "__main__":
    main()
