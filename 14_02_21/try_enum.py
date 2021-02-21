#Vachagan's version
from enum import Enum, auto
class NextInt:
    NUM = 0
    @classmethod
    def next(cls):
        cls.NUM += 1
        return cls.NUM

class AutoNumber(Enum):
    def _generate_next_value_(self, start, count, last_values):
        print('-',NextInt.next())

        return NextInt.next()

class Color(AutoNumber):
    red = auto()
    green = auto()
    blue = auto()
color1 = Color()
color2 = Color()
for name, member in color1.__members__.items():
    print(name, member.value)
for name, member in color2.__members__.items():
    print(name, member.value)