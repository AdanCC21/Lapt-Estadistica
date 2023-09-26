"""Clase 26/09/2023, Numpy pylyfit, checa fotos maybe ayudan"""
import numpy as np
import matplotlib.pyplot as plt

x=[28,8,11,37,15,25,51,11,32,34,43,2,40,16,40,25,40,17,21,57]
y=[8,8,9,72,22,51,85,4,75,48,72,1,62,37,75,42,75,47,57,95]

plt.scatter(x,y)

model= np.polyfit(x,y,9) #Grado del polinomio

print("modelo lineal",model);

preditc = np.poly1d(model)

x_valvue = 20
preditct(x_valvue)

#para x=20 cuanto vale y

from sklearn.mtrics import r2_score
r2=r2_score(y,preditc(x))

print("El valor de r_square es ",r2);

x_axis=range(0,60)
y_axis=preditc(x_axis)
plt.scatter(x,y)
plt.plot(x_axis, y_axis, c= 'g')

mymodel=np.poly1d(no.polyfit(x,y,3))

print("Mi modelo",mymodel)
predict = np.poly1d(mymodel)

x_valvue = 20
x_20=predict(x_valvue)
print("valor dey para x=20 es ",x_20)
#Trabajo encontrar r2 para grador de polinomio 3???