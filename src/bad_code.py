class Cart:
    def __init__(self):
        self.products = []
        self.total_price = None

    def add_product(self, product, price, discount = None):
        if discount is None:
            self.products.append(product)
            self.total_price += price
            return self.products, self.total_price
        elif discount == "DISCOUNT_10":
            self.products.append(product)
            self.total_price += 0.1 * price
            return self.products, self.total_price
        elif discount == "DISCOUNT_20":
            self.products.append(product)
            self.total_price += 0.2 * price
            return self.products, self.total_price
        elif discount == "DISCOUNT_30":
            self.products.append(product)
            self.total_price += 0.3 * price
            return self.products, self.total_price
        elif discount == "DISCOUNT_40":
            self.products.append(product)
            self.total_price += 0.4 * price
            return self.products, self.total_price
        else:
            return self.products, self.total_price

    def pay(self, payment_method):
        if payment_method == "CREDIT_CARD":
            print("Payment successful with credit card.")
        elif payment_method == "PAYPAL":
            print("Payment successful with PayPal.")
        elif payment_method == "BANK_TRANSFER":
            print("Payment successful with bank transfer.")
        else:
            print("Invalid payment method.")

