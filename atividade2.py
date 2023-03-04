
import math

numeroInformado = int(input("Informe o número desejado para verificação: "))

fibonacci = [0, 1]
numeroAnterior = 0
numeroAtual = 1
for i in range(15):
    soma = numeroAnterior + numeroAtual #1
    numeroAnterior = numeroAtual
    numeroAtual = soma
    fibonacci.append(soma) # Insere no vetor

# Formatação do output da sequência
print("Fibonacci: ", end='')
for x in fibonacci:
    print(x, " ", end='')
print("...") 

"""
Fórmula que mostra se um número pertence a Fibonacci:
Se (5*n*n+4) ou (5*n*n-4) for um quadrado perfeito.
Não seria possível verificar o número por meio de um loop,
Pois a sequência é infinita.
"""

def Fibonacci(n):
    quadrado1 = math.sqrt(5*n*n+4) #Informa se é um quadrado perfeito
    quadrado2 = math.sqrt(5*n*n-4)
    if (quadrado1==int(quadrado1) or quadrado2==int(quadrado2)):
        print("O número informado pertence a sequência de Fibonacci")
    else:
        print("Este número não pertence a sequência de Fibonacci")

Fibonacci(numeroInformado)