from custom_types import NoReturn
class Department:
    def __init__(self, name: str) -> NoReturn:
        self.name = name

class Category:
    def __init__(self, name: str, department: Department) -> NoReturn:
        self.name = name
        self.department = department

class Product:
    def __init__(self, name: str, description: str, picture_urls: list,
                 price: float, category: Category) -> NoReturn:

        self.name = name
        self.description = description
        self.picture_urls = picture_urls
        self.price = price
        self.category = category



