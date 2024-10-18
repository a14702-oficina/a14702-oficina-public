#EX0.0

print("hello world!")

ValorA = float(input("Insira um valor entre 1-20: "))
ValorB = float(input("Insira um valor entre 1-20: "))
soma = ValorA+ValorB
media = (soma/2)
print (media)
if media >=10:
  print("Aprovado")
if media <=10:
  print("Reprovado")

------------------------------------------------------------------------------------------

#EXO.1

"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("Insira a sua idade: ");
nome = input("Insira o seu nome: ");
print(f"O meu nome é {nome} e tenho {idade} anos.");

------------------------------------------------------------------------------------------

#EX0.2

"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá, mundo!");
fruta = "bananas";
print(f"Eu gosto de  {fruta}.");

------------------------------------------------------------------------------------------

#EX0.3

"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input("Qual é o teu nome? ");
print(f"Olá,tudo bem, {nome}!" );
numero = int(input("Digite um número inteiro: "));
dobro = numero * 2;
print(f"O dobro de {numero} é {dobro}.")

------------------------------------------------------------------------------------------

#EX1.1

print("Hello World!")
"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""
a= "\n"
print("\nBem-vindos ao Python!")

------------------------------------------------------------------------------------------

#EX1.2

"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
a ="\n"
print("\nJosé, bem-vindo ao Python!")

------------------------------------------------------------------------------------------

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
mensagem =
"""
_   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)
"""

------------------------------------------------------------------------------------------

#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome = "Daniel"
idade = "15"
localidade = "Alvarelhos"
print(f"O meu nome é {nome}, tenho {idade} anos e moro em {localidade}")

------------------------------------------------------------------------------------------

#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
linguagem = "Python"
nome = "Daniel"
print(f"Estou a prender {linguagem} e chamo-me {nome}")

------------------------------------------------------------------------------------------

# EX 1.6
"""Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""
mensagem ="Bem-vindo ao Python!"
print(f"{mensagem:>50}")
print(f"{mensagem:<50}")
print(f"{mensagem:^50}")

-------------------------------------------------------------------------------------------

# EX 1.7
print("Hello World!")
"""Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""
raio = float(input("Insira o raio da circunferência: "))
perimetro = 2 * 3.14 * raio
area = 3.14 * raio ** 2
print(f"O perimetro da circunferência é {perimetro} e a área é {area}")

------------------------------------------------------------------------------------------

#EX 1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
import datetime
data_atual = datetime.datetime.now()
dia = data_atual.strftime("%d")
mes = data_atual.strftime("%m")
ano = data_atual.strftime("%y")
hora = data_atual.strftime("%h")
minutos = data_atual.strftime("%m")
segundos = data_atual.strftime("%s")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}{ano} {hora}:{minutos}:{segundos}")
print(f" {dia}/{mes}/{ano}")
print(f" {hora}/:{minutos}/:{segundos}")
print(f"{dia}/{mes}/{ano} {hora}:{minutos}:{segundos}")

------------------------------------------------------------------------------------------

#EX 1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.

Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""
numero = int(input("Digite o número do atleta: "))
pontos = float(input("Digite a pontuação final: "))
print(f"O atleta número {numero} obteve {pontos} pontos.")

------------------------------------------------------------------------------------------

#EX 1.10

"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""
import datetime
data_atual = datetime.datetime.now()
dia = data_atual.strftime("%d")
mes = data_atual.strftime("%m")
ano = data_atual.strftime("%Y")
nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
data_atual = datetime.datetime.now()
dia_nascimento  = int(nascimento[:2])
mes_nascimento = int(nascimento[3:5])
ano_nascimento = int(nascimento[6:])
idade = data_atual.year - ano_nascimento - ((data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento))
print(f"A idade é {idade} anos.")

------------------------------------------------------------------------------------------

#EX 1.10

"""
Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO).
"""
libras = float(input("Insira o valor em libras: "))
euro = libras * 1.19
print(f"O valor em euros é {euro}")

------------------------------------------------------------------------------------------

#EX D 028

print("Hello World")
"""
Escreva um pograma que faça computador "pensar" em um numero inteiro entre o e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O pograma deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random

segredo = int(random.randint(0,5))
# print(f"O numero secreto é: {segredo}")

numeroescolhido = int(input("Insira um valor entre (0 e 5): "))
if numeroescolhido > segredo:
  print("O Numero Inserido é maior do que o meu!")
elif numeroescolhido < segredo:
  print("O Numero escolhido é menor do que o meu! ")
else:
  print("Você acertou!")

------------------------------------------------------------------------------------------

#EX D 029

print("Hello World")

"""Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar 7,00€ por cada Km acima do limite."""
velocidade = int(input("Insira a velocidade do carro: "))
multa = (velocidade) - 80
valor = (multa) * 7
if velocidade > 80:
  print(f"Excedeste a velocidade em {multa} km/h e vais ter que pagar {valor}€ de multa")
else:
  print("Estavas na velocidade certa!")







------------------------------------------------------------------------------------------

#FP1
print("Hello World")
"""
Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else.
"""
n = int(input("Insira um numero: "))
if n > 0:
  print("O numero é positivo")
elif n < 0:
  print("O numero é negativo")
else:
  print("Numero igual a 0")

------------------------------------------------------------------------------------------

#FP2
print("Hello World")
"""
Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.
"""
n = int(input("Insira um número inteiro: "))
if n % 2 == 0:
  print("O numero é Par")
else:
  print("O numero é Impar")

------------------------------------------------------------------------------------------

#FP3
print("Hello World")

"""
Calcular a nota final de um aluno.Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:
Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"

