import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

rekreasi = pd.read_csv('data usaha.csv')

data2 = rekreasi['kecamatan'].value_counts()

fig = plt.figure()
x = data2.index
y = data2.values 
plt.bar(x,y,color = 'green' , width=0.6)
plt.xticks(rotation = 90)
plt.xlabel('kecamatan')
plt.ylabel('value')
plt.title('banyak kecamatan yang memiliki jenis usaha di jakarta')
plt