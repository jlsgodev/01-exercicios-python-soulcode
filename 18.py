# 18. Tabuada de um Número
#    - **Descrição:** Crie um programa que exiba a tabuada (de 1 a 10) de um número
#    fornecido pelo usuário usando um loop `for`.

numero = int(input("Digite um número inteiro positivo: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")

    