import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(-10, 20, 100)  # 100 puntos entre -10 y 20
y = x**2  # Función cuadrática

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y = x²')
plt.title('Gráfico de una función cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()