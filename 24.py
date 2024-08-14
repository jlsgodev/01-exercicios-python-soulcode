# 24. Verificar Palíndromo
#     - **Descrição:** Desenvolva um programa que verifique se uma palavra é um palíndromo
#     (ou seja, se pode ser lida da mesma forma de trás para frente). Use um loop `for` e condicionais.

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")
    