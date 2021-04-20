from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):

    def __init__(self, numeroConta = 0, tipoConta = '', valorConta = 0.0):
        self.__nrConta = numeroConta
        self.__idTpConta = tipoConta
        self._vrConta = valorConta

    @property 
    def nrConta(self):
        return self.__nrConta

    @nrConta.setter
    def nrConta(self, valor):
        if valor > 0:
            self.__nrConta = valor
        else:
            print("Número de conta inválido")

    @property
    def idTpConta(self):
        return self.__idTpConta

    @idTpConta.setter
    def idTpConta(self, valor):
        if valor != 'CC':
            print("Nao é conta corrente, deverá abrir a conta por outro caminho.")
            self.__idTpConta = ''
        else:
            self.__idTpConta = valor

    @property
    def vrConta(self):
        return self._vrConta

    @vrConta.setter
    def vrConta(self, valor):
        if valor > 0:
            self._vrConta += valor
        else:
            print("Valor inválido para setar em conta:", valor)

    def cadastrar(self, numeroDaConta, contaCorrente):
        self.__nrConta = numeroDaConta
        self.__idTpConta = contaCorrente

    def depositar(self, valorDeposito):
        if valorDeposito > 0:
            self._vrConta += valorDeposito
        else:
            print("Valor inválido para depósito:", valorDeposito)