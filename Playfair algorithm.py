def create_matrix(keyword):
    matrix = []
    used = set()
    for char in keyword.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used and char != 'J':
            matrix.append(char)
            used.add(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def encrypt_pair(matrix, a, b):
    ra, ca = find_position(matrix, a)
    rb, cb = find_position(matrix, b)
    if ra == rb:
        return matrix[ra][(ca + 1) % 5] + matrix[rb][(cb + 1) % 5]
    elif ca == cb:
        return matrix[(ra + 1) % 5][ca] + matrix[(rb + 1) % 5][cb]
    else:
        return matrix[ra][cb] + matrix[rb][ca]

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    if len(text) % 2 != 0:
        pairs.append(text[-1] + 'X')
    return pairs

def encrypt_text(matrix, text):
    pairs = prepare_text(text)
    return ''.join(encrypt_pair(matrix, a, b) for a, b in pairs)

def main():
    keyword = input("Enter the keyword: ")
    plaintext = input("Enter the plaintext: ")
    matrix = create_matrix(keyword)
    encrypted_text = encrypt_text(matrix, plaintext)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
