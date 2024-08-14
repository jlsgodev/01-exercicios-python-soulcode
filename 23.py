 #  23 Inverter uma String
 #   - **Descrição:** Crie um programa que inverta uma
# string fornecida pelo usuário sem usar funções embutidas, utilizando um loop `for`.

s = input("Digite uma frase: ")
print(s)

#Inverter uma string usando slicing
x = s[::-1] # O slicing [::-1] começa do início até o final da sequência, mas com um passo de -1, o que inverte a string.

# y = s[0:5:2]

print(x)

