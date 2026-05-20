class IPaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(IPaymentMethod):
    def pay(self):
        print("payed with credit card")

class PaypalPayment(IPaymentMethod):
    def pay(self):
        print("payed with paypal")

class BankTransferPayment(IPaymentMethod):
    def pay(self):
        print("payed with bank transfer")

