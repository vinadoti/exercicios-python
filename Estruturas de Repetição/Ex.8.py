# Escreva um programa Python para verificar a validade da senha inserida pelos usuários. Validação:
# Pelo menos 1 letra entre [a-z] e 1 letra entre [A-Z].
# Pelo menos 1 número entre [0-9].
# Pelo menos 1 caractere de [$ # @].
# Comprimento mínimo de 6 caracteres.
# Comprimento máximo 16 caracteres.

while True:
  senha= input('Digite sua senha: ');
 
  if len(senha) < 6 or len(senha) > 16:
     print('Tamanho inválido')

  contem_a_z = False
  contem_A_Z = False
  contem_simbolo = False 
  contem_numero = False

  for caractere in senha:
    if caractere.islower():
      contem_a_z = True
    if caractere.isupper():
      contem_A_Z = True
    if caractere == '$' or caractere == '#' or caractere == '@':
      contem_simbolo = True  
    if caractere.isnumeric():
      contem_numero = True  

  if contem_a_z and contem_A_Z and contem_simbolo and len(senha) >= 6 and len(senha) <= 16 and contem_numero:
    print('Senha válida')
    break 
  else:
    print('senha inválida')