import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv('data.csv')
table.head()
fig = plt.figure()
wilayah = table['wilayah']
wilayah.value_counts().plot(kind='pie')
fig
