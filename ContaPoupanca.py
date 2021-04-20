from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):

    def __init__(self, numeroConta = '', tipoConta = '', valorConta = 0.0):
        self.__nrConta = numeroConta
        self.__idTpConta = tipoConta
        self._vrConta = valorConta
    
    @property 
    def nrConta(self):
        return self.__nrConta

    @nrConta.setter
    def nrConta(self, valor):
        if valor != '':
            self.__nrConta = valor
        else:
            print("Número de conta inválido")

    @property
    def idTpConta(self):
        return self.__idTpConta

    @idTpConta.setter
    def idTpConta(self, valor):
        if valor != 'CP':
            print("Nao é conta poupança, deverá abrir a conta por outro caminho.")
            self.__idTpConta = ''
        else:
            self.__idTpConta = valor
    
    @property
    def vrConta(self):
        return self._vrConta

    @vrConta.setter
    def vrConta(self, valor):
        if valor >= 100.00:
            self._vrConta += valor
        else:
            print("Conta Poupança deve iniciar com pelo menos R$100,00. Valor informado para setar:", valor)
    
    def cadastrar(self, numeroDaConta, contaCorrente):
        self.__nrConta = numeroDaConta
        self.__idTpConta = contaCorrente

    def depositar(self, valorDeposito):
        if valorDeposito > 100:
            self._vrConta += valorDeposito
        else:
            print("Valor mínimo para depósito em conta poupança é R$100,00. Tentativa de depósito:", valorDeposito)