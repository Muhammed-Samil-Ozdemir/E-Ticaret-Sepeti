from abc import ABC, abstractmethod

class CartService:
    def __init__(self):
        self.payment_method = None
        self.cart = Cart()
        self.payment_service = PaymentService()
        self.discount_factory = DiscountFactory()

    def add_product(self, product: Product):
        self.cart.add_product(product)
        return self

    def remove_product(self, product: Product):
        self.cart.remove_product(product)
        return self

    def apply_payment_method(self, payment_method: IPaymentMethod):
        self.payment_method = payment_method
        return self

    def pay(self):
        self.payment_service.pay(self.payment_method)
        return self

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











class IProduct(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

class ProductDecorator(IProduct, ABC):
    def __init__(self, product: IProduct):
        self._product = product

    def get_name(self) -> str:
        return self._product.get_name()

    def get_price(self) -> float:
        return self._product.get_price()

class LoggedProduct(ProductDecorator):
    def get_name(self) -> str:
        name = self._product.get_name()
        print(f"[LOG] get_name called → {name}")
        return name

    def get_price(self) -> float:
        price = self._product.get_price()
        print(f"[LOG] get_price called → {price}")
        return price

class PremiumProduct(ProductDecorator):
    def __init__(self, product: IProduct, surcharge: float = 0.0):
        super().__init__(product)
        self._surcharge = surcharge

    def get_name(self) -> str:
        return f"★ {self._product.get_name()}"

    def get_price(self) -> float:
        return self._product.get_price() + self._surcharge









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

class Product(IProduct):
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

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Discount:
    def __init__(self, amount, is_percentage = False):
        self.amount = amount
        self.is_percentage = is_percentage










class IPaymentChannel(ABC):
    @abstractmethod
    def process(self, amount: float, method_name: str):
        pass


class LiveChannel(IPaymentChannel):
    def process(self, amount: float, method_name: str):
        print(f"[LIVE] {method_name} {amount:.2f}")
        return True


class SandboxChannel(IPaymentChannel):
    def process(self, amount: float, method_name: str):
        print(f"[SANDBOX] {method_name} {amount:.2f}")
        return True


class MockChannel(IPaymentChannel):
    def __init__(self, always_succeed: bool = True):
        self._succeed = always_succeed

    def process(self, amount: float, method_name: str):
        print(f"[MOCK] {method_name} {'OK' if self._succeed else 'FAIL'}")
        return self._succeed

cart_service = CartService()
(cart_service.add_product(Product("Laptop", 1500))
            .add_product(Product("Mouse", 50))
            .apply_payment_method(CreditCardPayment())
            .pay())