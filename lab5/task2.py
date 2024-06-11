def is_password_good(password):
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_upper and has_lower and has_digit:
        return True
    else:
        return False

password = input("Введіть пароль для перевірки: ")
if is_password_good(password):
    print("Пароль надійний.")
else:
    print("Пароль ненадійний.")
