# **7. Conversão e Comparação de Temperatura**  
# Problema:** Crie um programa que receba uma temperatura em graus Celsius e a converta para Fahrenheit. 
# Em seguida, verifique se a temperatura em Fahrenheit é inferior a 32°F (fria), entre 32°F e 68°F (amena), ou superior a 68°F (quente).
# Mostre a classificação junto com a temperatura convertida. 

temperatura = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (temperatura * 9/5) + 32
if fahrenheit < 32:
    print("Temperatura fria: ", fahrenheit, "°F")
elif fahrenheit >= 32 and fahrenheit <= 68:
        print("Temperatura amena: ", fahrenheit, "°F")
else:
            print("Temperatura quente: ", fahrenheit, "°F")
            