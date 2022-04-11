#coleções(Listas)


#Valores de listas são acessíveis através de índices
precos = [20, 50, 200]
          #0    1    2 --> estes são os índices desta lista

print(precos[0])
print(precos.index(200))#neste trecho utilizamos a função index, e passamos um item da lista que estamos utilizando, para descobrir o índice daquele item da lista, no exemplo acima, queremos descobrir qual é o índice do item "200"

'''
Dado uma coleção de dados "idades" [15,46,75,34,23] imprima na tela a soma destes valores

idades = [15,46,75,34,23]
total = 0
loop idade em idades
  total = total+idade
print total
'''

idades = [15,46,75,34,23]
total = 0

for idade in idades:
  total = total + idade
print(total)