import os 
os.system("clear")
#Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do empréstimo deve ser até 
# dez vezes o valor da renda mensal do solicitante e o valor da prestação deve ser no máximo 30% da renda mensal 
# do solicitante. Escreva um programa que leia a renda mensal de um solicitante, o valor total do empréstimo 
# solicitado e o número de prestações que o solicitante deseja pagar 
# informe se o empréstimo pode ou não ser concedido.
renda = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor que você gostaria de tomar emprestado: "))
prestacoes = int(input("Digite o número de prestações: "))

limite_de_emprestimo = renda * 10
prestacoes_por_mes = valor_emprestimo / prestacoes
limite_de_parcelas = renda * 0.3

if valor_emprestimo <= limite_de_emprestimo and prestacoes_por_mes <= limite_de_parcelas:
    print ("Parabéns, seu empréstimo foi concedido! ")
else:
    print ("Poxa, Parece que você não precisa. Empréstimo negado. ")