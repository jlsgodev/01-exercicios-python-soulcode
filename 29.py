# 29. Verificar Paridade de Números
#     - **Descrição:** Dado um número máximo fornecido pelo usuário, crie um programa que exiba
#     todos os números de 1 até o máximo e informe se cada um é par ou ímpar.


numero = int(input("Digite um número inteiro positivo: "))
for i in range(1,numero+1):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")

        