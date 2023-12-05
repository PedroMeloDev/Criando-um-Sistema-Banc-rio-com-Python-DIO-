inicio = ' Banco Pandora '
print(inicio.center(50, "="))
menu ='''
Selecione uma opção:

[1] Depositar.
[2] Sacar.
[3] Extrato.
[0] Sair ->.
'''
saldo = 0
limite = 500
extrato = f"Seu saldo inicial é de: R$ {saldo:.2f} \n"
LIMITE_SAQUES = 3
numero_saques = 0

while True:
  opcao = int(input(menu + '\n\n=> '))

  if opcao == 1:
    valor = float(input("Qual valor deseja depositar? R$ "))
    if valor > 0:
      saldo += valor
      extrato += f"VOCÊ DEPOSITOU: R$ {valor:.2f} \n"
    else:
      "Por favor, digite um valor válido para deposito."

  #Opção 1 Funcionando corretamente até aqui.   

  elif opcao == 2:
    numero_saques += 1
    if numero_saques > LIMITE_SAQUES:
      print("Você atingiu o limite de saques diário permitidos.")

    #VERIFICAR SE TEM SALDO
    elif saldo > 0:
      saque = float(input("Quanto deseja sacar? R$ "))
      # VERIFICANDO SE O VALOR É MAIOR QUE R$ 500,00
      if saque > 500:
        print('Por questão de segurança só é autorizado saques de até R$ 500,00')
      # VERIFICANDO SE O SAQUE É MAIOR DO QUE O SALDO
      elif saque > saldo:
          print(f"Você não tem esse valor disponível para saque. \nSeu Saldo Atual é de R$ {saldo:.2f}")
      # EFETUANDO UM SAQUE
      elif saque <= saldo:
        saldo -= saque
        extrato += f"VOCÊ SACOU: R$ {saque:.2f} \n"
        saques_restantes = LIMITE_SAQUES - numero_saques
        print(f"Você possui {saques_restantes} saques restantes") 
    else:
      print(f"Você não tem saldo suficiente!\nSeu Saldo Atual é de R$ {saldo:.2f}")

  elif opcao == 3:

    if extrato == "":
      print("Não foram realizadas transações")

    else:
      print(10*'.', "EXTRATO BANCÁRIO", 10*'.')
      print(extrato)
      print(25*"=","\n",f"Seu saldo atual é R$ {saldo:.2f}")

  elif opcao == 0:
    print("Obrigado por usar nosso sistema bancário! Volte sempre")
    break

  else:
    print("Opção inválida, por favor tente novamente!")