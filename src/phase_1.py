from abc import ABC, abstractmethod

class Cart:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product: Product):
        self.products.append(product)
        self.total_price += product.price

    def remove_product(self, product: Product):
        self.products.remove(product)
        self.total_price -= product.price
        if self.total_price <= 0:
            self.total_price = 0

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount_factory = DiscountFactory()
        self.discount: Discount = None

    def set_discount(self, amount, is_percentage = False):
        self.discount = self.discount_factory.create(amount, is_percentage)
        self.set_price(self.price)

    def set_price(self, price):
        if self.discount is None:
            self.price = price
            return

        if not self.discount.is_percentage:
            self.price = price - self.discount.amount
            return

        self.price = price - (price * self.discount.amount / 100)

class Discount:
    def __init__(self, amount, is_percentage = False):
        self.amount = amount
        self.is_percentage = is_percentage

class CartService:
    def __init__(self):
        self.payment_method = None
        self.cart = Cart()
        self.payment_service = PaymentService()
        self.discount_factory = DiscountFactory()

    def add_product(self, product: Product):
        self.cart.add_product(product)

    def remove_product(self, product: Product):
        self.cart.remove_product(product)

    def apply_payment_method(self, payment_method: IPaymentMethod):
        self.payment_method = payment_method

    def pay(self):
        self.payment_service.pay(self.payment_method)

class PaymentService:
    def __init__(self):
        self.payment_method: IPaymentMethod = None

    def pay(self, payment_method: IPaymentMethod):
        self.payment_method = payment_method
        self.payment_method.pay()

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

