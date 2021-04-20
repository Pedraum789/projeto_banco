import datetime

def um():   #Função para criar uma conta nova
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    print("Tipos de conta:\nSalário\nComum\nPlus")
    conta = input("Digite um tipo de conta: ")
    if (conta == "Salário") or (conta == "salário") or (conta == 'Comum') or (conta == 'comum') or (conta == 'Plus') or (conta == 'plus') :
        #Caso ele escreva errado irá para o else criado. Se não ele continua o programa de criar conta.
        valor = float(input("Valor inicial da conta: "))
        senha = input("Senha do usuário: ")
        opcao_1 = open("{}.txt".format(cpf), "w")   #Conta para ver, usuário, senha, valores, cpf e tipo de conta

        Contas = open("{}_transacoes.txt".format(cpf), "w") #Onde vai ficar para mostrar as transações(Visual).
        #Basicamente, terão 2 arquivos de texto, 1 para o usuário ver(cpf_transacoes.txt) e outro para o programa entender e usarmos os dados.(cpf.txt).
        opcao_1.write("{}\n".format(nome))  #Adicionando no arquivo no cpf.txt
        opcao_1.write("{}\n".format(cpf))
        opcao_1.write("{}\n".format(conta))
        opcao_1.write("{}\n".format(senha))
        opcao_1.write("{}\n".format(valor))
        opcao_1.close()

        Contas.write("Nome: {}\n".format(nome)) #Adicionando o arquivo no cpf_transacoes.txt
        Contas.write("CPF: {}\n".format(cpf))
        Contas.write("Conta: {}\n".format(conta))
        Contas.write("Valor inicial: R${:.2f}\n".format(valor))

        Contas.close()
        print("Sua conta foi criada.")  #Avisar que foi criada
    else:
        print("Tipo de conta inválida.") #Caso o usuário não escreva certo os tipos de contas

def dois(): #Função para apagar conta
    import os
    remover = input("Digite o CPF da conta que deseja apagar: ")    #Apaga pelo cpf.
    os.remove("{}.txt".format(remover)) #Como o nome do texto é o CPF, então fica mais facil apaga-lo. O mesmo para o das transações.
    os.remove("{}_transacoes.txt".format(remover))  #Ele apaga direto pelo cpf da pessoa.
    print("A conta do CPF: {} foi apagada.".format(remover)) #Avisar que foi apagada

