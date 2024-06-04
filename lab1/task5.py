amount_50 = int(input("How many coins of 50 cents do you have? : "))
amount_25 = int(input("How many coins of 25 cents do you have? : "))
amount_10 = int(input("How many coins of 10 cents do you have? : "))
amount_5 = int(input("How many coins of 5 cents do you have? : "))

all_money = amount_50 * 0.5 + amount_25 * 0.25 + amount_10 * 0.1 + amount_5 * 0.05
print("You have :", all_money, "grivnas")
15