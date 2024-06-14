def vigenere_encrypt(plaintext, key):
    key = key.lower()
    key_repeated = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    ciphertext = ""

    for p_char, k_char in zip(plaintext, key_repeated):
        if p_char.isalpha():
            shift_base = ord('a') if p_char.islower() else ord('A')
            k_char_shift = ord(k_char) - ord('a')
            encrypted_char = chr((ord(p_char) - shift_base + k_char_shift) % 26 + shift_base)
            ciphertext += encrypted_char
        else:
            ciphertext += p_char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.lower()
    key_repeated = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    plaintext = ""

    for c_char, k_char in zip(ciphertext, key_repeated):
        if c_char.isalpha():
            shift_base = ord('a') if c_char.islower() else ord('A')
            k_char_shift = ord(k_char) - ord('a')
            decrypted_char = chr((ord(c_char) - shift_base - k_char_shift) % 26 + shift_base)
            plaintext += decrypted_char
        else:
            plaintext += c_char

    return plaintext

def main():
    while True:
        choice = input("Виберіть дію (encrypt/decrypt): ").strip().lower()
        if choice not in ["encrypt", "decrypt"]:
            print("Невірний вибір. Спробуйте ще раз.")
            continue

        text = input("Введіть текст: ")
        key = input("Введіть ключ: ")

        if choice == "encrypt":
            result = vigenere_encrypt(text, key)
            print(f"Зашифрований текст: {result}")
        else:
            result = vigenere_decrypt(text, key)
            print(f"Дешифрований текст: {result}")

        continue_choice = input("Бажаєте спробувати ще раз? (Y/N): ").strip().lower()
        if continue_choice != "y":
            break

if __name__ == "__main__":
    main()
