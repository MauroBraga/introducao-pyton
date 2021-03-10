

class Conta:

    def __init__(self,numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de  {} de titular {}".format(self.__saldo,  self.__titular));

    def deposita(self, valor):
        self.__saldo += valor;

    def sacar(self, valor):
        self.__saldo -= valor;
    
    def transferir(self,valor, destino):
        self.sacar(valor);
        destino.deposita(valor);

    def get_saldo(self):
        return self.__saldo;

    def get_titular(self):
        return self.__titular;
   
    @property
    def limite(self):
        return self.__limite;

    def set_saldo(self,saldo):
        self.__saldo = saldo;

    def set_titular(self, titular):
        self.__titular = titular;

    @limite.setter
    def  limite(self, limite):
        self.__limite=limite;