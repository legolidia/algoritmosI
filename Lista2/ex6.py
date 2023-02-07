preco = int(input())

N100 = (preco//100)
N50 = ((preco-(N100*100))//50)
N20 = ((preco-(N100*100)-(N50*50))//20)
N10 = ((preco-(N100*100)-(N50*50)-(N20*20))//10)
N5 = ((preco-(N100*100)-(N50*50)-(N20*20)-(N10*10))//5)
N2 = ((preco-(N100*100)-(N50*50)-(N20*20)-(N10*10)-(N5*5))//2)
N1 = (preco-(N100*100)-(N50*50)-(N20*20)-(N10*10)-(N5*5)-(N2*2))

if(N100!=0):
    print("%d nota(s) de R$ 100,00" %(N100))
if(N50!=0):
    print("%d nota(s) de R$ 50,00" %(N50))
if(N20!=0):
    print("%d nota(s) de R$ 20,00" %(N20))
if(N10!=0):
    print("%d nota(s) de R$ 10,00" %(N10))
if(N5!=0):
    print("%d nota(s) de R$ 5,00" %(N5))
if(N2!=0):
    print("%d nota(s) de R$ 2,00" %(N2))
if(N1!=0):
    print("%d nota(s) de R$ 1,00" %(N1))