def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            new_pos = (ord(char) - ord('A') + shift) % 26
            result += chr(new_pos + ord('A'))
        elif char.islower():
            new_pos = (ord(char) - ord('a') + shift) % 26
            result += chr(new_pos + ord('a'))
        else:
            result += char

    return result

text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (1-25): "))

if 1 <= shift <= 25:
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)
else:
    print("Invalid shift value. Please enter a number between 1 and 25.")
