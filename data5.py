import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

data = pd.read_csv('data usaha.csv')

grouped_data = data.groupby(['kecamatan' , 'wilayah']).size().unstack().fillna(0)

grouped_data.plot(kind='bar',stacked=True)
plt.xlabel('kecamatan')
plt.ylabel('jumlah usaha')
plt.title('sebaran kecamatan yang meiliki jenis usaha pada setiap wilayahnya')
plt.legend(title='jenis usaha')
plt