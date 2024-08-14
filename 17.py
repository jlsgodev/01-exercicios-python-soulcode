# 17. Contar Caracteres em uma String
#    - **Descrição:** Conte quantas vezes um caractere específico aparece em uma string
#    fornecida pelo usuário usando um loop `for`.

palavra = input("Digite uma palavra: ")
caractere = input("Digite um caractere: ")
contador = 0
for letra in palavra:
    if letra == caractere:
        contador += 1

print(f"O caractere '{caractere}' aparece {contador} vezes na palavra '{palavra}'.")
