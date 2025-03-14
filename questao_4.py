import os
os.system ("clear")
#Uma fruteira está vendendo frutas com a seguinte tabela de preços...
#Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00,
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

kg_morango = float(input("Olá digite a quantidade de morangos (em kilos):" ))
kg_maça = float(input("Olá digite a quantidade de maçãs (em kilos):" ))

preço_morango_ate5 = 2.50
preço_maça_ate5 = 1.80
preço_morango_acima5 = 2.20
preço_maça_acima5 = 1.50

if kg_morango <= 5:
    preço_morango = kg_morango * preço_morango_ate5
else:
    preço_morango = kg_morango * preço_morango_acima5

if kg_maça <= 5: 
    preço_maça = kg_maça * preço_maça_ate5
else:
    preço_maça = kg_maça * preço_maça_acima5

valor_final = preço_morango + preço_maça

if (kg_morango + kg_maça) > 10 or valor_final > 15.00:
    valor_final *= 0.9
    print(f"O valor a ser pago é: R$ {valor_final:.2f}")