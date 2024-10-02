menu = '''
========= BEM VINDO! =========
   DIGITE A OPÇÃO DESEJADA:
  
    [1] Depositar;
    [2] Sacar;
    [3] Extrato;
    [0] Sair.

    => '''


#DADOS DA CONTA#
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


#FUNCOES DE CONTA
def funcao_depositar ():
    global saldo, extrato
    valor = float(input("Digite valor a depositar: "))

    if valor >0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print(f"Valor de R${valor: .2f} depositado com sucesso!")
    else:
        print("Valor Inválido! Tente Novamente: ")


def funcao_saque ():
    global saldo, extrato, numero_saques
    valor = float(input("Digite valor a sacar: "))

    excesso_saques = numero_saques >= LIMITE_SAQUES
    saldo_insuficiente = valor > saldo
    limite_saque = valor > 500

    if excesso_saques:
        print("Limite diário de 3 saques atingido.")
    elif limite_saque:
        print("Valor limite por saque excedido.")
    elif saldo_insuficiente:
        print(f"Saldo insuficiente. Valor disponível: R$ {saldo: .2f}.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor: .2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor: .2f} realizado com sucesso!")
    else:
        print('Valor inválido! Tente novamente.')


#FUNCIONALIDADE CONTA
while True:
    
    opcao = input(menu)

    if opcao == '1':
        funcao_depositar()
    
    elif opcao == '2':
        funcao_saque()
    
    elif opcao == '3':
        print("\n========= EXTRATO =========")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo: .2f}")
        print(f"\nQtd de saques disponíveis: {LIMITE_SAQUES - numero_saques}")
        print("=============================\n")
    
    elif opcao =='0':
        print("Obrigado por utilizar nosso serviço bancário.")
        break

    else:
        print('Opção inválida. Selecione opção desejada!')


