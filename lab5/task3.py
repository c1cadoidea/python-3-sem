def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False

    diff_count = sum(1 for char1, char2 in zip(word1, word2) if char1 != char2)
    return diff_count == 1

while True:
    proceed = input("Продовжити? (Y-так/N-ні): ").strip().upper()
    if proceed == 'N':
        break
    elif proceed == 'Y':
        word1 = input("Введіть перше слово: ")
        word2 = input("Введіть друге слово: ")

        if is_one_away(word1, word2):
            print("Слова мають однакову довжину і відрізняються рівно в одному символі.")
        else:
            print("Слова не відповідають умові.")
    else:
        print("Будь ласка, введіть 'Y' для продовження або 'N' для виходу.")
