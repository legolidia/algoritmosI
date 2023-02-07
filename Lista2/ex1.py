custo = float(input())
preco = float(input())

convites = int(custo/preco)

if(custo%preco!=0):
    convites = convites + 1

print(convites)

lucro = custo + (custo*0.23)

convites = int(lucro/preco)

if(lucro%preco!=0):
    convites = convites + 1   

print(convites)
