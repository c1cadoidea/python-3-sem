def caesar_cipher(text, shift, alphabet):
    encrypted_text = []
    alphabet_len = len(alphabet)
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = alphabet.upper()
            else:
                base = alphabet.lower()

            idx = base.find(char)
            if idx != -1:
                new_idx = (idx + shift) % alphabet_len
                encrypted_text.append(base[new_idx])
            else:
                encrypted_text.append(char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decipher(text, shift, alphabet):
    return caesar_cipher(text, -shift, alphabet)

def get_alphabet(language):
    if language == 'en':
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif language == 'ua':
        return 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    else:
        raise ValueError("Unsupported language")

def main():
    direction = input("Enter direction (encrypt/decrypt): ").strip().lower()
    language = input("Enter language (en/ua): ").strip().lower()
    shift = int(input("Enter shift: "))

    alphabet = get_alphabet(language)

    text = input("Enter text: ")

    if direction == 'encrypt':
        result = caesar_cipher(text, shift, alphabet)
    elif direction == 'decrypt':
        result = caesar_decipher(text, shift, alphabet)
    else:
        print("Unsupported direction")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
