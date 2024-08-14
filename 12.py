# 12. Soma de Números até um Limite 
# Descrição:** Desenvolva um programa que receba um número inteiro positivo e use um loop `while` 
# para calcular a soma de todos os números de 1 até o número fornecido.

# Solicitando um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))
soma = 0
i = 1

# Calculando a soma de todos os números de 1 até o número fornecido
while(i <= numero):
    soma += i
    i += 1
print(f"A soma de todos os números de 1 até {numero} é {soma}.")

