from math import pow 
n = int (input ())
m = int (input ())
s = 0 
for i in range (1, n+1):
  for j in range (1, m+1):
    s = s + ((pow (i, 2) * j) / (pow (3, i) * (j * pow (3, i) + i * pow (3, j)))) 

print (s)
