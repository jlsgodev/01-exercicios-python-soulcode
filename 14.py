# 14. Fatorial de um Número 
# Descrição:** Calcule o fatorial de um número fornecido pelo 
# usuário usando um loop `for`. 
# O fatorial de um número `n` é o produto de todos os números de 1 até `n`.


# Solicitando um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))
fatorial = 1
for i in range (1,numero +1 ):
    fatorial = (fatorial*i)

print(f"O fatorial de {numero} é {fatorial}")
