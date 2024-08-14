# 15. Verificação de Primalidade
# Descrição: Crie um programa que verifique se um número é primo. Use um loop `for` e condicionais
# para determinar se o número tem apenas dois divisores: 1 e ele mesmo.

numero = int(input("Digite um numero inteiro: "))
contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador +=1
if contador == 2:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

