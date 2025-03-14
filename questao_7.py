import os
os.system("clear")
#Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
#Se quantidade <= 5 o desconto será de 2% 
#Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
#Se quantidade > 10 o desconto será de 5%.

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade que você quer: "))
valor = float(input("Digite o valor do produto: "))

total = quantidade * valor

if quantidade <= 5:
    desconto = 0.2
elif quantidade <= 10:
    desconto = 0.3
else:
    desconto = 0.5
desconto_final = total * desconto
valor_final = total - desconto_final

print(f"\nProduto: {produto}")
print(f"Total: R$ {total:.2f}")
print(f"Seu desconto é: R$ {desconto_final:.2f}")
print(f"Total a ser pago: R$ {valor_final:.2f}")