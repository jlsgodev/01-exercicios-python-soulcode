# 16. Sequência de Fibonacci
#    - **Descrição:** Gere a sequência de Fibonacci até um número máximo fornecido pelo usuário usando um loop `while`.
#    A sequência começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.

numero = int(input("Digite um número inteiro positivo: "))
n1 = 0
n2 = 1
contador = 0
while n1 <= numero:
    print(n1)
    nesimo = n1 + n2
    n1 = n2
    n2 = nesimo
   
    


