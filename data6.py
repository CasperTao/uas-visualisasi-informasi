import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

data = pd.read_csv('data usaha.csv')

grouped_data = data.groupby(['wilayah' , 'jenis_usaha']).size().unstack().fillna(0)

grouped_data.plot(kind='bar',stacked=True)
plt.xlabel('wilayah')
plt.ylabel('jumlah usaha')
plt.title('sebaran jenis usaha yang ada di setiap wilayah')
plt.legend(title='jenis usaha')
plt
