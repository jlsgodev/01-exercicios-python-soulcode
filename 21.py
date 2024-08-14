# 21. Média de Notas
#     - **Descrição:** Crie um programa que calcule a média de uma série de notas fornecidas pelo usuário.
#     O programa deve parar quando o usuário digitar um valor negativo.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media <= -1: 
    print("Valor negativo")

else:
    print(f"A média das notas é {media}.")

