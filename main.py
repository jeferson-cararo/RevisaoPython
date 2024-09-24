''' --> Comentário de Bloco
Título: Revisão de Python
Autor: Jeferson
Data: 2024.07.02
'''
# --> Comentário de linha
#Objetivo: Revisar os fundamentos de Programação em Python

print("Hello World")

# Saída --> print()
print('o rhuan é adm namorador') # 'string'
print('100 + 100') # 'string'
print(100 + 100) # operação

# Entrada --> input()
nome = input('Matheus é um Míseravel?: ')
print( 'Você disse:' "é verdade", nome)
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
total = valor1 + valor2
print('Soma dos valores digitados é:', total)

# variáveis --> espaço de memória que armazena valores temporariamente
# str --> Armazena textos e caracteres --> %s ou %c
nome = 'Echolinoooo'
print('A variável nome é do tipo:', type(nome), 'e tem armazenado o valor: %s' %nome)
# int --> Armazena números inteiros positivos e negativos --> %d
valorX = -81
print('A variável valorX é do tipo:', type(valorX), 'e tem armazenado o valor: %d' %valorX)
#float --> Armazena números de ponto flutuante positivos e negativos --> NÂO USA , USA . --> %f == %.2f
pi = 3.14159
print('A variavel pi é do tipo:', type(pi), 'e tem armazenado o valor: %.2f' %pi)
#bool --> Armazena True ou False
teste = 10 > 50 
print('A variavel teste é do tipo:', type(teste), 'e tem armazenado o valor:', teste)

# Operadores
# Aritméticos --> Calculos +, -, *, /, **, //, %
print(5*5)
print(15/4) # --> resultado float
print(10//3) # --> resultado número inteiro
print(10%4)
# Atribuição 
A = 10 # --> = (RECEBE)
A += 1 # INCREMENTO SOMA 1
A -= 1 # --> DECREMENTO DIMINUI 1
# Relacionais --> Fazem comparação e retornam True ou False
A == 10 # == é igual == True
A != 10 # diferente == False
# >; <; >=; <=
#Lógicos --> Concatenação de operadores relacionais
# and == e; or == ou; not == não 

# Repetição -->
#laço for --> Quando eu sei quantas vezes vai repetir
#for i in range(11, 102, 2):
# print(i)

palavra = 'Programação'
for letra in palavra:
  print(letra)

tecla = 1
while tecla != 0: # --> Repete até a condição ser False
  tecla =int(input('Esta no laço While! Digite um número:'))

# Condição --> if; else; elif
idade = int(input('Informe a idade?:'))
if idade >= 18: # Testa e faz se o resultado True
  print('pode ir pro server dos guri!')
elif idade >= 16: # Faz se o if == False e os elif == True
  print('Entra no server com autorização!')
else: # Se o resultado do if for == a False
  print('Não pode ir no server dos guri!')
  
# Funções --> def
def soma(X, Y):
  R = X + Y
  return R

print(soma(10, 5 ))
print(soma(100, 50))
A = int(input('Digite um valor: '))
B = int(input('Digite outro valor'))
print('Soma de %d e %d é igual a %d' %(A, B, (soma(A,B))))



