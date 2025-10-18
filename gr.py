import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 200)

plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), 'r-', label='sen(x)')
plt.plot(x, np.cos(x), 'b-', label='cos(x)')
plt.plot(x, np.tan(x), 'g-', label='tan(x)', alpha=0.7)

plt.title('Funciones trigonométricas')
plt.xlabel('x (radianes)')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.ylim(-2, 2)  # Limitar el eje Y
plt.show()