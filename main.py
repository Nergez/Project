import math
import numpy as np 

f = open('values.txt' , 'r')
f.readline()
r = []
Mc = []
for line in f:
  r.append(float(line.split('\t')[0]))

x = 4*(math.pi)*(100*(10**6))*((1.87)**2)

for i in r:
  atan = math.atan(i/(1.87))
  equation1 = i-((1.87)*(atan))
  equation = (x)*(equation1)
  Mc.append(equation)

print(Mc) 
