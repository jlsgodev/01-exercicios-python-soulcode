# 13. Número de Tentativas para Senha 
# Descrição: Crie um programa que limite o número de tentativas para 
# digitar a senha correta.
# O usuário deve ter no máximo 3 tentativas. Use `while` e `if`.


senha_correta = "1234"
tentativas_maximas = 3
contar_tentativas = 0

while contar_tentativas < tentativas_maximas:
  senha = input("Digite a senha:")
  if senha == senha_correta:
    print("Acesso Autorizado")
    break
  else:
    contar_tentativas +=1
    if contar_tentativas < tentativas_maximas:
      print(f"Senha incorreta, tente novamente. Você tem {tentativas_maximas - contar_tentativas} tentativas restantes.")
    else:
      print("Número máximo de tentativas atingido. Acesso Bloqueado")



