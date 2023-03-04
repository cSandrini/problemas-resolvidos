import json

# Leitura do arquivo json
with open("dados.json", encoding='utf-8') as dadosJson:
    dados = json.load(dadosJson)

valorMax=0
valorMin=dados[0]['valor']
soma=0

for i in range(len(dados)): # Loop para verificar os valores maximos e minimos
    valorLido=dados[i]['valor']
    if(valorLido>valorMax):
        valorMax=valorLido
    if(valorLido<valorMin):
        valorMin=valorLido
    if(valorLido!=0): # Retira os valores iguais a 0 da soma
        soma += valorLido

media = soma/len(dados) # Calculo da media baseado no numero de dias

diasSuperiorMedia=[]
for i in range(len(dados)):
    valorLido=dados[i]['valor']
    if(valorLido>media):
        diasSuperiorMedia.append(dados[i]['dia'])

print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", len(diasSuperiorMedia))
print("Valor máximo: ", valorMax)
print("Valor mínimo: ", valorMin)

# Para facilitar o código poderia ser utilizado essas duas funções do python
# min(dados["valor"] for dados in dados)
# max(dados["valor"] for dados in dados)

# Media mensal
# print("Média mensal: %.4f" %media)