"""
nota = int(input("Insira a sua nota: "))
if nota <10 :
   print("Reprovado")
elif nota >=10 and nota <=14:
   print("Suficiente")
elif nota >=15 and nota <=17:
   print("Bom")
elif nota >17:
   print("Muito Bom")

-----------------------------------------------------------------------------------------

#FP4
print("Hello World")

"""
Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15
"""
temp = float(input("Insira a temperatura em graus Celsius: "))
unidade = input("Insira a unidade de destino (Fahrenheit ou Kelvin): ")
if unidade == "Fahrenheit":
  fahrenheit = temp * 9/5 + 32
  print(f"A temperatura em Fahrenheit é {fahrenheit} °F")
if unidade ==  "Kelvin":
  kelvin = temp + 273.15
  print(f"A temperatura em Kelvin é {kelvin} K")

----------------------------------------------------------------------------------------

#FP5
print("Hello World")

"""
Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""
salario = int(input("Insira o seu salário mensal: "))
if salario <= 1000:
  print("Isento de impostos")
elif salario > 1000 and salario <= 2000:
  imposto = salario * 0.1
  print(f"O imposto é de {imposto} €")
elif salario > 2000:
  imposto = salario * 0.2
  print(f"O imposto é de {imposto} €")







----------------------------------------------------------------------------------------

"""
 Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.

[consola]
1
2
3
...
10
"""
for i in range(1,11):
  print(i)
----------------------------------------------------------------------------------------
"""
Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.

[consola]
A soma de 1 a 100 é: 5050
"""
soma = 0
i = 1
while i <= 100:
  soma += i
  i += 1
print(f"A soma de 1 a 100 é: {soma}")

------------------------------------------------------------------------------------------
"""
Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.

[consola]
Introduza uma frase: Programação em Python
Número de vogais: 7
"""
frase = input("Insira uma frase: ")
contador = 0
for letra in frase:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    contador += 1
print(f"Número de vogais: {contador}")

------------------------------------------------------------------------------------------
"""
Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.

[consola]
5
10
15
...
50
"""
for i in range(5,51,5):
  print(i)
------------------------------------------------------------------------------------------
"""
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
[consola]
Introduza um número: 13
13 é um número primo.
"""
notas = []
for i in range(0,5):
  numeros = int(input("Insira o valor inteiro: "))  
  notas.append(numeros) #Adicionar um elemento á lista
soma = sum(notas) #calcula a soma dos elementos da lista
x= len(notas) #devolve o numero total de elementos da lista
media = (soma / x) #calcula a media
print(media) 


-------------------------------------------------------------------------------------------
"""Média de uma lista de números.
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.

[consola]
Introduza o número 1: 10
Introduza o número 2: 20
Introduza o número 3: 30
Introduza o número 4: 40
Introduza o número 5: 50
A média é: 30.0
"""
numero = int(input("Insira um numero: "))
divisores = 0
for i in range(1, numero + 1):
  if numero % i == 0:   #Se o resto da divisão for 0 
    divisores += 1   #Adiciona 1 ao contador de divisores
if divisores == 2:   #Se o contador de divisores for 2
  print(f"{numero} é um número primo.")   #Imprime que o número é primo
else:
  print(f"{numero} não é um número primo.")  #Imprime que o número não é primo


------------------------------------------------------------------------------------------
"""Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""
"""Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""
lista = [] #Cria uma lista vazia
for i in range(1,21): #Cria um ciclo for que vai de 1 a 20
  if i % 2 == 0: #Se o resto da divisão for 0
    lista.append(i) #Adiciona o elemento à lista
print(lista) #Imprime a lista

------------------------------------------------------------------------------------------
"""Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
"""
texto = str(input("Insira uma palavra ou frase: "))
textoinv = texto [::-1]
print(textoinv)

------------------------------------------------------------------------------------------
"""Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.
"""
numero = int(input("Insira um numero: "))
for i in range(1,11):
  mult = numero * i
  print(f"{numero} x {i} = {mult}")

------------------------------------------------------------------------------------------
"""Escreve um programa que utilize um ciclo while para calcular o fatorial de um número introduzido pelo utilizador. O fatorial de um número n (n!) é o produto de todos os números inteiros positivos até n.
"""



  
