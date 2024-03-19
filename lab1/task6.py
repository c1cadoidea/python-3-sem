i = 1
q = 1
while i < 20:
    print("stage", i)
    q = q * (i + 1)
    print(q)
    i += 1
print("\nThe product of the first 20 natural numbers is:", q)
