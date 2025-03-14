import os
os.system("clear")
#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, 
#solicitar o tempo de casada (anos). Por fim, mostre os dados do usuário.

nome= input("Digite seu nome: ")
sexo= input("Digite seu sexo (F para feminino e M para masculino): ")
estado= input("Digite seu estado civil: ")

if sexo == "F" and estado == "casado":
    tempo_casamento = input("Há quanto anos você é casada?")
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estado}")
    print(f"Seu tempo de casamento: {tempo_casamento} anos")
else: 
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estado}")