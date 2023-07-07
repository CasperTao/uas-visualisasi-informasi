import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

rekreasi = pd.read_csv('data usaha.csv')

data1 = rekreasi['jenis_usaha'].value_counts()

fig = plt.figure()
x = data1.index
y = data1.values 
plt.bar(x,y,color = 'purple' , width=0.6)
plt.xticks(rotation = 90)
plt.xlabel('jenis usaha')
plt.ylabel('value')
plt.title('banyak jenis usaha di jakarta')
plt