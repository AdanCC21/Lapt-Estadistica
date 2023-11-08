import pandas
from sklearn import linear_model

data = pandas.read_csv("heart.data_.cvs.csv")

x = data[['biking', 'smoking']] # SE ELIGEN LAS VARIABLES INDEPENDIENTES

y = data['heart.disease']
regression = linear_model.LinearRegression()

regression.fit(x, y)

r_sq = regression.score(x, y)
print('coeficient of determination: ', r_sq)
#
print('intercept: ', regression.intercept_)
#
print('slope: ', regression.coef_)
#

predictedDisease = regression.predict([[30.80124571, 10.89660802]])
print("Hearth Disease: ", predictedDisease)