from abc import ABC,abstractmethod,abstractproperty
from calendar import c
from uuid import uuid4

class DollarMixin:

    def indiviuial_property(self):
        self.name="Dollar"
        self.symbol="$"

class EuroMixin:

    def indiviuial_property(self):
        self.name="Euro"
        self.symbol="Eu"

class RialMixin:

    def indiviuial_property(self):
        self.name="Rial"
        self.symbol="IR"



class Money(ABC):

    @abstractmethod
    def __init__(self, value) -> None:
        self.value=value

    @abstractproperty
    def Rate():
        pass


class Dollar(Money, DollarMixin):

    Rate = 1

    def __init__(self, value) -> None:
        super().__init__(value)
        self.indiviuial_property()


    # @property
    # def Rate(self):
    #     pass    

class Euro(Money, EuroMixin):

    Rate = 1.1

    def __init__(self, value) -> None:
        super().__init__(value)
        self.indiviuial_property()

class Rial(Money, RialMixin):

    Rate = 0.001

    def __init__(self, value) -> None:
        super().__init__(value)
        self.indiviuial_property()


class Creadit:

    def __init__(self,**kwarg) -> None:        
        self.__dict__.update(kwarg)


class Receipt:

    def __init__(self,**kwarg) -> None:        
        self.__dict__.update(kwarg)        
       

class Wallet:

    __id = None
    transactions = []
 
    @classmethod
    def __set_recovery(cls):

        question = input("enter a question:")
        answer = input("enter answer:")

        return {question:answer}

    def __new__(cls):
       
       if not hasattr(cls,"__instance"):
        cls.__instance = super().__new__(cls)
        cls.__id=str(uuid4()).split('-')[0]
        cls.money_packet = {}
        cls.creadit_packet = {}
        cls.receipt_packet = {}
        print(f"your code is {cls.__id} please store it")
        cls.__recovery = cls.__set_recovery()
        # return cls.__instance
    #    else:

    #       return cls.__instance

    @classmethod
    def __log(cls, value, kind):
        cls.transactions.append(f"{value} {kind} setted to wallet")

    @classmethod
    def history(cls):
        code = input("enter your code : ")
        if not cls.__id == code:
            raise Exception("you cant acsess")    

        else:
            for i in cls.transactions:
                print(i)    
    @classmethod
    def add_money(cls, money):
        if isinstance(money, Money):
            if money.name in cls.money_packet:
                cls.money_packet[money.name] += money.value
            else:
                cls.money_packet[money.name] = money.value  

            cls.__log(money.value,money.name)     

    @classmethod
    def add_creadit(cls, name, **kwargs):

         cls.creadit_packet[name] = kwargs
         cls.__log("",name)

    @classmethod
    def add_receipt(cls, name, **kwargs):

         cls.creadit_packet[name] = kwargs
         cls.__log("",name)     

    @classmethod
    def balance(cls):
        code = input("enter your code : ")
        if not cls.__id == code:
            raise Exception("not match")
        else:
            for i in cls.money_packet:
                print("we have :",i, cls.money_packet[i])   
            print(cls.creadit_packet) if cls.creadit_packet else \
                 print("no creadit")

            print(cls.receipt_packet) if cls.receipt_packet else \
                 print("no receipt")    


    @classmethod
    def recovery(cls):
        qusetion = input("enter your question : ")
        answer = input("enter answer : ")
        if cls.__recovery == {qusetion:answer}:
            print(cls.__id)
        else:
            raise Exception("doesnt match")    

    @classmethod
    def export(cls, name):
        code =  input("enter your code : ")
        if not cls.__id == code:
            raise Exception("doesnt match")

        else:
            if name in cls.creadit_packet:
                cls.creadit_packet.pop(name)
                cls.__log("delete",name)

Wallet()

Wallet.add_money(Dollar(100))
Wallet.add_money(Euro(100))
Wallet.add_money(Rial(100))
Wallet.add_money(Rial(10000))
Wallet.add_creadit("Melli",code=1224)
Wallet.balance()
Wallet.export("Melli")
Wallet.balance()
Wallet.history()