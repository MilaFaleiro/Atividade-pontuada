import os
os.system ("clear")
#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas. 
# O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado
# (média superior ou igual a 6,0), média até 4,0, o aluno está em recuperação, caso a média seja inferior a 4,0 o aluno será reprovado

nota_um = float(input("Digite sua nota: "))
nota_dois = float(input("Digite sua segunda nota: "))
 
soma = (nota_um + nota_dois) /2

if soma >= 6:
 print("Parabéns você foi aprovado.")
 print(f"Sua media é: {soma}")

elif soma >= 4:
 print("Você está em recuperação.")
 print(f"Sua media é: {soma}")

else:
 print("Você está reprovado.")
 print(f"Sua media é: {soma}")