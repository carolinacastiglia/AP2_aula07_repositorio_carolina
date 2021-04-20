from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass=ABCMeta):

    @property
    def nrConta(self):
        pass

    @nrConta.setter
    @abstractmethod
    def nrConta(self, valor):
        pass

    @property
    def idTpConta(self):
        pass

    @idTpConta.setter
    @abstractmethod
    def idTpConta(self, valor):
        pass

    @property
    def vrConta(self):
        pass

    @vrConta.setter
    @abstractmethod
    def vrConta(self, valor):
        pass

    @abstractmethod
    def cadastrar(self, valorConta, valorTpConta):
        pass

    @abstractmethod
    def depositar(self, valorDepositado):
        pass