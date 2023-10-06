import numpy as np
from statsmodels.stats.proportion import proportion_confint

# Datos
x = 275  # Número de casas con dos o más televisores
n = 500  # Número total de casas

# Calcular el intervalo de confianza al 90%
conf_interval = proportion_confint(count=x, nobs=n, alpha=0.1, method='normal')

# Imprimir el intervalo de confianza
print("Intervalo de confianza del 90% para la proporción de casas con 2 o más TVs:")
print(conf_interval)
