#simule la calificacion de 300, 1000 y 10,000 estudiantes en un intervalo del 0 al 100, Calcule la media y desviacion estandar de la muestra, Despues el intervalo de confianza de 99%
#de las calificacion promedio de las calificaciones
#opinion
import random
import statistics as st
import math
z=0.005 #=99%
za=0.005/2
poblacion=range(0,300) #genera 300 valores
m1=random.sample(poblacion,100)#seleccioan 100
n=math.sqrt(100)
media=st.mean(m1)#media
desviacion=st.stdev(m1)#desviacion
fi=media-za*desviacion/n
fi2=media+za*desviacion/n
u=fi2-fi
print("Sus primeros valores seria\n")
print("Seria", fi, "<", u, "<", fi2, "\n")

##ahora con 1000
z=0.005 #=99%
za=0.005/2
poblacion=range(0,1000) #genera 1,000 valores
m1=random.sample(poblacion,100)#seleccioan 100
n=math.sqrt(100)
media=st.mean(m1)#media
desviacion=st.stdev(m1)#desviacion
fi2=media-za*desviacion/n
fi=media+za*desviacion/n
u=fi-fi2
print("Sus segundos valores seria\n")
print("Seria", fi, "<", u, "<", fi2, "\n")

##ahora con 10,000
z=0.005 #=99%
za=0.005/2
poblacion=range(0,10000) #genera 10,000 valores
m1=random.sample(poblacion,100)#seleccioan 100
n=math.sqrt(100)
media=st.mean(m1)#media
desviacion=st.stdev(m1)#desviacion
fi=media-za*desviacion/n
fi2=media+za*desviacion/n
u=fi2-fi
print("Sus terceros valores serian\n")
print("Seria", fi, "<", u, "<", fi2, "\n")