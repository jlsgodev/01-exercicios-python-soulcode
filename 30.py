#  30. Somar Números em uma Lista
#     - **Descrição:** Crie uma lista de números e calcule a soma de todos
#     os números positivos usando um loop `for`.


lista = [1,2,3,4,5,6,7,8,9,-10]
soma = 0
for i in lista:
    if i > 0:
        soma += i
print(f"A soma de todos os números positivos na lista é {soma}")



