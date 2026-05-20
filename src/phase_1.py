class Discount:
    def __init__(self, amount, is_percentage = False):
        self.amount = amount
        self.is_percentage = is_percentage

class DiscountFactory:
    def create(self, amount, is_percentage = False):
        return Discount(amount, is_percentage)


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

