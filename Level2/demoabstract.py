from abc import  ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def payment(self,amt):
        pass
    def gen_slip(self,amt):
        print(amt)
class CrediPayment(Payment):
    def payment(self,amt):
        print("Paid Amount Using Credit card",amt)
    def gen_slip(self,amt):
        print(amt)
class DebitCard(Payment):
    def payment(self,amt):
        print("Paid amount using Debit card",amt)
    def gen_slip(self,amt):
        print(amt)

obj=CrediPayment()
obj.payment(350)
obj.gen_slip(350)
