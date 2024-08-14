#**6. Verificação de Ano Bissexto com Mensagens**  
#Problema:** Desenvolva um programa que receba um ano e determine se ele é bissexto. 
#Se for, informe que "O ano é bissexto e possui 366 dias." Caso contrário,
#informe que "O ano não é bissexto e possui 365 dias."  

ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto e possui 366 dias.")
else:
    print("O ano não é bissexto e possui 365 dias.")

    
