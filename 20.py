# 20. Conversão de Temperatura
#     - **Descrição:** Desenvolva um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa.
#     Use loops para permitir múltiplas conversões até que o usuário decida parar.

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("Escolha uma opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")
    escolha = input("Digite 1, 2 ou 3: ")
    
    if escolha == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius)}°F.")
    elif escolha == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit)}°C.")
    elif escolha == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue

    