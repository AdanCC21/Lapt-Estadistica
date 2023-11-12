# Importa las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas as pd

# Datos de muestra
y = [790, 1160, 929, 865, 1140, 929, 1109, 1365, 1112, 1150, 980, 990, 1112, 1252, 1326, 1330, 1365, 1280, 1119, 1328, 1584, 1428, 1365, 1415, 1415, 1465, 1490, 1725, 1523, 1705, 1605, 1746, 1235, 1390, 1405, 1395]
x = [99, 95, 95, 90, 105, 105, 90, 92, 98, 99, 99, 101, 99, 94, 97, 97, 99, 104, 104, 105, 94, 99, 99, 99, 99, 102, 104, 114, 109, 114, 115, 117, 104, 108, 109, 120]

# Ajustar un polinomio de grado 9 a los datos
model = np.polyfit(x, y, 9)

# Crear una función polinómica a partir del modelo ajustado
predict = np.poly1d(model)

# Predecir los valores ajustados
y_pred_all = predict(x)

# Calcular el coeficiente de determinación (R cuadrado)
r2 = r2_score(y, y_pred_all)
print("Resultado de r cuadrada: ", r2)

# Generar valores en el rango de 90 a 120 para la línea de regresión
x_axis = range(90, 120)
y_axis = predict(x_axis)

# Crear un gráfico de dispersión de los datos y trazar la línea de regresión
plt.scatter(x, y)
plt.plot(x_axis, y_axis, c="g")

# Calcular los errores
errores = []
for i in y:
    errores = y - predict(x)
print("errores", errores)

# Calcular la media de los errores
media_error = np.mean(errores)
print("media: ", media_error)

# Calcular la desviación estándar de los errores
ds_error = np.std(errores)
print("Desviación estándar de los errores = ", ds_error)

# Crear un histograma de los errores
plt.figure()
plt.title("Histograma de Errores")
plt.xlabel("Error")
plt.ylabel("Frecuencia")
plt.hist(errores, bins=20)
plt.show()
