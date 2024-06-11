def find_infected_fridges(data):
    infected_indices = []
    for index, line in enumerate(data, start=1):
        pattern = "anton"
        i = 0
        for char in line:
            if char == pattern[i]:
                i += 1
                if i == len(pattern):
                    infected_indices.append(index)
                    break
    return infected_indices

while True:
    user_input = input("Продовжити? Y/N: ").strip().upper()
    if user_input == 'N':
        break
    elif user_input == 'Y':
        num_fridges = int(input("Введіть кількість холодильників: "))
        data = []
        for i in range(num_fridges):
            fridge_data = input(f"Введіть дані для холодильника {i+1}: ").strip()
            data.append(fridge_data)

        infected = find_infected_fridges(data)
        
        if infected:
            print("Номери заражених холодильників:")
            for idx in infected:
                print(f"Холодильник {idx}")
        else:
             print("Немає заражених холодильників.")

    else:
        print("Невірний ввід. Будь ласка, введіть 'Y' для продовження або 'N' для завершення.")