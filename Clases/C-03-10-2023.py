import pandas
from sklearn import linear_model

datos=pandas.read_csv('50_Startups.csv')
print(datos)

datos.columns
datos.shape
x= datos[['R&D Spend', 'Administration', 'Marketing Spend']]
y= datos['Profit']

regr= linear_model.LinearRegression() #obtene el modelo de regresion

regr.fit(x, y) #Realiza el calculo de regresion lineal con los parametros
#print("MODELO", regr.fit)

r_sq = regr.score(x, y)
print("Coeficiente de determinacion: ", r_sq)

print("Intercepcion: ", regr.intercept_) #donde empieza la recta, cuando valen 0

print("Slope: ", regr.coef_)

predicted= regr.predict([[150000, 200500, 345000]])
print("Valor predicho: ", predicted)