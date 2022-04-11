#Projeto - Chute um número
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início seja chutado corretamente

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa

#Método 5Q's para montar um algorítmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações/investigue mais até voce compreender completamente o problema)

1.Quais são os dados de entrada necessários?
valor aleatório, chute do usuário
2.O que devo fazer com estes dados?
comparar o valor do usuario com o valor aleatório, e dizer no final se o chute foi maior, menor ou igual ao valor aleatorio gerado no inicio do programa 
3.Quais são as restrições deste problema?
deve ser gerado um valor de 1 a 10 apenas
4.Qual é o resultado esperado?
O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa
5.Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
  print seu chute foi maior que o valor gerado
elif chute < valor_aleatorio
  print seu chute foi menor que o valor gerado
else
  print voce acertou o chute
'''

import random

valor_aleatorio = random.randint(1,10)

chute = int(input("Digite seu chute entre 1 e 10: "))

if chute > valor_aleatorio:
  print("Seu chute foi maior que o número gerado")
elif chute < valor_aleatorio:
  print("Seu chute foi menor que o número gerado")
else:
  print("Você acertou!")

#Se eu tiver mais de uma condicional, usar ELIF e não IF