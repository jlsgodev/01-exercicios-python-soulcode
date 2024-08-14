# 8. Comparação de Três Números com Verificação de Ordenação**  
#  Problema:  Desenvolva um programa que receba três números inteiros e determine qual é o maior e o menor. 
# Além disso, verifique e informe se os números estão em ordem crescente, decrescente ou se não estão ordenados.  



# Solicitando três números inteiros ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Determinando o maior e o menor número
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

# Exibindo o maior e o menor número
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

# Verificando a ordenação dos números
if numero1 <= numero2 <= numero3:
    print("Os números estão em ordem crescente.")
elif numero1 >= numero2 >= numero3:
    print("Os números estão em ordem decrescente.")
else:
    print("Os números não estão ordenados.")
