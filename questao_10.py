import os
os.system("clear")
#Um posto está vendendo combustíveis com a seguinte tabela de descontos: (...)
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.
tipo = input("Digite o tipo de combustível (A- álcool, G- gasolina ): ")
litros = float(input("Digite a quantidade de litros vendidos: "))

match tipo: 
    case "A": 
        preço_litro = 3.79
        desconto = 0.2 if litros <= 25 else 0.4
    case "G":
        preço_litro = 6.59
        desconto = 0.3 if litros <= 25 else 0.5
    case _: 
        print("Opção inválida!")

valor = litros * preço_litro
valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print(f"\nTotal a pagar: R$ {valor_final:.2f}")