#  27. Contar Palavras em uma Frase
#     - **Descrição:** Crie um programa que conte o número de palavras em uma frase fornecida pelo usuário.
#     Use um loop `for` para iterar sobre as palavras da frase.


frase = input("Digite uma frase: ")
contador = 1
for letra in frase:
    if letra == " ":
        contador += 1

print(f"A frase '{frase}' tem {contador} palavras.")
