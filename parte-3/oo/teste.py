
from  conta import Conta;

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "titular":titular, "saldo":saldo, "limite": limite}
    return conta;

def deposita(conta, valor):
    conta["saldo"] += valor;

def saque(conta, valor):
    conta["saldo"] -= valor;

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]));



conta = Conta(123, "mauro",55.5, 1000.0);
conta2 = Conta(123, "nico",55.5, 1000.0);

print(conta.saldo)