import pandas
from sklearn import linear_model

datos=pandas.read_csv('drivers.csv')
print(datos)

datos.columns
datos.shape
x= datos[['Number of drivers involved in fatal collisions per billion miles', 'Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding']]
y= datos['Percentage Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired']

regr= linear_model.LinearRegression() #obtene el modelo de regresion

regr.fit(x, y) #Realiza el calculo de regresion lineal con los parametros
#print("MODELO", regr.fit)

r_sq = regr.score(x, y)
print("Coeficiente de determinacion: ", r_sq)

print("Intercepcion: ", regr.intercept_) #donde empieza la recta, cuando valen 0

print("Slope: ", regr.coef_)

predicted= regr.predict([[150000, 200500]])
print("Valor predicho: ", predicted)