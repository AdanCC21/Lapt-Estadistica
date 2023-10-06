import random
import matplotlib.pyplot as plt #generamos un apodo a matplotlib.pyplot, esta libreria ayuda a generar graficas de dos dimensiones o histogramas

# Crear una lista para almacenar las calificaciones
calif = []

# Generar 300 calificaciones aleatorias entre 0 y 100
for _ in range(300): #Se le coloca un "_' Porque indicamos que la variable no se utilizara en el bloque de codigo. Solo repetira 300 veces lo que este dentro
    calificaciones = random.randint(0, 101) #generamos un numero desde el 0 al 101, el random.randint hace diferencia ya que generara numeros de a a b, incluyendo estos
    calif.append(calificaciones) #Ya generando la calificacion, se pondra cada calificacion al final de la lista, y asi evitando sustituir un valor de la 1ra posicion de la lista

# Crear un histograma con 20 barras para las calificaciones generadas
plt.hist(calif, bins=20, edgecolor='black') #la lista que usara, bins es el número de barras en el histograma o como los saltos que dara entre valores por ejemplo, la calif del 0 al 20 del 20 al 40 y asi, color
plt.title('Histograma de Calificaciones')  #titulo
plt.xlabel('Calificaciones') #barra horizontal
plt.ylabel('Frecuencia') #barra lateral
plt.show() #mostramos como imagen

#Repetimos ahora con rango de 1000
calif = []

for _ in range(1000):
    calificaciones = random.randint(0, 101)
    calif.append(calificaciones)

plt.hist(calif, bins=20, edgecolor='black')
plt.title('Histograma de Calificaciones')
plt.xlabel('Calificaciones')
plt.ylabel('Frecuencia')
plt.show()

#repetimos ahora con rango de 10,000
calif = []

for _ in range(10000):
    calificaciones = random.randint(0, 101)
    calif.append(calificaciones)

plt.hist(calif, bins=20, edgecolor='black')
plt.title('Histograma de Calificaciones')
plt.xlabel('Calificaciones')
plt.ylabel('Frecuencia')
plt.show()