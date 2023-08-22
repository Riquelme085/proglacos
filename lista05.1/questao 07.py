'''Desenvolver um programa que apresente todos os números divisíveis por 4 que sejam menores que 200. Para
saber se o número é divisível por 4 será necessário verificar a lógica desta condição com o comando if. Sendo
divisível, mostre-o; não sendo, passe para o próximo passo. A variável que controla o contador deve ser iniciada
com valor 1.'''

contador = 1

while contador * 4 < 200:
    numero = contador * 4
    if numero % 4 == 0:
        print(numero)
    contador += 1