import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'año': [1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638],
    'niños': [5218, 4858, 4422, 4994, 5158, 5035, 5106, 4917, 4703, 5359],
    'niñas': [4683, 4457, 4102, 4590, 4841, 4912, 4928, 4783, 4661, 5473]
}

data = pd.DataFrame(datos)

# 1. Graficar los nacimientos de hombres y mujeres a lo largo de los años
plt.figure(figsize=(12, 6))
plt.plot(data['año'], data['niños'], label='Niños')
plt.plot(data['año'], data['niñas'], label='Niñas')
plt.xlabel('Año')
plt.ylabel('Nacimientos')
plt.title('Nacimientos de Hombres y Mujeres a lo largo de los Años')
plt.legend()
plt.show()

# 2. Agregar una cuarta columna que muestre el total de nacimientos
data['total_nacimientos'] = data['niños'] + data['niñas']

# 3. Agregar una quinta columna que muestre la proporción de hombres del total de nacimientos
data['prop_hombres'] = data['niños'] / data['total_nacimientos']

# 4. Agregar una sexta columna que muestre la proporción de mujeres del total de nacimientos
data['prop_mujeres'] = data['niñas'] / data['total_nacimientos']

# 5. Agregar una séptima columna con la comparación prop_hombre > prop_mujeres
data['comparacion'] = data['prop_hombres'] > data['prop_mujeres']

# Imprimir el DataFrame resultante
print(data)
