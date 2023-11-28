import numpy as np
from scipy.stats import f_oneway

"""Resultados EJ3S
ANOVA: 6.5865080964859235
P: 0.001497104486931074
Se rechaza la hipótesis nula
Hay evidencia de que las marcas proporcionan diferentes números medios de horas de alivio.
"""

tabla_data = np.array([
    [5.2, 9.1, 3.2, 2.4, 7.1],
    [4.7, 7.1, 5.8, 3.4, 6.6],
    [8.1, 8.2, 2.2, 4.1, 9.3],
    [6.2, 6.0, 3.1, 1.0, 4.2],
    [3.0, 9.1, 7.2, 4.0, 7.6]
])

statistic, p_value = f_oneway(*tabla_data.T)

nivel_significancia = 0.05

print(f"ANOVA: {statistic}")
print(f"P: {p_value}")

if p_value < nivel_significancia:
    print("Se rechaza la hipótesis nula\nHay evidencia de que las marcas proporcionan diferentes números medios de horas de alivio.")
else:
    print("No hay suficiente evidencia para rechazar la hipótesis nula\nNo hay diferencias significativas entre las marcas en términos del número medio de horas de alivio.")

