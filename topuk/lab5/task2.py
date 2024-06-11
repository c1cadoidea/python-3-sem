import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Параметри сигналу
B = 2       # Амплітуда імпульсу
tau = 5     # Ширина імпульсу

# Побудова часової області сигналу
t = np.linspace(-2*tau, 4*tau, 1000)
f_t = np.zeros_like(t)
f_t[(t >= -tau/3) & (t <= 3*tau)] = B

# Графік функції f(t)
plt.figure(figsize=(10, 4))
plt.plot(t, f_t, label='f(t)')
plt.title('Часова область сигналу')
plt.xlabel('Час (t)')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.legend()
plt.show()

# Спектральний аналіз сигналу
N = 1000  # Кількість точок для FFT
yf = fft(f_t, n=N)
xf = fftfreq(N, t[1] - t[0])

# Виділення тільки додатних частот
xf = xf[:N//2]
yf = np.abs(yf[:N//2]) # type: ignore

# Графік спектру сигналу
plt.figure(figsize=(10, 4))
plt.plot(xf, yf)
plt.title('Спектральна область сигналу')
plt.xlabel('Частота (Hz)')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.show()
