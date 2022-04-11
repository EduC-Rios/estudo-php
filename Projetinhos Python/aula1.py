#Variáveis
#Números
velocidade_net = 10
print(velocidade_net)
nota_filme = 8.5 #float
#Valores booleanos
esta_aberto = True #bool, pode ser True ou False
#Strings
nome_do_curso = 'Lógica de Programação'

#Como variáveis seriam usadas num programa real?
#Problema 1 - Valor por hora
#Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e em sua horas trabalhadas no mês

salario_mes = input ('Qual é o seu salário mensal? ')
horas_trabalhadas_mes = input ('Quantas horas você trabalha por mês? ')

valor_hora = int (salario_mes) / int (horas_trabalhadas_mes)

print(valor_hora)