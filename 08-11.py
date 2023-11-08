import numpy as np
import matplotlib.pyplot as plt

x = [ 17.3, 19.3, 19.5, 19.7, 22.9, 23.1, 26.4, 26.8, 27.6, 28.1, 28.2, 28.7, 29, 29.6, 29.9, 29.9, 30.3, 31.3, 36, 39.5, 40.4, 44.3, 44.6, 50.4, 55.9]
y = [ 71.7, 48.3, 88.3, 75, 91.7, 100, 73.3, 65, 75, 88.3, 68.3, 96.7, 76.7, 78.3, 60, 71.7, 85, 85, 88.3, 100, 100, 100, 91.7, 100, 71.7 ]

plt.scatter(x, y)
model = np.polyfit( x, y, 2) #CON EL NUM. 9 LE DECIMOS CON QUE POLINOMIO NOS QUEREMOS ENCONTRAR. LO CAMBIAMOS A 1.
print("MODELO LINEAL ", model)

#y con flecha arriba = 64.52+.56x ESA SERIA LA RESPUESTA DEL INCISO A.
#CUANDO X = 0, EL MODELO EMPEZARA EN 64. TENEMOS QUE EL COEFICIENTE ES POSITIVO, ES DECIR QUE ES UNA LINEA RECTA QUE VA A IR AUMENTANDO.
#ES DECIR, SE VA A IR YENDO PARA ARRIBA.
#LINEA DESDE 64 EN EJE Y, PARA ARRIBA.
#Y con flechita, (b). .56 * 30 + 64.52

#------
#Prediccion utilizando ploy1d
predict= np.poly1d(model)# predict va a contener los coeficientes

x_value=30
predict(x_value) #evaluar el modelo para x=x_value

from sklearn.metrics import r2_score
r2=r2_score(y, predict(x))

print("El valor de r_square es ", r2)
