from statistics import multimode, mode

presidentes = []
governadores = []
prefeitos = []
eleitores = []
eleitoresQueVotaram = []
partidosEleitos = []

votosBrancosPresidente = 0
votosBrancosGovernador = 0
votosBrancosPrefeito = 0

votosNulosPresidente = 0
votosNulosGovernador = 0
votosNulosPrefeito = 0

votosTotaisPresidente = 2
votosTotaisGovernador = 2
votosTotaisPrefeito = 2

presidentes.append(["Jose", 123, "PSD", "Presidente", 0])
presidentes.append(["Maria", 124, "PST", "Presidente", 0])
governadores.append(["Mario", 256, "PST", "Governador", 0])
governadores.append(["Carla", 281, "PSD", "Governador", 0])
prefeitos.append(["Antonio", 456, "PEF", "Prefeito", 0])
prefeitos.append(["Marta", 499, "PSD", "Prefeito", 0])

eleitores.append(["Ariel", "1234", False])
eleitores.append(["Marcos", "5678", False])
eleitores.append(["Carla", "7654", False])
eleitores.append(["Monica", "9356", False])
eleitores.append(["Manoel", "3567", False])
eleitores.append(["Joao", "5556", False])

def menu():
    print("+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++")
    print()
    print("     1. Cadastrar Candidatos")
    print("     2. Cadastrar Eleitores")
    print("     3. Votar")
    print("     4. Apurar Resultados")
    print("     5. Relatório e Estatísticas")
    print("     6. Encerrar")
    op = int(input("\nOpção escolhida:")) 
    while(op<1 and op>6):
            input("Inválido. Digite um valor diferente.")
    if op==1:
        cadastraCandidato()
    elif op==2:
        cadastraEleitores()
    elif op==3:
        computaVoto()
    elif op==4:
        if votosTotaisGovernador==0 or votosTotaisPrefeito==0 or votosTotaisPresidente==0:
            print("Não é possível exibir a apuração pois nenhum voto foi computado.")
            input("Aperte qualquer tecla para continuar.")
            menu()
        else:
            exibeVotos()
    elif op==5:
        if votosTotaisGovernador==0 or votosTotaisPrefeito==0 or votosBrancosPresidente==0:
            print("Não é possível exibir estatísticas pois nenhum voto foi computado.")
            input("Aperte qualquer tecla para continuar.")
            menu()
        else:
            exibeRelatorioEstatisticas()
    else:
        breakpoint        

def cadastraCandidato():
    print("Informe os dados do candidato.")
    nome = input("Nome: ")
    numero = int(input("Número: "))
    partido = input("Partido: ")
    votos = 0
    print("Informe o cargo para qual está concorrendo: ")
    print("1 - Presidente | 2 - Governador | 3 - Prefeito")
    cargo = int(input())
    if cargo==1:
        presidentes.append([nome, numero, partido, "Presidente", votos])
    elif cargo==2:
        governadores.append([nome, numero, partido, "Governador", votos])     
    else:
        prefeitos.append([nome, numero, partido, "Prefeito", votos])       
    continuar = input("Deseja cadastrar outro candidato? y/n: ")
    if(continuar=='y'):
        cadastraCandidato()
    else:
        menu()

def cadastraEleitores():
    print("Informe os dados do eleitor.")
    nome = input("Nome: ")
    cpf = input("Digite o cpf: ")
    jaVotou = False
    eleitores.append([nome, cpf, jaVotou])
    continuar = input("Deseja cadastrar outro eleitor? y/n: ")
    if(continuar=='y'):
        cadastraEleitores()
    else:
            menu()

