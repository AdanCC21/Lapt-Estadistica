import random
import statistics as st #damos u napodo al statistics
calificaciones=range(0,101,1) #generamos rango
len(calificaciones) #leemos su longitud
poblacion=list(calificaciones) #convertimos una lista

n300=random.choices(poblacion,k=300) #imprtamos 300 numeros random con remplazo de la poblacion en n300
n=len(n300) #calculamos su longitud o por asi decirlo su anchura

media_n300=st.mean(n300) #Calculamos media
print("La media es= \n", media_n300)

dv_n300=st.stdev(n300) #calculamso desviacion estandar
print("su desviacion es \n", dv_n300)

z=2.575 #definimos z ya que trabajaremos con 99% de intervalo de confianza y su alpha es de 0.5

xinf=((media_n300)-(z)*((dv_n300)/(n**0.5))) #calculamos x inferior
xsup=((media_n300)+(z)*((dv_n300)/(n**0.5))) #calculamos x superior
rango_mu=xsup-xinf #restamos las dos x inferior y superior
print("Su valor final es =", rango_mu) #imprimimos resultados
 
#Repetimos pero esta vez con una poblacion de 1,000
calificaciones=range(0,101,1)
len(calificaciones)
poblacion=list(calificaciones)

n300=random.choices(poblacion,k=1000)
n=len(n300)

media_n300=st.mean(n300)
print("La media es= \n", media_n300)

dv_n300=st.stdev(n300)
print("su desviacion es \n", dv_n300)

z=2.575

xinf=((media_n300)-(z)*((dv_n300)/(n**0.5)))
xsup=((media_n300)+(z)*((dv_n300)/(n**0.5)))
rango_mu=xsup-xinf
print("Su valor final es =", rango_mu)

#Repetimos pero esta vez con una poblacion de 10,000
calificaciones=range(0,101,1)
len(calificaciones)
poblacion=list(calificaciones)

n300=random.choices(poblacion,k=10000)
n=len(n300)

media_n300=st.mean(n300)
print("La media es= \n", media_n300)

dv_n300=st.stdev(n300)
print("su desviacion es \n", dv_n300)

z=2.575

xinf=((media_n300)-(z)*((dv_n300)/(n**0.5)))
xsup=((media_n300)+(z)*((dv_n300)/(n**0.5)))
rango_mu=xsup-xinf
print("Su valor final es =", rango_mu)