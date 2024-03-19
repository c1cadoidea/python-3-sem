price_per_m = float(input("Enter the price of a carpet per m^2: "))
length_float_sm  = float(input("Enter the lenght of room in sm: "))
width_float_sm  = float(input("Enter the width of room in sm: "))
area_float_sm = length_float_sm  * width_float_sm 
area_float_m = area_float_sm/10000
price_float = price_per_m * area_float_m

print(" ---------------------------------------------")
print("| {:^12} | {:^12} | {:^13} |".format("Measurement", "Area", "Price"))
print(" -------------------------------------------- ")
print("| {:^12} | {:<12.3f} | {:<11.2f} $ |".format("sm^2", area_float_sm, price_float))
print("| {:^12} | {:<12.3f} | {:<11.2f} $ |".format("m^2", area_float_m, price_float))
print(" ---------------------------------------------")
#test12

