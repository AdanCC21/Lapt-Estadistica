import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#altura en centímetros
altura_hombres = np.array([175, 180, 170, 185, 178, 172, 188, 182, 177, 169])
altura_mujeres = np.array([162, 165, 160, 168, 158, 163, 166, 164, 159, 161])

# Calcular la media y la desviación estándar de las alturas para hombres y mujeres
media_hombres = np.mean(altura_hombres)
desviacion_hombres = np.std(altura_hombres, ddof=1)  # Usar ddof=1 para calcular la desviación estándar muestral
media_mujeres = np.mean(altura_mujeres)
desviacion_mujeres = np.std(altura_mujeres, ddof=1)

# Tamaño de las muestras
n_hombres = len(altura_hombres)
n_mujeres = len(altura_mujeres)

# Nivel de confianza
confianza = 0.95

# Calcular el intervalo de confianza para la diferencia de medias
diferencia_medias = media_hombres - media_mujeres
error_estandar = np.sqrt((desviacion_hombres**2 / n_hombres) + (desviacion_mujeres**2 / n_mujeres))
margen_error = stats.t.ppf((1 + confianza) / 2, df=(n_hombres + n_mujeres - 2)) * error_estandar
intervalo_confianza = (diferencia_medias - margen_error, diferencia_medias + margen_error)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(altura_hombres, bins=10, alpha=0.5, color='blue', label='Hombres')
plt.hist(altura_mujeres, bins=10, alpha=0.5, color='red', label='Mujeres')
plt.title('Histograma de Alturas')
plt.xlabel('Altura (cm)')
plt.ylabel('Frecuencia')
plt.legend()

plt.subplot(1, 2, 2)
plt.bar(['Diferencia de Medias'], [diferencia_medias], yerr=margen_error, color='green', alpha=0.7)
plt.title('Diferencia de Medias con Intervalo de Confianza')
plt.xlabel('Diferencia de Medias')
plt.ylabel('Intervalo de Confianza')

plt.tight_layout()
plt.show()

# Imprimir el resultado
print("Diferencia de medias:", diferencia_medias)
print("Intervalo de confianza al {}%:".format(int(confianza * 100)), intervalo_confianza)