def tres(): #Função para Debitar
    cpf_solicitado = input("Digite o CPF: ")
    senha_solicitada = input("Digite a senha: ")
    validacao = open("{}.txt".format(cpf_solicitado), "r")
    
    Contas_1 = [] #Matriz para ler os valores do arquivo cpf.txt para fazer as contas e verificar o cpf e senha se estão corretos.

    for i in validacao.readlines(): #Adicionando o que tem dentro do arquivo cpf.txt dentro da matriz Contas_1
        Adicionar = i.split()
        Contas_1.append(Adicionar)

    if (Contas_1[1][0] == cpf_solicitado) and (Contas_1[3][0] == senha_solicitada) : #Condição para ver se a senha e o cpf estão certos
        valor = float(input("Digite o valor do débito: "))
        if Contas_1[2][0] == "Salário" or Contas_1[2][0] == "salário":  #Condição conta salário
            tarifa = 0.05
            Total = float(Contas_1[-1][0])  #Está como -1 pois sempre ele será adicionado para o ultimo lugar no cpf.txt(O ultimo valor), então sempre irá pegar o ultimo valor.
            Total -= (valor + (valor * tarifa)) #Conta total
            if Total < 0:   #Como a conta Salário não pode saldos negativos, coloquei Total < 0 ele não faz, senão ele faz a transação.
                print("Essa transação não pode ser feita, SALDO MENOR QUE R$0,00.")
            else:#Nesse else Abrir o arquivo de texto digitado pelo usuário. e aconta visual, depois colocando a variavel time, para marcar o tempo, para depois no extrato, aparecer tudo.
                Atualiza = open("{}.txt".format(cpf_solicitado), "a")#Conta para ver, usuário, senha, valores, cpf e tipo de conta
                Atualiza.write("{}\n".format(Total))    #Adicionando o ultimo valor no cpf.txt
                Atualiza.close()
                Contas = open("{}_transacoes.txt".format(cpf_solicitado), "a")  #Conta visual
                time = datetime.datetime.now()
                Contas.write("Data: {}-{}-{}...{}:{}..+..R${:.2f}..Tarifa:..{}..Saldo:..R${:.2f}\n".format(time.year, time.month, time.day, time.hour, time.minute, valor, tarifa, Total))
                #Escrevi na conta visual o valor e já atualizei na variavel Atualiza o valor no final do arquivo txt do cpf do usuário.
                Contas.close()
                print("Seu débito foi feito.")

        elif Contas_1[2][0] == "Comum" or Contas_1[2][0] == "comum":    #Condição conta comum
            tarifa = 0.03
            Total = float(Contas_1[-1][0])  #Está como -1 pois sempre ele será adicionado para o ultimo lugar, então sempre irá pegar o ultimo valor.
            Total -= (valor + (valor * tarifa))
            if Total < -500:    #Como a conta Comum não pode saldos negativos, coloquei Total < 500 ele não faz, senão ele faz a transação.
                print("Essa transação não pode ser feita, SALDO MENOR QUE R$500,00")
            else:
                Atualiza = open("{}.txt".format(cpf_solicitado), "a") #Conta para Adicionar para o ultimo valor
                Atualiza.write("{}\n".format(Total))
                Atualiza.close()
                Contas = open("{}_transacoes.txt".format(cpf_solicitado), "a") #Conta visual
                time = datetime.datetime.now()
                Contas.write("Data: {}-{}-{}...{}:{}..+..R${:.2f}..Tarifa:..{}..Saldo:..R${:.2f}\n".format(time.year, time.month, time.day, time.hour, time.minute, valor, tarifa, Total))
                #Escrevi na conta visual o valor e já atualizei na variavel Atualiza o valor no final do arquivo txt do cpf do usuário.
                Contas.close()
                print("Seu débito foi feito.")

        elif Contas_1[2][0] == "Plus" or Contas_1[2][0] == "plus":  #Condição conta plus
            tarifa = 0.01
            Total = float(Contas_1[-1][0])  #Está como -1 pois sempre ele será adicionado para o ultimo lugar, então sempre irá pegar o ultimo valor.
            Total -= (valor + (valor * tarifa))
            if Total < -5000:   #Como a conta Plus não pode saldos negativos, coloquei Total < 5000 ele não faz, senão ele faz a transação.
                print("Essa transação não pode ser feita, SALDO MENOR QUE R$5000,00")
            else:
                Atualiza = open("{}.txt".format(cpf_solicitado), "a")
                Atualiza.write("{}\n".format(Total))    #Adicionando o valor total no arquivo cpf.txt
                Atualiza.close()
                Contas = open("{}_transacoes.txt".format(cpf_solicitado), "a") #Conta visual
                time = datetime.datetime.now()
                Contas.write("Data: {}-{}-{}...{}:{}..+..R${:.2f}..Tarifa:..{}..Saldo:..R${:.2f}\n".format(time.year, time.month, time.day, time.hour, time.minute, valor, tarifa, Total))
                #Escrevi na conta visual o valor e já atualizei na variavel Atualiza o valor no final do arquivo txt do cpf do usuário.
                Contas.close()
                print("Seu débito foi feito.")
    else:
        print("CPF ou senha incorretas.")   #Caso o cpf esteja incorreto

def quatro():   #Função para fazer o depósito
    cpf_solicitado = input("Digite o CPF para depósito: ")
    validacao = open("{}.txt".format(cpf_solicitado), "r")
    
    Contas_1 = []

    for i in validacao.readlines(): #Abrir o arquivo do cpf.txt do usuário na lista Contas_1 para conferir depois.
        Adicionar = i.split()
        Contas_1.append(Adicionar)

    valor_solicitado = float(input("Digite o valor para depósito: "))
    tarifa = 0.00
    Total = float(Contas_1[-1][0])  #Ele pega o ultimo valor colocado no cpf.txt.
    Total += valor_solicitado   #Fazendo a soma para adicionar.
    Atualiza = open("{}.txt".format(cpf_solicitado), "a")
    Atualiza.write("{}\n".format(Total))    #Adicionando o novo saldo no cpf.txt
    Atualiza.close()
    Contas = open("{}_transacoes.txt".format(cpf_solicitado), "a")
    time = datetime.datetime.now()
    Contas.write("Data: {}-{}-{}...{}:{}..+..R${:.2f}..Tarifa:..{}..Saldo:..R${:.2f}\n".format(time.year, time.month, time.day, time.hour, time.minute, valor_solicitado, tarifa, Total))
    #Escrevi na conta visual(cpf_transacoes.txt) o valor e já atualizei no cpf.txt o valor do novo saldo(Linha 121).
    Contas.close()
    print("Seu depósito foi feito.")    #Avisando que o depósito foi feito


