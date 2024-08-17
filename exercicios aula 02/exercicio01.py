import os
os.system('cls')

prod = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))

if valor <= 0:
    result = "Valor inválido"
    
if valor < 50:
    result = "Sem desconto"
elif valor >= 50 and valor < 200:
    result = valor * 0.05
elif valor >= 200 and valor < 500:
    result = valor * 0.06
elif valor >= 500 and valor < 1000:
    result = valor * 0.07
elif valor >= 500 and valor < 1000:
    result = valor * 0.07
else:
    result = valor * 0.08
        

print("nome do produto: ", prod)
print("valor do produto: ", valor)
print("valor do desconto: ", round(result,2))
print("valor com desconto: ", valor-result)