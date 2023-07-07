import matplotlib.pyplot as plt
import csv 

x = []
y = []

with open('tahun_2021.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[3])
        y.append(row[3])
plt.bar(x,y, color= 'b', width =0.55, label = "jumlah")
plt.title('JUMLAH GURU 2021')
plt.legend()
plt.show()