# 10. Verificação de Senha Segura com Requisitos Adicionais  
# Problema:  Desenvolva um programa que receba uma senha e verifique se ela é segura. 
# Uma senha é considerada segura se tiver pelo menos 8 caracteres, incluir pelo menos uma letra maiúscula, uma letra minúscula, 
# um número e um caractere especial (como !, @, #). Informe se a senha é segura ou não e liste quais requisitos estão faltando. 




# Solicitando a senha ao usuário
senha = input("Digite a senha: ")

# Requisitos da senha
comprimento = len(senha) >= 8
maiuscula = False
minuscula = False
numero = False
especial = False

# Verificar cada caractere da senha
for caractere in senha:
    if caractere.isupper():
        maiuscula = True
    elif caractere.islower():
        minuscula = True
    elif caractere.isdigit():
        numero = True
    elif caractere in "!@#$%^&*(),.?\":{}|<>":
        especial = True

# Verificar se todos os requisitos são atendidos
segura = comprimento and maiuscula and minuscula and numero and especial

# Listar os requisitos faltando
requisitos_faltando = []
if not comprimento:
    requisitos_faltando.append("comprimento")
if not maiuscula:
    requisitos_faltando.append("maiuscula")
if not minuscula:
    requisitos_faltando.append("minuscula")
if not numero:
    requisitos_faltando.append("numero")
if not especial:
    requisitos_faltando.append("especial")

# Exibindo o resultado
if segura:
    print("A senha é segura.")
else:
    print("A senha não é segura. Requisitos faltando:")
    for requisito in requisitos_faltando:
        print(f"- {requisito}")
