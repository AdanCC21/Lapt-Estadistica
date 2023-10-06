"""27/09/2023
Practica 6 y 7 del manual con los sigsuientes datos"""

"""Encontrar el mejor modelo,
Reportar el codigo, el r al cuadrado obtenido
Graficar el histograma de los error
La media del error, la desviacion estandar del error
concluir si los errores se aproximan a una distribucion normal"""

import numpy as np
import matplotlib.pyplot as plt

# Datos
y = [790, 1160, 929, 865, 1140, 929, 1109, 1365, 1112, 1150, 980, 990, 1112, 1252, 1326, 1330, 1365, 1280, 1119, 1328, 1584, 1428, 1365, 1415, 1415, 1465, 1490, 1725, 1523, 1705, 1605, 1746, 1235, 1390, 1405, 1395]
x = [99, 95, 95, 90, 105, 105, 90, 92, 98, 99, 99, 101, 99, 94, 97, 97, 99, 104, 104, 105, 94, 99, 99, 99, 99, 102, 104, 114, 109, 114, 115, 117, 104, 108, 109, 120]

# Convierte las listas en arrays de NumPy
x = np.array(x)
y = np.array(y)

# Función para calcular el coeficiente de determinación (R al cuadrado)
def r_squared(y_true, y_pred):
    ssr = np.sum((y_true - y_pred) ** 2)
    sst = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ssr / sst)

# Realiza la regresión lineal
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)

# Calcula el coeficiente de determinación (R al cuadrado)
y_pred = poly(x)
r2 = r_squared(y, y_pred)
print(f"Coeficiente de determinación (R^2): {r2}")

# Calcula los errores
errors = y - y_pred

# Grafica el histograma de errores
plt.hist(errors, bins=10, edgecolor='k')
plt.xlabel('Errores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Errores')
plt.show()

# Calcula la media y la desviación estándar de los errores
mean_error = np.mean(errors)
std_error = np.std(errors)
print(f"Media del error: {mean_error}")
print(f"Desviación estándar del error: {std_error}")
