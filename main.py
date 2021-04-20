from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente

print("-------CONTA CORRENTE-------\n")
cc1 = ContaCorrente()
cc1.nrConta = 34
cc1.idTpConta = 'CC'
print("Número da conta:", cc1.nrConta)
print("Tipo de conta:", cc1.idTpConta)

cc2 = ContaCorrente()
cc2.cadastrar(23,'CC')
print("\nConta cadastrada (",cc2.idTpConta,"):", cc2.nrConta)

print("\nDEPÓSITO CONTA Nº", cc1.nrConta)
cc1.vrConta = 0.0

print("\nDEPÓSITO CONTA Nº",cc2.nrConta)
cc2.depositar(25.89)
print("Valor atual em conta (", cc2.nrConta,"):",cc2.vrConta)
cc2.depositar(0.0)