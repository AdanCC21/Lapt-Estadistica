
from scipy import stats

#Tamb se puede hacer con numpy dice

import matplotlib.pyplot as plt
datos=[2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3, 2.6,
       3.4, 1.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7,
       2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1,
       3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 1.9, 3.4,
       4.7, 3.8, 3.2, 2.6, 3.9, 3, 4.2, 3.5]

plt.hist(datos,bins=7)
res = stats.normaltest(datos)
res.statistic

# Out[5]: 1.5096401543334301

res.pvalue
# Out[6]: 0.4700951879801155

