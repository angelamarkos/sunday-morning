from enum import (Enum,
                  IntEnum,
                  IntFlag,
                  auto,
                  EnumMeta)

class AutoMeta(EnumMeta):
    last_value = 1
    def __call__(cls, *args, **kwargs):
        members = cls.__members__.keys()
        last_value = cls.last_value
        new_cls = super().__call__(value=super().__name__,
                         names=', '.join(members),
                         start=cls.last_value)
        cls.last_value = cls.last_value + len(members)
        print(new_cls.last_value)

        return new_cls

    @staticmethod
    def _get_mixins_(bases):
        """Returns the type for creating enum members, and the first inherited
        enum class.

        bases: the tuple of bases that was given to __new__

        """
        if not bases:
            return object, Enum

        # double check that we are not subclassing a class with existing
        # enumeration members; while we're at it, see if any other data
        # type has been mixed in so we can use the correct __new__
        member_type = first_enum = None

        # base is now the last base in bases
        if not issubclass(bases[-1], Enum):
            raise TypeError("new enumerations must be created as "
                    "`ClassName([mixin_type,] enum_type)`")

        # get correct mix-in type (either mix-in type of Enum subclass, or
        # first base if last base is Enum)
        if not issubclass(bases[0], Enum):
            member_type = bases[0]     # first data type
            first_enum = bases[-1]  # enum type
        else:
            for base in bases[0].__mro__:
                # most common: (IntEnum, int, Enum, object)
                # possible:    (<Enum 'AutoIntEnum'>, <Enum 'IntEnum'>,
                #               <class 'int'>, <Enum 'Enum'>,
                #               <class 'object'>)
                if issubclass(base, Enum):
                    if first_enum is None:
                        first_enum = base
                else:
                    if member_type is None:
                        member_type = base

        return member_type, first_enum

class Color(IntEnum, metaclass=AutoMeta):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()


color_1 = Color()
color_2 = Color()
color_3 = Color()


print(color_1.RED.value)
print(color_2.RED.value)
print(color_3.RED.value)


for name, member in color_1.__members__.items():
    print(name, member.value)

for member in color_2:
    print(member.name, member.value)

member_1 = color_1.RED
member_2 = color_1.BLUE

print(member_1 != member_2)
print(member_1 > member_2)


class Permission(IntFlag):
    READ = 1
    WRITE = 2
    CLOSE = 3
    APPEND = 4
    EXECUTION = 6

permission_1 = Permission.READ
permission_2 = Permission.APPEND

permission_3 = Permission.READ | Permission.WRITE
permission_4 = Permission.READ + Permission.WRITE

# print(permission_1)
# print(permission_2)
# print(permission_3)
# print(permission_4)
# print(permission_1.value)
# print(Permission.R_W.value)
# print(permission_1 in permission_3)

# print(Permission.R_W.value & Permission.R_W.value == permission_1.value)
# print(Permission.__members__.items())
# print(Permission.R_W in Permission.EXECUTION)
# if permission_3 > Permission.R_W:
#     pass

class ResponseStatus(IntEnum):
    BAD_REQUEST = 400
    BAD_GATWAY = 500
    SUCCESS = 200

import requests
response = requests.get('https://www.google.com')
if response.status_code < ResponseStatus.BAD_REQUEST:
    print(response.content)
else:
    print(response.text)
