from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

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

print("\n-------CONTA POUPANÇA-------\n")
cp1 = ContaPoupanca()
cp1.nrConta = '1987-2'
cp1.idTpConta = 'CP'
print("Número da conta:", cp1.nrConta)
print("Tipo de conta:", cp1.idTpConta)

cp2 = ContaPoupanca()
cp2.cadastrar('6528-2','CP')
print("\nConta cadastrada (",cp2.idTpConta,"):", cp2.nrConta)

print("\nDEPÓSITO CONTA Nº", cp1.nrConta)
cp1.vrConta = 0.0

print("\nDEPÓSITO CONTA Nº",cp2.nrConta)
cp2.depositar(25.89)
cp2.depositar(150.00)
print("Valor atual em conta (", cp2.nrConta,"):",cp2.vrConta)
cp2.depositar(101.00)
print("Valor atual em conta (", cp2.nrConta,"):",cp2.vrConta)