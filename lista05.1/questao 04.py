'''Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)'''

soma = 0
numero = 1

while numero <= 100:
    soma += numero
    numero += 1

print(f"O valor da soma dos cem primeiros números inteiros é {soma}")