def computaVoto():
    global votosBrancosPresidente 
    global votosBrancosGovernador 
    global votosBrancosPrefeito 

    global votosNulosPresidente
    global votosNulosGovernador
    global votosNulosPrefeito 

    global votosTotaisPresidente 
    global votosTotaisGovernador
    global votosTotaisPrefeito 

    print("+++++++++++ VOTAÇÃO +++++++++++++")
    numCPF = input("Informe o CPF do eleitor: ")
    while(numCPF!=1):
        for i in range(0, len(eleitores)):
           if eleitores[i][1]==numCPF:
            print(eleitores[i][0])
            if eleitores[i][2]==True:
                print("Esse eleitor já votou, informe outro CPF.")
                numCPF = input("Informe o CPF do eleitor: ")
            else:
                cpf = numCPF
                idEleitor = i
                numCPF = 1

    print("Voto branco: digitar -1 | Voto nulo: digitar -2")

    numPrefeito = int(input("Informe o número do prefeito: "))
    if numPrefeito == -1:
        votosBrancosPrefeito+=1
        votosTotaisPrefeito+=1
    elif numPrefeito ==-2:
        votosNulosPrefeito+=1
        votosTotaisPrefeito+=1
    else:
        while(numPrefeito>0):
            if numPrefeito == -1:
                votosBrancosPrefeito+=1
                votosTotaisPrefeito+=1
            elif numPrefeito ==-2:
                votosNulosPrefeito+=1
                votosTotaisPrefeito+=1
            for i in range(0, len(prefeitos)):
                if prefeitos[i][1]==numPrefeito:
                    for j in range(0,4):
                        print(prefeitos[i][j])
                    confirma = input("Confirmar voto? y/n: ")
                    if(confirma=='y'):
                        prefeitos[i][4]+=1
                        votosTotaisPrefeito+=1
                        numPrefeito = 0
                    else:
                        numPrefeito = int(input("Informe o número do prefeito: "))

    numGovernador = int(input("Informe o número do governador: "))
    if numGovernador == -1:
        votosBrancosGovernador = votosBrancosGovernador + 1
        votosTotaisGovernador+=1
    elif numGovernador ==-2:
        votosNulosGovernador+=1
        votosTotaisGovernador+=1
    else:
        while(numGovernador>0):
            if numGovernador == -1:
                votosBrancosGovernador+=1
                votosTotaisGovernador+=1
            elif numGovernador ==-2:
                votosNulosGovernador+=1
                votosTotaisGovernador+=1
            for i in range(0, len(governadores)):
                if governadores[i][1]==numGovernador:
                    for j in range(0,4):
                        print(governadores[i][j])
                    confirma = input("Confirmar voto? y/n: ")
                    if(confirma=='y'):
                        governadores[i][4]+=1
                        votosTotaisGovernador+=1
                        numGovernador = 0
                    else:
                        print("Voto branco: digitar -1 | Voto nulo: digitar -2")
                        numGovernador = int(input("Informe o número do governador: "))

    numPresidente = int(input("Informe o número do presidente: "))
    if numPresidente == -1:
        votosBrancosPresidente+=1
        votosTotaisPresidente+=1
    elif numPresidente ==-2:
        votosNulosPresidente+=1
        votosTotaisPresidente+=1
    else:
        while(numPresidente>0):
            if numPresidente == -1:
                votosBrancosPresidente+=1
                votosTotaisPresidente+=1
            elif numPresidente ==-2:
                votosNulosPresidente+=1
                votosTotaisPresidente+=1
            for i in range(0, len(presidentes)):
                if presidentes[i][1]==numPresidente:
                    for j in range(0,4):
                        print(presidentes[i][j])
                    confirma = input("Confirmar voto? y/n: ")
                    if(confirma=='y'):
                        presidentes[i][4]+=1
                        votosTotaisPresidente+=1
                        numPresidente = 0
                    else:
                        print("Voto branco: digitar -1 | Voto nulo: digitar -2")
                        numPresidente = int(input("Informe o número do presidente: "))

    print("VOTO CONFIRMADO!")

    eleitoresQueVotaram.append(eleitores[idEleitor][0])
    eleitores[idEleitor][2]=True

    input("Aperte qualquer tecla para voltar ao menu.")
    menu()   

