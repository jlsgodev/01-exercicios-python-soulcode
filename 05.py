# 5. Classificação e Ajuste de Salário com Reajuste 
#Problema: Crie um programa que receba o salário de um funcionário e determine 
#sua faixa salarial: "Baixa" (até R$ 2.500), "Média" (de R$ 2.501 a R$ 5.000) ou "Alta" (acima de R$ 5.000).
#Aplique um reajuste de 7% para a faixa baixa, 5% para a faixa média e 3% para a faixa alta. Mostre o salário reajustado. 

salario = float(input("Digite o salario do funcionario: "))
if salario <= 2500:
    salario = salario + (salario * 0.07)
    print("Salario reajustado: R$ ", salario)
elif salario >2501 and salario <= 5000:
    salario = salario + (salario * 0.05)
    print("Salario reajustado: R$ ", salario)
else:
    salario = salario + (salario * 0.03)
    print("Salario reajustado: R$ ", salario)
    
     