def cinco():    #Função que mostra o saldo.
    cpf_solicitado = input("Digite o CPF para ver o saldo: ")
    senha_solicitada = input("Digite a senha para ver o saldo: ")
    validacao = open("{}.txt".format(cpf_solicitado), "r")
    
    Contas_1 = []   #Lista para receber os valores do cpf.txt e mostrar o ultimo valor

    for i in validacao.readlines(): #Abrindo a conta em uma lista
        Adicionar = i.split()
        Contas_1.append(Adicionar)
    
    inteiro = float(Contas_1[-1][0]) #recebe o valor inteiro

    if (Contas_1[1][0] == cpf_solicitado) and (Contas_1[3][0] == senha_solicitada) :    #Condição para cpf e senha corretos
        print("O saldo da conta com cpf: {} é de: R${:.2f}".format(cpf_solicitado, inteiro))
        #Como ele sempre adiciona o novo saldo no ultimo ponto, ele usa o -1 para encontrar sempre o novo saldo.

    else:
        print("CPF ou senha inválidas.")

def seis(): #Função que mostra o extrato(Os arquivos cpf_transacoes.txt foram feitos justamente para mostrar visualmente mais bonito.)
    cpf_solicitado = input("Digite o CPF para ver o saldo: ")
    senha_solicitada = input("Digite a senha para ver o saldo: ")
    validacao = open("{}.txt".format(cpf_solicitado), "r")
    Contas = open("{}_transacoes.txt".format(cpf_solicitado), "r")
    
    Contas_1 = []   #Lista para receber os valores de cpf.txt
    Contas_2 = []   #Lista para receber os valores de cpf_transacoes.txt
    
    for i in validacao.readlines(): #Adicionando o cpf.txt na lista Conta_1.txt para fazer a validação do cpf e da senha.
        Adicionar = i.split()
        Contas_1.append(Adicionar)

    for i in Contas.readlines(): #Adicionando o cpf_transacoes.txt na lista Contas_2.txt para ler as transações depois.
        Adicionar = i.split()
        Contas_2.append(Adicionar)
    
    if (Contas_1[1][0] == cpf_solicitado) and (Contas_1[3][0] == senha_solicitada): #Usado o Contas_1 para fazer a validação do CPF e senha
        for lista in Contas_2:
            for elemento in lista:
                print(elemento,end='')  #Impressão do arquivo: cpf_transacoes.txt
            print()
    else:
        print("CPF ou senha incorretas.")


while True:

    print()
    print("1 - Novo Cliente")
    print("2 - Apaga Cliente")
    print("3 - Debita")
    print("4 - Deposita")
    print("5 - Saldo")
    print("6 - Extrato")
    print()
    print("0 - Sair")

    Escolha = int(input("Digite a escolha desejada: ")) #Pede ao usuário digitar uma das opções

    if (Escolha == 0):  #Se for digitado 0 ele sai da repetição com o break
        print("Obrigado por ter usado nosso serviço!")
        break

    elif (Escolha == 1):    #Se for digitado 1 ele chama a função
        um()

    elif (Escolha == 2):    #Se for digitado 2 ele chama a função
        dois()

    elif (Escolha == 3):    #Se for digitado 3 ele chama a função
        tres()

    elif (Escolha == 4):    #Se for digitado 4 ele chama a função
        quatro()

    elif (Escolha == 5):    #Se for digitado 5 ele chama a função
        cinco()

    elif (Escolha == 6):    #Se for digitado 6 ele chama a função
        seis()

    else:
        print("Opção inválida, digite novamente.")