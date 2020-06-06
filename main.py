import numpy as np
import matplotlib.pyplot as plt

f = open("values.txt", "r") 
f.readline()
x = []
y = []

for line in f:
  x.append(float(line.split('\t')[1]))
  y.append(float(line.split('\t')[0]))

plt.plot(x,y)
plt.xlabel('Radius(kpc)')
plt.ylabel('Velocity(km/h)')
plt.show()

