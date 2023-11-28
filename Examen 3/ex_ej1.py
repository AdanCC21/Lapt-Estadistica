import numpy as np
from scipy.stats import norm, chi2

""" Resultados Ej1
F observadas: [ 8  9 25 18]
F esperadas: [ 6.95678199 17.33843836 21.39426744 11.38409459]       
Valor Estadistico Chi-cuadrado: 8.619133711244526
Grados de libertad: 3
Valor crítico de chi-cuadrado: 7.814727903251179
Se rechaza la hipótesis nula
Hay evidencia de que las frecuencias observadas y esperadas difieren.
"""

datos = np.array([23, 60, 79, 32, 57, 74, 52, 70, 82, 36, 80, 77, 81, 95, 41, 65, 92, 85, 55, 76, 52,
                  10, 64, 75, 78, 25, 80, 98, 81, 67, 41, 71, 83, 54, 64, 72, 88, 62, 74, 43, 60, 78,
                  89, 76, 84, 48, 84, 90, 15, 79, 34, 67, 17, 82, 69, 74, 63, 80, 85, 61])
mu = 65
sigma = 21


intervalos = [0, 40, 60, 80, 100]
frecuencias_observadas, bordes = np.histogram(datos, bins=intervalos)

prob_acum = np.diff(norm.cdf(bordes, loc=mu, scale=sigma))
frecuencias_esperadas = len(datos) * prob_acum

chi_cuadrado = np.sum((frecuencias_observadas - frecuencias_esperadas)**2 / frecuencias_esperadas)
grados_libertad = len(intervalos) - 2

valor_critico = chi2.ppf(0.95, grados_libertad)

print(f"F observadas: {frecuencias_observadas}")
print(f"F esperadas: {frecuencias_esperadas}")
print(f"Valor Estadistico Chi-cuadrado: {chi_cuadrado}")
print(f"Grados de libertad: {grados_libertad}")
print(f"Valor crítico de chi-cuadrado: {valor_critico}")

if chi_cuadrado > valor_critico:
    print("Se rechaza la hipótesis nula\nHay evidencia de que las frecuencias observadas y esperadas difieren.")
else:
    print("No hay suficiente evidencia para rechazar la hipótesis nula.")