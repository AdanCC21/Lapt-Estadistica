import random 
import statistics as st

# PoblaciÃ³n de productividad
poblacion = [1] * 300 + [2] * 700 + [3] * 4000 + [4] * 4000 + [5] * 1000

# muestras
m1=random.sample(poblacion,10)
m2=random.sample(poblacion,10)
m3=random.sample(poblacion,10)
m4=random.sample(poblacion,10)
m5=random.sample(poblacion,10)

# calcular la media muestral
media1=st.mean(m1)
media2=st.mean(m2)
media3=st.mean(m3)
media4=st.mean(m4)
media5=st.mean(m5)

# imprimir resultados
print ("Muestra 1=", m1 ,"Media=", media1, "\n")
print ("Muestra 2=", m2 ,"Media=", media2, "\n")
print ("Muestra 1=", m3 ,"Media=", media3, "\n")
print ("Muestra 1=", m4 ,"Media=", media4, "\n")
print ("Muestra 1=", m5 ,"Media=", media5, "\n")