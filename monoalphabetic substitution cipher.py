import random
import string

def generate_cipher_alphabet():
  
    alphabet = list(string.ascii_lowercase)
    cipher_alphabet = alphabet[:]  
    random.shuffle(cipher_alphabet)  
    return ''.join(cipher_alphabet)

def create_mapping(plain_alphabet, cipher_alphabet):
    mapping = dict(zip(plain_alphabet, cipher_alphabet))
    reverse_mapping = dict(zip(cipher_alphabet, plain_alphabet))
    return mapping, reverse_mapping

def encrypt(text, mapping):
    encrypted_text = ''.join(mapping.get(char, char) for char in text.lower())
    return encrypted_text

def decrypt(encrypted_text, reverse_mapping):
    decrypted_text = ''.join(reverse_mapping.get(char, char) for char in encrypted_text.lower())
    return decrypted_text

def main():
    plain_alphabet = string.ascii_lowercase
    cipher_alphabet = generate_cipher_alphabet()

    print("Plain Alphabet: ", plain_alphabet)
    print("Cipher Alphabet:", cipher_alphabet)

    mapping, reverse_mapping = create_mapping(plain_alphabet, cipher_alphabet)

    text = input("Enter the text to encrypt: ")

    encrypted_text = encrypt(text, mapping)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, reverse_mapping)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
