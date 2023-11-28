from scipy.stats import chi2_contingency

"""Resultados
Valor Estadistico Chi-cuadrado: 4.526243118294752
P: 0.03337881746687282
Grados de libertad: 1
No se rechaza la hipótesis nula
No hay suficiente evidencia para afirmar que el tiempo dedicado a ver televisión depende del género.
"""

data = [[15, 29],
        [27, 19]]

chi2, p, dof, expected = chi2_contingency(data)

nivel_significancia = 0.01

print(f"Valor Estadistico Chi-cuadrado: {chi2}")
print(f"P: {p}")
print(f"Grados de libertad: {dof}")

if p < nivel_significancia:
    print("Se rechaza la hipótesis nula\nHay evidencia suficiente para concluir que el tiempo dedicado a ver televisión no es independiente del género.")
else:
    print("No se rechaza la hipótesis nula\nNo hay suficiente evidencia para afirmar que el tiempo dedicado a ver televisión depende del género.")

