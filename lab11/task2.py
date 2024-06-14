def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(ciphertext):
    possible_decryptions = []
    for shift in range(1, 26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        possible_decryptions.append((shift, decrypted_text))
    return possible_decryptions

def main():
    while True:
        ciphertext = input("Введіть зашифрований текст: ")

        possible_decryptions = brute_force_caesar(ciphertext)

        for shift, decrypted_text in possible_decryptions:
            print(f"Shift {shift}: {decrypted_text}")

        continue_choice = input("Бажаєте спробувати ще раз? (Y/N): ").strip().lower()
        if continue_choice != "Y":
            break

if __name__ == "__main__":
    main()
