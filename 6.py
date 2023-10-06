#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

menor_valor = float('inf')  
maior_valor = float('-inf')  
soma_valores = 0

n = int(input("quantos números deseja inserir? "))


for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma_valores += numero

    if numero < menor_valor:
        menor_valor = numero

    if numero > maior_valor:
        maior_valor = numero

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")
