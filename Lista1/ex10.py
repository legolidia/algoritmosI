salario = float(input())
aumento = float(input())

novoSalario = salario + (salario * aumento / 100)

print("R$ %.2f" %novoSalario)