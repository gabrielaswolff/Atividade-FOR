#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada

numero = int(input("digite um número entre 1 e 10 para aparecer a tabuada: "))

if 1 <= numero <= 10:
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("número inválido.")
