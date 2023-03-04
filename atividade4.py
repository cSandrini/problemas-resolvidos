"""
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
"""

# Vetor com os dados
faturamentoEstado = [["SP", 67836.43],["RJ", 36678.66],["MG", 29229.88],["ES", 27165.48],["Outros", 19849.53]]
valorTotalMensal=0

# Calcula o valor total mensal
for i in range(len(faturamentoEstado)):
    valorTotalMensal += faturamentoEstado[i][1]

# Informação gerada
print("Percentual de representação do estado no valor total: ")
for i in range(len(faturamentoEstado)):
    porcentagem=100*faturamentoEstado[i][1]/valorTotalMensal
    print(faturamentoEstado[i][0], " - %.2f%%" %porcentagem)
