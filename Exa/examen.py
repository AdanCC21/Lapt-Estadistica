import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("heart.data_.cvs.csv")

x = data[['biking', 'smoking']]
y = data['heart.disease']

regression = LinearRegression()
regression.fit(x, y)

# Media
media_biking = x['biking'].mean()
media_smoking = x['smoking'].mean()
print("media biking= ", media_biking," media smoking= ", media_smoking)

predVal = regression.predict([[media_biking, media_smoking]])
print("Valor predicho:", predVal)

#(R^2)
r_sq = regression.score(x, y)
print('Coeficiente de determinación: ', r_sq)

# Intercepto y coeficientes de la regresión
print('Intercepto: ', regression.intercept_)
print('Coeficientes: ', regression.coef_)

# Ecuación del modelo
intercepto = regression.intercept_
coefs = regression.coef_
print(f'Modelo de regresión: heart_disease = {intercepto:.4f} + {coefs[0]:.4f} * biking + {coefs[1]:.4f} * smoking')

# Realiza una predicción para nuevos datos
predicted_disease = regression.predict([[30.80124571, 10.89660802]])
print("Enfermedad Cardíaca (predicción): ", predicted_disease)

# Medias de las variables independientes
biking_mean = data['biking'].mean()
smoking_mean = data['smoking'].mean()

# Proyección utilizando el modelo
proyeccion_heart_disease = intercepto - 0.2001 * biking_mean + 0.1783 * smoking_mean

print(f'Proyección de heart_disease para medias: {proyeccion_heart_disease:.4f}')