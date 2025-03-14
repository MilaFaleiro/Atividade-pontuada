import os
os.system ("clear")
#Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores. 
# Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. 
# Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço. 
# A loja está atualmente com a seguinte tabela de preços.  


opcao = input("""
Olá, bem-vindo a feirinha de cd, aqui vai a tabela de cores
Verde 
Azul 
Amarelo 
Vermelho                
Digite a opção desejada:                                                                                      
""")
match opcao:
    case "Verde":
        print("Olá o valor do cd verde é R$ 10,00.")
    case "Azul": 
        print("Olá o valor do cd azul é R$ 20,00.")
    case "Amarelo":
        print("Olá o valor do cd amarelo é R$ 30,00.")
    case "Vermelho":
        print("Olá o valor do cd vermelho é R$ 40,00.")