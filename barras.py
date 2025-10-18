import matplotlib.pyplot as plt

# Datos para el gráfico de barras
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 45, 56, 12, 67]

plt.figure(figsize=(8, 6))
plt.bar(categorias, valores, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.show()