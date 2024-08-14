# 22. Números Divisíveis por 3 e 5
#     - **Descrição:** Crie um programa que liste todos os números entre 1 e 100 que são divisíveis por 3 e por 5
#     usando um loop `for` e condicionais.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

        