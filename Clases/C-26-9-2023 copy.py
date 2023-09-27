from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt

x = [10, 10 , 10, 10, 10, 50, 50, 50, 50, 50]
y = [13, 18, 16, 15, 20, 86, 90, 88, 88, 92]
plt.scatter (x,y)
mymodel=np.poly1d(np.polyfit(x,y,1)) #GENERA EL POLINOMIO
print("Mi modelo ", mymodel)
predict= np.poly1d(mymodel)
x_value = 54
x_54 = predict(x_value)
print("Valor de Y para X=54 ",x_54)

r0 = r2_score(y,predict(x)) #EL VALOR DEL COEFICIENTE DE DETERMINACION
                            #INDICA HACIA DONDE TIENDE LA PREDICCION DEPENDIENDO SI + O -\
    
print("El valor de r_square es", r0)

#Si los residuos siguen una distribucion normal de cuanto deberia ser la media? Cuando la media es igual a la moda y la mediana