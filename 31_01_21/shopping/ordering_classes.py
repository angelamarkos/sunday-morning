from custom_types import DatetimeType
from custom_types import NoReturn
from user_classes import Customer, Address, Card
from products_classes import Product

class Shipping:
    def __init__(self, shipping_type: str, cost: float, delivery_interval: tuple) -> NoReturn:
        self.shipping_type = shipping_type
        self.cost = cost
        self.delivery_interval = delivery_interval


class ShoppingList:
    def __init__(self, customer: Customer, product: Product, count: int) -> NoReturn:
        self.customer = customer
        self.product = product
        self.count = count


class Order:
    def __init__(self, shopping_list: list, shipping_method: Shipping, shipping_address: Address,
                 billing_method: str, billing_info: Card, status: str) -> NoReturn:
        self.shopping_list = shopping_list
        self.shipping_method = shipping_method
        self.shipping_address = shipping_address
        self.billing_method = billing_method
        self.billing_info = billing_info
        self.status = status
