Regresion Lineal Calculador
¡Si hubiera tenido esto antes, me habría ahorrado mucho dolor en estadística inferencial!

Descripción
Este proyecto utiliza Python para realizar una regresión lineal sobre datos de ejemplo, generando una gráfica y calculando el coeficiente de determinación 
𝑅
2
R 
2
 .

Pasos
1. Importación de Bibliotecas
Importamos las siguientes bibliotecas necesarias:

numpy: Para operaciones matemáticas.
matplotlib.pyplot: Para graficar los datos y la línea de regresión.
LinearRegression de scikit-learn: Para crear y entrenar el modelo de regresión lineal.
python
Copiar código
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
2. Datos de Ejemplo
Definimos datos de ejemplo para la regresión lineal. Puedes reemplazar X y y con tus propios datos.

python
Copiar código
# Ejemplo de datos
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3.5, 3.6, 4.1, 5.0])
3. Modelo de Regresión Lineal
Creamos una instancia de LinearRegression y ajustamos el modelo a nuestros datos.

python
Copiar código
model = LinearRegression()
model.fit(X, y)
4. Predicciones
Usamos el modelo entrenado para hacer predicciones sobre los datos de entrada X.

python
Copiar código
y_pred = model.predict(X)
5. Gráfica
Creamos una gráfica usando matplotlib que muestra los datos reales como puntos azules y la línea de regresión como una línea roja.

python
Copiar código
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred, color='red', linewidth=2, label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.legend()
plt.grid(True)
6. Guardado de la Gráfica
Guardamos la gráfica como un archivo .png.

python
Copiar código
plt.savefig('regression_plot.png')
7. Resultados
Calculamos el coeficiente de determinación 
𝑅
2
R 
2
  y lo imprimimos en la consola.

python
Copiar código
r2 = model.score(X, y)
print(f'Coeficiente de determinación R^2: {r2}')
8. Generación de HTML
Creamos un contenido HTML que incluye la gráfica y los resultados.

python
Copiar código
html_content = f'''
<!DOCTYPE html>
<html>
<head>
  <title>Resultados de Regresión Lineal</title>
</head>
<body>
  <h2>Gráfica de Regresión Lineal</h2>
  <img src="regression_plot.png" alt="Gráfica de Regresión Lineal">
  <h2>Coeficiente de determinación R^2</h2>
  <img src="regression_plot.png" alt="![image](https://github.com/Dahakablue/RegresionLinealCalculador/assets/72954658/56a95cae-5117-4c70-9c81-3a8151e362b7)
">
  <p>{r2}</p>
</body>
</html>
'''

# Guardado del archivo HTML
with open('regression_results.html', 'w') as f:
    f.write(html_content)

print('Archivo HTML guardado exitosamente: regression_results.html')

