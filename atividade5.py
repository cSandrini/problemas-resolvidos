txt = input("Insira um texto: ")
txtInv = []

# Faz um loop reverso para criar o novo vetor
for i in range(len(txt)-1, -1, -1):
    txtInv.append(txt[i])

# Linha que transforma o vetor em uma string
txt = ''.join(str(x) for x in txtInv)

# Output do textova invertido
print(txt)