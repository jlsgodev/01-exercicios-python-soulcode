#  19. Contador de Letras em Palavras
#    - **Descrição:** Dada uma lista de palavras, conte quantas letras `a` existem
#    em todas as palavras usando um loop `for` e condicionais.

palavras = ["banana", "açai", "abacaxi", "abacate", "melancia"]
contador = 0
for palavra in palavras:
    for letra in palavra:
        if letra == "a":
            contador += 1
print(f"O caractere 'a' aparece {contador} vezes nas palavras: ", palavras)