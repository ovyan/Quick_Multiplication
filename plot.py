import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import csv
from scipy.ndimage.filters import gaussian_filter1d

x = []
y = []
z = []

with open('out.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

ysmoothed = gaussian_filter1d(y, sigma=1)
zsmoothed = gaussian_filter1d(z, sigma=1)
plt.plot(x, zsmoothed, label='Divide and Conquer')
plt.plot(x, ysmoothed, label='School Multiplication')
plt.xlabel('Number of elements')
plt.ylabel('Time')
plt.title('School vs DaC')
plt.legend()
plt.show()