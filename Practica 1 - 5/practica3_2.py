import scipy.stats as stats
import math

desviacion_estandar = 0.0015 
tamaño_muestra = 75  
media_muestra = 0.310 
nivel_confianza = 0.95  

# Calcular el error estándar de la media
error_estandar_media = desviacion_estandar / math.sqrt(tamaño_muestra)

# Calcular el valor crítico de la distribución t de Student
grados_libertad = tamaño_muestra - 1
valor_critico = stats.t.ppf((1 + nivel_confianza) / 2, df=grados_libertad)

# Calcular el intervalo de confianza
intervalo_confianza = (
    media_muestra - valor_critico * error_estandar_media,
    media_muestra + valor_critico * error_estandar_media
)

# Imprimir el resultado
print(f"Intervalo de confianza del {nivel_confianza * 100}% para la media de profundidad:")
print(f"({intervalo_confianza[0]:.5f}, {intervalo_confianza[1]:.5f}) pulgadas")
