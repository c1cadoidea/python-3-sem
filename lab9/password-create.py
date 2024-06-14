import random

def get_user_input() -> tuple:
    while True:
        num_passwords = int(input("Кількість паролів для створення: "))
        length = int(input("Довжина одного пароля (бажано більше 10 символів): "))
        
        while True:
            if length < 10:
                length = int(input("Паролі з менш ніж 10 символів мають погану стійкість до взлому. Будь ласка, введіть нове значення:"))
                continue
            if length >= 10:
                break


        
        include_digits = input("Чи включати цифри 0123456789? (Y/N): ").upper() == 'Y'
        include_uppercase = input("Чи включати великі літери ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Y/N): ").upper() == 'Y'
        include_lowercase = input("Чи включати малі літери abcdefghijklmnopqrstuvwxyz? (Y/N): ").upper() == 'Y'
        include_punctuation = input("Чи включати символи !#$%&*+-=?@^_? (Y/N): ").upper() == 'Y'
        exclude_ambiguous = input("Чи виключати неоднозначні символи il1Lo0O? (Y/N): ").upper() == 'Y'

        return (num_passwords, length, include_digits, include_uppercase, include_lowercase, include_punctuation, exclude_ambiguous)


def generate_password(length: int, chars: str) -> str:
    return ''.join(random.choice(chars) for _ in range(length))
    pass


def main():
    num_passwords, length, include_digits, include_uppercase, include_lowercase, include_punctuation, exclude_ambiguous = get_user_input()
    
    chars = ''
    if include_digits:
        chars += '0123456789'
    if include_uppercase:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if include_lowercase:
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if include_punctuation:
        chars += '!#$%&*+-=?@^_.'
    if exclude_ambiguous:
        chars = chars.replace('i', '').replace('l', '').replace('1', '').replace('L', '').replace('o', '').replace('0', '').replace('O', '')
    
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, chars)
        passwords.append(password)
    
    for idx, password in enumerate(passwords, start=1):
        print(f"Пароль {idx}: {password}")

    while True:
        repeat = input("Бажаєте згенерувати ще паролі? (Y/N): ").strip().upper()
        if repeat == 'Y':
            break
        elif repeat == 'N':
            return
        else:
            print("Будь ласка, введіть 'Y' або 'N'.")    


if __name__ == "__main__":
    main()

