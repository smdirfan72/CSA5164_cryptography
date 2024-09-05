# Example Permutation tables and shift schedule for simplicity
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# Shift schedule
shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Input key and ciphertext from user
key = int(input("Enter a 64-bit hexadecimal key (example: 133457799BBCDFF1): "), 16)
ciphertext = int(input("Enter the 64-bit ciphertext (example: 85E813540F0AB405): "), 16)

# Step 1: Apply the Initial Permutation (IP) on the ciphertext
initial_permuted_block = 0
for i in range(64):
    initial_permuted_block <<= 1
    initial_permuted_block |= (ciphertext >> (64 - IP[i])) & 1

# Step 2: Split the permuted block into left and right halves
left = initial_permuted_block >> 32
right = initial_permuted_block & 0xFFFFFFFF

# Step 3: Generate the 16 subkeys (simplified version)
subkeys = []
left_key = (key >> 36) & 0x0FFFFFFF  # 28 bits
right_key = (key >> 8) & 0x0FFFFFFF  # 28 bits

for i in range(16):
    # Perform left circular shift
    left_key = ((left_key << shift_schedule[i]) | (left_key >> (28 - shift_schedule[i]))) & 0x0FFFFFFF
    right_key = ((right_key << shift_schedule[i]) | (right_key >> (28 - shift_schedule[i]))) & 0x0FFFFFFF
    
    # Combine left and right to form a subkey (simplified)
    subkeys.append((left_key << 28) | right_key)

# Step 4: Perform 16 rounds of decryption using the keys in reverse order
for i in range(15, -1, -1):
    previous_right = right
    right = left ^ (previous_right ^ subkeys[i])  # Simplified Feistel-like function
    left = previous_right

# Step 5: Combine the two halves and apply the Final Permutation (FP)
combined_block = (right << 32) | left
plaintext = 0
for i in range(64):
    plaintext <<= 1
    plaintext |= (combined_block >> (64 - FP[i])) & 1

# Output the decrypted plaintext
print(f"Decrypted plaintext: {plaintext:016X}")
