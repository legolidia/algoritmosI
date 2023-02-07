preco = int(input())

n100 = preco//100
n50 = (preco%100)//50
n20 = ((preco%100)%50)//20
n10 = (((preco%100)%50)%20)//10
n5 = ((((preco%100)%50)%20)%10)//5
n2 = (((((preco%100)%50)%20)%10)%5)//2

print("%d nota(s) de R$ 100,00" %(n100))
print("%d nota(s) de R$ 50,00" %(n50))
print("%d nota(s) de R$ 20,00" %(n20))
print("%d nota(s) de R$ 10,00" %(n10))
print("%d nota(s) de R$ 5,00" %(n5))
print("%d nota(s) de R$ 2,00" %(n2))