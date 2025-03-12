import os
os.system ("clear")
#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, 
# caso contrário multiplique A por B. Ao final de qualquer um dos cálculos 
# deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.
valor_a = int(input("Digite um número: "))
valor_b = int(input("Digite outro número:"))

if valor_a == valor_b:
    valor_c = valor_a + valor_b
else: 
    valor_a * valor_b
    print(f"O resultado é: {valor_c} ")