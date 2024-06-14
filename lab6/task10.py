import random

def generate_alphabet_pairs():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet)
    row1 = alphabet[:13]
    row2 = alphabet[13:]
    return row1, row2

def create_encryption_dict(row1, row2):
    encryption_dict = {}
    for i in range(13):
        encryption_dict[row1[i]] = row2[i]
        encryption_dict[row2[i]] = row1[i]
    return encryption_dict

def encrypt_decrypt(text, encryption_dict):
    result = []
    for char in text:
        if char.lower() in encryption_dict:
            if char.isupper():
                result.append(encryption_dict[char.lower()].upper())
            else:
                result.append(encryption_dict[char])
        else:
            result.append(char)
    return ''.join(result)

def main():
    row1, row2 = generate_alphabet_pairs()
    encryption_dict = create_encryption_dict(row1, row2)
    
    print("Row 1:", ''.join(row1))
    print("Row 2:", ''.join(row2))
    
    while True:
        direction = input("Enter direction (encrypt/decrypt) or 'exit' to quit: ").strip().lower()
        if direction == 'exit':
            break
        if direction not in ('encrypt', 'decrypt'):
            print("Unsupported direction")
            continue
        
        text = input("Enter text: ").strip()
        result = encrypt_decrypt(text, encryption_dict)
        
        print("Result:", result)

if __name__ == "__main__":
    main()
