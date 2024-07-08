# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo (puedes cambiar estos datos por los tuyos)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Variables independientes
y = np.array([2, 3, 4, 5, 6])               # Variable dependiente

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Hacer predicciones
y_pred = model.predict(X)

# Calcular métricas de rendimiento (en este caso, el coeficiente de determinación R^2)
r2_score = model.score(X, y)

# Generar la gráfica
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regresión lineal')
plt.title('Regresión Lineal')
plt.xlabel('Variable independiente')
plt.ylabel('Variable dependiente')
plt.legend()
plt.grid(True)

# Guardar la gráfica en un archivo HTML
plt.savefig('regression_plot.png')

# Mostrar los resultados
print(f'Coeficiente de determinación R^2: {r2_score}')

# Cerrar la figura de matplotlib para evitar que se muestre en la terminal
plt.close()

# Generar HTML para mostrar la gráfica y los resultados
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Resultados de Regresión Lineal</title>
</head>
<body>
    <h2>Gráfica de Regresión Lineal</h2>
    <img src="regression_plot.png" alt="Gráfica de Regresión Lineal" width="600" height="450">
    <h3>Resultados:</h3>
    <p>Coeficiente de determinación R^2: {r2_score}</p>
</body>
</html>
"""

# Guardar el contenido HTML en un archivo
with open('regression_results.html', 'w') as file:
    file.write(html_content)

# Mostrar mensaje de éxito
print('Se han guardado los resultados en regression_results.html')
