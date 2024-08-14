#
#  25. Múltiplos de um Número
 #   - **Descrição:** Crie um programa que encontre todos os múltiplos de um número fornecido
# pelo usuário até um valor máximo também fornecido pelo usuário.

numero = int(input("Digite um número inteiro positivo: "))
maximo = int(input("Digite um valor máximo: "))
for i in range(1,maximo+1):
    if i % numero == 0:
        print(i)

        