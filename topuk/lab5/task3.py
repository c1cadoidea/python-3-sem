import numpy as np
import matplotlib.pyplot as plt

# Дані з таблиці
data = np.array([
    [0.64, 0.74, 0.62, 0.56, 0.35, -0.09, -0.39],
    [0.44, 0.37, -0.06, -0.32, -0.6, -0.69, -0.67],
    [0.34, 0.05, 0.37, -0.3, -0.52, -0.72, 0.42],
    [0.23, 0.26, 0.35, 0.55, 0.49, 0.75, 0.48],
    [0.12, 0.4, -0.15, -0.08, 0.2, 0.43, 0.63],
    [-0.26, -0.22, -0.15, 0.03, 0.2, 0.61, 0.67],
    [0.22, 0.29, -0.38, -0.34, 0.1, 0.4, 0.56],
    [-0.26, -0.69, -0.7, -0.53, -0.43, -0.22, 0.29],
    [-0.35, -0.68, -0.62, -0.51, -0.56, -0.44, 0.18],
    [0.43, 0.13, 0.75, 0.84, 0.78, 0.73, 0.71],
    [0.59, 0.4, 0.6, 0.16, 0.12, 0.18, 0.33],
    [0.38, -0.79, -0.56, -0.39, -0.42, -0.58, -0.43]
])

# Обчислення середнього значення M
M = np.mean(data, axis=0)

# Побудова графіка середнього значення M
plt.figure(figsize=(10, 4))
plt.plot(M, marker='o')
plt.title('Середнє значення M')
plt.xlabel('Індекс')
plt.ylabel('M')
plt.grid(True)
plt.show()

# Обчислення дисперсії D
D = np.var(data, axis=0)

# Побудова таблиці дисперсії D
print("Таблиця значень дисперсії D:")
print(D)

# Обчислення кореляційної функції
def correlation_function(x, y):
    return np.correlate(x - np.mean(x), y - np.mean(y), mode='full') / (np.std(x) * np.std(y) * len(x))

correlation_matrix = np.array([[correlation_function(data[i], data[j]) for j in range(data.shape[0])] for i in range(data.shape[0])])

# Побудова графіка кореляційної функції
plt.figure(figsize=(10, 4))
for i in range(correlation_matrix.shape[0]):
    plt.plot(correlation_matrix[i], label=f'Кореляція з сигналом {i+1}')
plt.title('Кореляційна функція')
plt.xlabel('Зсув')
plt.ylabel('Кореляція')
plt.legend()
plt.grid(True)
plt.show()
