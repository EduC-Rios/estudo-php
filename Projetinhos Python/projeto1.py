#EXEMPLO 5 - Fatorial de um número

'''
Crie um programa que recebe um número e imprime o seu fatorial
#Método 5Q's para montar algorítimo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações/investigue mais até voce compreender completamente o problema)

1.Quais são os dados de entrada necessários?
numero
2.O que devo fazer com estes dados?
devo calcular o fatorial do numero passado para o meu programa e o exibir na tela
3.Quais são as restrições deste problema?
não pode ser um numero negativo, e precisa ser inteiro
4.Qual é o resultado esperado?
mostrar o numero fatorial na tela
5.Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
pedir um numero ao usuário, que seja positivo e inteiro, calcular seu fatorial, e exibir o resultado na tela

input numero
if numero > 0
if numero == inteiro
fatorial = 1 
loop de 1 a numero
  fatorial = fatorial * numero
print (fatorial)
'''

numero = int(input('Digite um número por favor: '))
if numero > 0:
  fatorial = 1
  for item in range(1,numero + 1):
    fatorial = fatorial * item
  print(fatorial)
  


