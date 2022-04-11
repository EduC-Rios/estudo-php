#Condicionais
#if, elif e else
'''
Eae Eduardo, bora dar uma saida hoje?
R: Se eu terminar meu trabalho aqui, eu consigo.

trabalho_terminado = False

if trabalho_terminado == True:
  print('Opa, bora dar uma saída.')
else:
  print('Não posso sair agora.')
'''

'''
Ei, você consegue me ajudar a mover essas caixas lá pra fora hoje a tarde?
R: Se eu estiver livre, sim. Mas, se não der pede meu irmão pra te ajudar

estou_livre = True
if estou_livre == True:
  print('Ok, posso ajudar hoje sim.')
else:
  print('Peça o meu irmão para te ajudar')
'''

'''
Eu cheguei atrasado na aula, ainda posso entrar?
R: Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão

qtd_de_atrasos = 2
if qtd_de_atrasos >= 3:
  print('Você está suspenso!')
elif qtd_de_atrasos == 1:
  print('Pode entrar, porém caso tome mais duas faltas, irá ser suspenso')
elif qtd_de_atrasos == 2:
  print('Pode entrar, porém caso tome mais uma falta, irá ser suspenso')
else:
  print('Pode entrar')
'''


#Condicionais
#if, elif e else

#Encontre o maior entre 2 números
'''
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
  print o primeiro valor é maior
else
  print o segundo valor é maior
'''

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if int(primeiro_valor) > int(segundo_valor):
  print('O primeiro valor é maior!')
else:
  print('O segundo valor é maior!')
  