def exibeVotos():

    selectionSort(presidentes)

    votosValidosPresidente = votosTotaisPresidente-votosBrancosPresidente-votosNulosPresidente
    votosValidosPresPorc = (votosValidosPresidente/votosTotaisPresidente)*100 

    print("\nPresidentes: ")
    for i in range(0, len(presidentes)):
        print(presidentes[i][0], "| Partido", presidentes[i][2], "|", presidentes[i][4], "votos. | Votos válidos:", ((presidentes[i][4]/votosValidosPresidente)*100))

    partidosEleitos.append(presidentes[0][2])
    
    print("Total de votos:", votosTotaisPresidente)
    print("Total de votos válidos e %", votosValidosPresidente, votosValidosPresPorc)
    print("Total de brancos e %", votosBrancosPresidente, (votosBrancosPresidente/votosTotaisPresidente)*100, "%")
    print("Total de nulos e %", votosNulosPresidente, (votosNulosPresidente/votosTotaisPresidente)*100, "%")

    selectionSort(governadores)

    votosValidosGovernador = votosTotaisGovernador-votosBrancosGovernador-votosNulosGovernador
    votosValidosGovPorc = (votosValidosGovernador/votosTotaisGovernador)*100 

    partidosEleitos.append(governadores[0][2])

    print("\nGovernadores: ")
    for i in range(0, len(governadores)):
        print(governadores[i][0], "| Partido", governadores[i][2], "|", governadores[i][4], "votos. | Votos válidos:", ((governadores[i][4]/votosValidosGovernador)*100))


    print("Total de votos:", votosTotaisGovernador)
    print("Total de votos válidos e %", votosValidosGovernador, votosValidosGovPorc)
    print("Total de brancos e %", votosBrancosGovernador, (votosBrancosGovernador/votosTotaisGovernador)*100, "%")
    print("Total de nulos e %", votosNulosGovernador, (votosNulosGovernador/votosTotaisGovernador)*100, "%")

    selectionSort(prefeitos)

    partidosEleitos.append(prefeitos[0][2])

    votosValidosPrefeito = votosTotaisPrefeito-votosBrancosPrefeito-votosNulosPrefeito
    votosValidosPrefPorc = (votosValidosPrefeito/votosTotaisPrefeito)*100 

    print("\nPrefeitos: ")
    for i in range(0, len(prefeitos)):
        print(prefeitos[i][0], "| Partido", prefeitos[i][2], "|", prefeitos[i][4], "votos. | Votos válidos:", ((prefeitos[i][4]/votosValidosPrefeito)*100))

    print("Total de votos:", votosTotaisPrefeito)
    print("Total de votos válidos e %", votosValidosPrefeito, votosValidosPrefPorc)
    print("Total de brancos e %", votosBrancosPrefeito, (votosBrancosPrefeito/votosTotaisPrefeito)*100, "%")
    print("Total de nulos e %", votosNulosPrefeito, (votosNulosPrefeito/votosTotaisPrefeito)*100, "%")

    input("Aperte qualquer tecla para voltar ao menu.")
    menu() 

def exibeRelatorioEstatisticas():
    print(eleitoresQueVotaram)
    votosTotais = votosTotaisGovernador
    if votosTotais==len(eleitoresQueVotaram):
        print(votosTotais, "eleitores votaram, auditoria válida")
    else:
        print("Auditoria inválida")
   
    listaPartidos = multimode(partidosEleitos)
    print("Partido que mais elegeu políticos:", mode(listaPartidos))
    for i in range(len(partidosEleitos)):
        if partidosEleitos[i]!=mode(partidosEleitos):
            print("Partido que menos elegeu políticos:", partidosEleitos[i])

    input("Aperte qualquer tecla para voltar ao menu.")
    menu() 

def selectionSort(lista):
    for step in range(len(lista)):
        minIndex = step
        for i in range(step+1, len(lista)):
            if lista[i][4] > lista[minIndex][4]:
                minIndex = i
        (lista[step], lista[minIndex]) = (lista[minIndex], lista[step])

menu()