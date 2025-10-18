import matplotlib.pyplot as plt
import numpy as np

# Datos aleatorios
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6, c='purple')
plt.title('Gráfico de dispersión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True)
plt.show()