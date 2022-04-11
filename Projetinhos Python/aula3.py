#Laços de repetição
#Listas

#for palavra in range(1,4):
  #print('Carregando')

'''
a função range(x, y) serve para criarmos uma lista simples, onde os parametros xe y seriam o tamanho dela
por exemplo: range(1, 8) essa lista teria 7 posições pois o número que está no "limite" não seria contado
por exemplo "a lista irá de n, até n-1"

também existe a sintaxe onde nos permite "pularmos valores" por exemplo(uma range(1,10,2) esta range terá 9 casas e ira contar sempre somando +2, ex:
1, 3, 5, 7, fim da execução, e por ai vai dependendo do valor da sua range)

nomes = ['Eduardo', 'Fabricio', 'Camila', 'Robson']
for nome in nomes:
  print(nome)
'''

'''
#Imprima os valores de 1 a N
input numero_max
valor_inicial = 1
loop de valor_ini a numero_max
  print valor
'''
valor_max = int(input('Digite o valor máximo desejado: '))
valor_ini = 1
for numero in range(valor_ini, valor_max + 1):
  print (numero)
