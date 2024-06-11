import matplotlib.pyplot as plt
import numpy as np

# Дані
t = [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4]
K = [0.227, 0.185, 0.138, 0.086, 0.058, -0.008, -0.059]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(t, K, marker='o', linestyle='-', color='b')

# Додавання підписів точок
for i, txt in enumerate(K):
    plt.annotate(f'{txt:.3f}', (t[i], K[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Підписи осей
plt.xlabel('t')
plt.ylabel('K')


# Сітка
plt.grid(True)

# Відображення графіка
plt.show()
