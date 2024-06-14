def read_prices(filename):
    orders = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                item = parts[0].strip()
                quantity = int(parts[1].strip())
                price_per_item = int(parts[2].strip())
                orders.append((item, quantity, price_per_item))
    return orders

def calculate_total_cost(orders):
    total_cost = 0
    for item, quantity, price_per_item in orders:
        total_cost += quantity * price_per_item
    return total_cost

def main():
    filename = "prices.txt"
    orders = read_prices(filename)
    total_cost = calculate_total_cost(orders)
    print(f"Загальна вартість замовлення: {total_cost} грн")

if __name__ == "__main__":
    main()
