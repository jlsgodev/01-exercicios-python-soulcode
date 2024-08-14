# 9. Calculadora de Desconto com Condição de Pagamento**  
# Problema: Crie um programa que receba o valor de uma compra e determine o desconto a ser aplicado. 
# Aplique 20% de desconto para compras acima de R$ 1.500, 10% para compras entre R$ 800 e R$ 1.500, e 5% para compras abaixo de R$ 800. 
# Se o pagamento for à vista, aplique um desconto adicional de 5% sobre o valor final com desconto. 
 


valor = float(input("Digite o valor da compra: "))

# Determinando o desconto inicial com base no valor da compra
if valor > 1500:
    desconto = valor * 0.20
    valor -= desconto
    print("Desconto de 20% aplicado. Valor final:R$ ", valor )
elif valor >= 800:
    desconto = valor * 0.10
    valor -= desconto
    print("Desconto de 10% aplicado. Valor final: R$ ", valor)
else:
    valor > 0 and valor < 800 
    desconto = valor * 0.05
    valor -= desconto
    print("Desconto de 5% aplicado. Valor final: R$ ", valor )

# Solicitando a forma de pagamento
pagamento = input("Digite a forma de pagamento (a vista ou parcelado): ")

# Aplicando desconto adicional se o pagamento for à vista
if pagamento.lower() == "a vista":
    desconto_adicional = valor * 0.05
    valor -= desconto_adicional
    print("Desconto adicional de 5% aplicado. Valor final: R$ ", valor )
else:
    print("Valor final: R$  ", valor )


