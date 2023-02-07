sm = float(input())
qtd = float(input())

valor = (sm*0.02*qtd)/1000

print("R$%.2f" %valor)

desconto = valor-(valor*0.15)

print("R$%.2f" %desconto)