# Shift schedule for DES key generation
shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Get input 64-bit key from the user
key = int(input("Enter a 64-bit hexadecimal key (example: 133457799BBCDFF1): "), 16)

# Step 1: Split the key into two 28-bit halves
# The left 28 bits and right 28 bits
left_key = (key >> 36) & 0x0FFFFFFF  # Left 28 bits
right_key = (key >> 8) & 0x0FFFFFFF  # Right 28 bits

# Print the initial halves
print(f"Initial Left 28 bits: {bin(left_key)[2:].zfill(28)}")
print(f"Initial Right 28 bits: {bin(right_key)[2:].zfill(28)}")

# Step 2: Generate 16 subkeys
subkeys = []

for i in range(16):
    # Perform left circular shift on both halves according to the shift schedule
    shift = shift_schedule[i]
    
    left_key = ((left_key << shift) | (left_key >> (28 - shift))) & 0x0FFFFFFF
    right_key = ((right_key << shift) | (right_key >> (28 - shift))) & 0x0FFFFFFF

    # Take the first 24 bits from both left and right halves
    left_24_bits = (left_key >> 4) & 0xFFFFFF  # First 24 bits of left half
    right_24_bits = (right_key >> 4) & 0xFFFFFF  # First 24 bits of right half

    # Combine these to form a 48-bit subkey
    subkey = (left_24_bits << 24) | right_24_bits
    subkeys.append(subkey)

    # Print the generated subkey in binary format
    print(f"Subkey {i + 1}: {bin(subkey)[2:].zfill(48)}")

# Print all subkeys in hexadecimal format
print("\nSubkeys in hexadecimal format:")
for i, subkey in enumerate(subkeys):
    print(f"Subkey {i + 1}: {hex(subkey)[2:].upper().zfill(12)}")
