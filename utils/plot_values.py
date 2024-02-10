import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

trade_values=[]
fil = open('./trade_values_change_mar20.csv', 'r')
reader = csv.reader(fil)

for row in reader:
    trade_values.append(float(row[0].replace("'","")))

y = np.fromstring( str(trade_values)[1:-1], dtype=np.float, sep=',' )
plt.plot(y)
plt.show()