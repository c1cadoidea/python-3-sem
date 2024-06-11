import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Часові точки
t = [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4]

# Обчислення середнього значення m
m = np.mean(data, axis=0)

# Обчислення кореляційної функції
n = data.shape[0]
K = np.zeros((len(t), len(t)))

for i in range(len(t)):
    for j in range(len(t)):
        K[i, j] = np.mean(data[:, i] * data[:, j]) - m[i] * m[j]
        K[i, j] *= n / (n - 1)

# Створення DataFrame для зручності виводу
df_K = pd.DataFrame(K, index=t, columns=t)

print("Кореляційна функція K_x(t, t'):")
print(df_K)

# Побудова графіка
plt.figure(figsize=(10, 8))
sns.heatmap(df_K, annot=True, cmap="coolwarm", xticklabels=[str(i) for i in t], yticklabels=[str(i) for i in t])
plt.title("Кореляційна функція K_x(t, t')")
plt.xlabel("t'")
plt.ylabel("t")
plt.show()
