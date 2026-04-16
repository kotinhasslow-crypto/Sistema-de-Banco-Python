# Conta dos cliente, classe MÃE
class Conta:
    def __init__(self, nome, cpf, saldo, tipo): # dados do cliente
        self.nome    = nome
        self.cpf     = cpf
        self._saldo = saldo
        self.tipo    = tipo

    def depositar(self, valor): # deposita um valor em dinheiro pro sistema
        if valor > 0:
            self._saldo += valor
        else:
            print(f'\033[31mQuantia inválida.\033[m')

    def sacar(self, valor): # retira uma quantia de dinheiro do sistema
        if valor > self._saldo:
            print(f'\033[31mSaldo insuficiente.\033[m')
        elif valor < 0:
            print(f'\033[31mQuantida inválida\033[m')
        else:
            self._saldo -= valor

    def ver_saldo(self): # Ve o saldo do cliente.
        print(f'\033[33mSaldo: R${self._saldo}\033[m')

# Conta corrente, boa para atividades do cotidiano, cobra 10R$ por saque
class ContaCorrente(Conta):
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print(f'\033[31mQuantia inválida.\033[m')

    def sacar(self, valor):
        if valor+10 > self._saldo:
            print(f'\033[31mSaldo Insuficiente.\033[m')
        elif valor < 0:
            print(f'\033[31mQuantia inválida.\033[m')
        else:
            self._saldo -= valor+10

    def ver_saldo(self):
        print(f'\033[33mSaldo: R${self._saldo}\033[m')

# Conta Poupança, boa pra deixar o dinheiro meio parado, rende 5% ao mes ( função render())
class ContaPoupanca(Conta):
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print(f'\033[31mQuantia inválida.\033[m')

    def sacar(self, valor):
        if valor > self._saldo:
            print(f'\033[31mSaldo Insuficiente.\033[m')
        elif valor < 0:
            print(f'\033[31mQuantia inválida.\033[m')
        else:
            self._saldo -= valor

    def render(self): # rende 5% do saldo
        self._saldo += self._saldo * 0.05

    def ver_saldo(self):
        print(f'\033[33mSaldo: R${self._saldo}\033[m')

class Banco:
    def __init__(self):
        self.lista = []

    def adicionar(self, cliente):
        self.lista.append(cliente)

    def listar(self):
        for c in self.lista:
            print(f'Nome: {c.nome} | CPF: {c.cpf}')

    def buscar(self, cpf):
        for c in self.lista:
            if c.cpf == cpf:
                print(f'Nome: {c.nome}')

banco = Banco()
adm   = Conta('ADM', 101, 1000000, 'ADM')
banco.adicionar(adm)

while True:
    print('Digite seu CPF: ')
    cpf_buscar = int(input(''))

    # CONTA DO ADM
    if cpf_buscar == 101:
        print('Abrindo painel adm...')
        print(f'1. Listar clientes\n2. Buscar clientes\n0. sair')
        escolha1 = int(input(''))
        if escolha1 == 0:
            break

        # Listar todos os clientes
        if escolha1 == 1:
            banco.listar()

        # Busca clientes especificos pelo CPF
        if escolha1 == 2:
            buscar_cliente = int(input('Digite o CPF do cliente que deseja buscar: '))
            banco.buscar(buscar_cliente)
        continue


    # aprendizado ai ( ajuda do Claude )
    conta_encontrada = None
    for c in banco.lista:
        if c.cpf == cpf_buscar:
            conta_encontrada = c
            break

    # percorre a lista, se achar, guarda a conta e abre o painel
    # se não achar, fica None, 

    # se for NONE, ele vai pra criação de contas
    if conta_encontrada is None:
        print(f'CPF não encontrado...')
        print(f'Deseja criar qual tipo de conta?\n1. Conta Corrente\n\033[34m( Conta normal, cobramos 10R$ de taxa por saque )\033[m\n2. Conta Poupança\n\033[34m( Conta normal, tem opção de renda, que aumenta seu saldo em 5%. )\033[m')
        escolha2 = int(input(''))
        
        # lista com as opções
        contas = {1:ContaCorrente, 2:ContaPoupanca}
        conta_escolhida = contas[escolha2]

        nome_registro  = str(input('Digite seu nome: '))
        cpf_registro   = int(input('Digite seu CPF: '))
        saldo_registro = 0
        if escolha2 == 1:
            tipo_conta = 'ContaCorrente'
        else:
            tipo_conta = 'ContaPoupanca'

        cliente_conta  = conta_escolhida(nome_registro, cpf_registro, saldo_registro, tipo_conta)
        banco.adicionar(cliente_conta)


    if conta_encontrada is not None:
        c = conta_encontrada
        print(f'CPF já cadastrado, entrando na conta...')
        if c.tipo == 'ContaCorrente':
            print(f'1. Depositar dinheiro\n2. Sacar dinheiro\n3. Ver saldo\n0. Sair')
            escolha3 = int(input(''))
            if escolha3 == 0:
                break
            if escolha3 == 1:
                valor_depositar_corrente = float(input('Quanto deseja depositar: '))
                c.depositar(valor_depositar_corrente)
            if escolha3 == 2:
                valor_sacar_corrente = float(input('Quanto deseja sacar: '))
                c.sacar(valor_sacar_corrente)
            if escolha3 == 3:
                c.ver_saldo()
        
        if c.tipo == 'ContaPoupanca':
            print(f'1. Depositar dinheiro\n 2. Sacar dinheiros\n3. Render\n4. Ver saldo\n0. Sair')
            escolha4 = int(input(''))
            if escolha4 == 0:
                break
            if escolha4 == 1:
                valor_depositar_poupanca = float(input('Quando deseja depositar: '))
                c.depositar(valor_depositar_poupanca)
            if escolha4 == 2:
                valor_sacar_poupanca = float(input('Quanto deseja sacar: '))
                c.sacar(valor_sacar_poupanca)
            if escolha4 == 3:
                c.render()
            if escolha4 == 4:
                c.ver_saldo()
