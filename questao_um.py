import os
os.system("clear")
#Faça um algoritmo que leia os valores A, B, C e imprima na tela 
#Se a soma de A + B é menor que C, caso contrário.
# Imprima que a A + B é maior que C. 

valor_a = int(input("Olá digite um número: "))
valor_b = int(input("Digite outro número: "))
valor_c = int(input("Mais um: "))

soma= valor_a + valor_b

if soma < valor_c:
    print(f"A soma dos 2 primeiros números é menor que  o terceiro")

else: 
    soma > valor_c
    print(f"a soma dos dois primeiros números é maior que o terceiro")