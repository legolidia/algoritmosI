#Bruno Cruz Bregion Novo - TIA: 42222494
#Lídia Carolina de Andrade Rosa - TIA: 32281374

def calculaRaiz(num): #função que calcula a raiz quadrada
    return num**0.5

def verificaQuadrante(x, y): #função que verifica em que quadrante o ponto está
    if x>0 and y>0: #1º quadrante: x e y positivos
        return "1o quadrante"
    elif x<0 and y>0: #2º quadrante: x negativo e y positivo
       return "2o quadrante"
    elif x<0 and y<0: #3º quadrante: x e y negativos
        return "3o quadrante"
    elif x>0 and y<0: #4º quadrante: x positivo e y negativo
        return "4o quadrante"    
    else: #ponto está em um dos eixos
        return "eixo coordenado"

def calculaDistancia(x2, y2): #função que calcula a distância entre o ponto e a origem transladada
    distancia = calculaRaiz(x2**2+y2**2) #fórmula para calcular distância entre pontos (e chama a função calculaRaiz)
    return distancia #retorna a distância calculada

def calculaTranslacao(pontoNaoTransladado, translacao): #função que calcula a translação de uma coordenada do Ponto
    return translacao - pontoNaoTransladado #para calcular a translação, subtrai a coordenada lida da coordenada transladada

xTransladado = int(input()) #leitura da translação do x
yTransladado = int(input()) #leitura da translação do y

pontos = int(input()) #quantidade de pontos que serao lidos

for i in range(0, pontos):
    x = int(input()) #lê a abscissa do ponto
    y = int(input()) #lê a ordenada do ponto

    x2 = calculaTranslacao(xTransladado, x) #calcula a diferença de acordo com a translação do X com uma função
    y2 = calculaTranslacao(yTransladado, y) #calcula a diferença de acordo com a translação do Y com uma função

    q = verificaQuadrante(x2, y2) #verifica em qual quadrante está o ponto com uma função
    
    print("\nPonto (%d, %d) está no %s." %(x, y, q))
   
    distancia = calculaDistancia(x2, y2) #calcula a distancia entre o ponto e da origem

    #na primeira execução do laço de repetição (for), armazena a primeira distância calculada para futuras comparações
    if i==0:
        maiorDist = distancia
        menorDist = distancia

    #verifica se a atual distância é a maior 
    if distancia>=maiorDist:
        maiorDist = distancia #se for a maior, armazena a distância atual na variável maiorDist
        pontoMaior = "(%d, %d)" %(x, y) #armazena uma string com o Ponto que possui a maior distância, já formatada
        
    #verifica se a atual distância é a menor
    if distancia<=menorDist:
        menorDist = distancia #se for a menor, armazena a distância atual na variável menorDist
        pontoMenor = "(%d, %d)" %(x, y) #armazena uma string com o Ponto que possui a menor distância, já formatada


print("Ponto %s eh o mais proximo, distancia=%.2f." %(pontoMenor, menorDist)) #imprime o ponto mais próximo e a menor distância
print("Ponto %s eh o mais distante, distancia=%.2f." %(pontoMaior, maiorDist)) #imprime o ponto mais distante e a maior distância