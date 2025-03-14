import os
os.system ("clear")
#Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
#O programa deve calcular o resultado da operação escolhida aplicado a A e B. Por exemplo, se a operação escolhida
#  foi * e A = 1 e B = 3, o programa deve fornecer como resultado o valor de 1*3, que é 3.

numero_um = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
numero_dois = int(input("Digite um número: "))

match operador:
    case "+":
        resultado = numero_um + numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "/":
        resultado = numero_um / numero_dois
    case _:
        resultado = "Opção inválida. "
print(f"\nSeu primeiro número foi: {numero_um}")
print(f"Seu operador: {operador}")
print(f"Seu segundo número foi: {numero_dois}")
print(f"O resultado é: {resultado}")