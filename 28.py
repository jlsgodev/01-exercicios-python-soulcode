#  28. Tabuada de 1 a 10
#     - **Descrição:** Crie um programa que exiba a tabuada de 1 a 10
#     usando dois loops `for`: um para o número base e outro para o multiplicador.



for i in range(1,11):
    print(f"Tabuada do {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("\n")
