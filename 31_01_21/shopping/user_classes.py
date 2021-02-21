import datetime
from products_classes import Department
from custom_types import DatetimeType
from custom_types import NoReturn

class Card:
    def __init__(self, cardholder_name: str, card_number: str, expiration_date: str,
                 cvv_cvc: str) -> NoReturn:

        self.cardholder_name = cardholder_name
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv_cvc = cvv_cvc
        self.type = self.get_type()

    def get_type(self):
        return 'VISA'

    def __str__(self):
        return f'{self.cardholder_name} \n' \
               f'{self.card_number[-4:]:*>16}\n' \
               f'{self.expiration_date}\n' \
               f'{self.type}'


    def to_dict(self):
        return self.__dict__


card = Card('Full name', '1223122312351234', '05/24', '123')
print(card)
print(card.to_dict())

class Address:
    def __init__(self, country, state, city, address_1, address_2, zipcode):
        self.country = country
        self.state = state
        self.city = city
        self.address_1 = address_1
        self.address_2 = address_2
        self.zipcode = zipcode

    def __str__(self):
        return f'{self.address_1}, {self.zipcode}, {self.city}, {self.state}, {self.country}'

    def __add__(self):

address = Address('USA', 'Californa', 'LA', 'Street 1','Street 2', '12345')
print(address)

class User:
    def __init__(self, full_name: str, email: str, password: str, gender: str,
                 birth_date: DatetimeType) -> NoReturn:
        self.full_name = full_name
        self.email = email
        self.__password = password
        self.gender = gender
        self.birth_date = birth_date

    def set_password(self, value):
        pass

    def get_info(self, value):
        pass

    def login(self):
        pass

class Customer(User):
    def __init__(self, full_name: str, email: str, password: str, gender: str, birth_date: DatetimeType,
                 card: Card, shipping_address: Address, billing_address: Address, phone_number: int) -> NoReturn:
        super().__init__(full_name, email, password, gender, birth_date)
        self.card = card
        # self.shipping_method = shipping_address
        # self.billing_address = billing_address
        self.phone_number = phone_number
        self.__currency = 'USD'

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value

    def get_addresses(self):
        return

class VipCustomer(Customer):
    def __init__(self, full_name: str, email: str, password: str, gender: str, birth_date: DatetimeType,
                 card: Card, shipping_address: Address, billing_address: Address, phone_number: int,
                 discount: int, free_shipping: bool, cupon: int) -> NoReturn:
        super().__init__(full_name, email, password, gender, birth_date,
                         card, shipping_address, billing_address, phone_number)

        self.discount = discount
        self.free_shipping = free_shipping
        self.cupon = cupon


class Admin(User):
    def __init__(self,full_name: str, email: str, password: str, gender: str, birth_date: DatetimeType,
                 department: Department) -> NoReturn:
        super().__init__(full_name, email, password, gender, birth_date)
        self.department = department


user = User('Name', 'email@s.sd', 'pass', 'female', datetime.datetime(1999, 1, 1))


