def calculate_series_sum(terms):
    series_sum = 0
    for n in range(1, terms + 1):
        a_n = ((-1) ** n) * (2 ** n) / (n ** (n + 1) + 1)
        series_sum += a_n
    return series_sum

# Кількість членів ряду
num_terms = 10

sum_of_series = calculate_series_sum(num_terms)

print(f"Сума перших {num_terms} членів ряду: {sum_of_series}")
