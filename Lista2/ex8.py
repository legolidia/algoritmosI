import math

n1 = int(input())
n2 = int(input())
n3 = int(input())

somaQuadrados = int(math.pow(n1,2) + math.pow(n2, 2) + math.pow(n3, 2))
quadradoSoma = int(math.pow((n1 + n2 + n3),2))

print(somaQuadrados)
print(quadradoSoma)