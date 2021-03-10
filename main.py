class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            print('O atributo agencia deve ser maior que zero')
            return

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return

        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return
        self.__saldo = value

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


conta_corrente = ContaCorrente(None, 'agencia falsa', 22500)
conta_corrente.agencia = 0
print(conta_corrente.agencia)
