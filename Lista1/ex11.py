m2 = float(input())

litros = m2 / 3

if(litros <= 18):
    latas = 1
else:
    latas = litros//18 + 1

preco = latas * 80

print(latas, "%.2f" %preco)