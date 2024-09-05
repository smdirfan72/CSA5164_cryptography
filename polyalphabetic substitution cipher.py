def encrypt_char(plaintext_char, key_char):
    """Encrypt a single character using the key character."""
    if plaintext_char.isalpha():
        # Determine the base ASCII value for uppercase or lowercase
        base = ord('A') if plaintext_char.isupper() else ord('a')
        key_base = ord('A') if key_char.isupper() else ord('a')
        
        # Encrypt character and return result
        return chr((ord(plaintext_char) - base + (ord(key_char) - key_base)) % 26 + base)
    else:
        return plaintext_char  # Non-alphabetic characters are not encrypted

def encrypt_text(plaintext, key):
    """Encrypt the entire plaintext using the provided key."""
    encrypted_text = []
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            encrypted_text.append(encrypt_char(char, key[key_index]))
            key_index = (key_index + 1) % key_length
        else:
            encrypted_text.append(char)  # Non-alphabetic characters are not encrypted

    return ''.join(encrypted_text)

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    # Encrypt the plaintext
    encrypted_text = encrypt_text(plaintext, key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
