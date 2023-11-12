import random 
import statistics as st #anade un apodo a statistics

poblacion = [1] * 300 + [2] * 700 + [3] * 4000 + [4] * 4000 + [5] * 1000 #generamos una poblacion por separada de cada numero
#generara 300 unos, luego 700 dos, 4000 tres y asi

m1=random.sample(poblacion,10)
m2=random.sample(poblacion,10)
m3=random.sample(poblacion,10)
m4=random.sample(poblacion,10)
m5=random.sample(poblacion,10)
#Tomara 5 muestras random de la poblacion sin remplazo

#a continaucion tomara la media de cada uno
media1=st.mean(m1)
media2=st.mean(m2)
media3=st.mean(m3)
media4=st.mean(m4)
media5=st.mean(m5)
#finalmente imprimira todo
print ("Muestra 1=", m1 ,"Media=", media1, "\n")
print ("Muestra 2=", m2 ,"Media=", media2, "\n")
print ("Muestra 1=", m3 ,"Media=", media3, "\n")
print ("Muestra 1=", m4 ,"Media=", media4, "\n")
print ("Muestra 1=", m5 ,"Media=", media5, "\n")
