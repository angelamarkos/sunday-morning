import types
type_function = types.FunctionType
import time

def execution_time(f):

    def wrap_f(*args, **kwargs):
        print(f"Start function {f.__name__}")
        start_time = time.time()
        value = f(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time for {f.__name__} is {end_time-start_time}')
        return value

    return wrap_f

def class_execution_time(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                attr = super().__getattribute__(item)
            except AttributeError:
                attr = self.instance.__getattribute__(item)
            else:
                if not callable(attr):
                    return attr

            return execution_time(attr)

    return NewCls

@class_execution_time
class Test:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add_a_b(self):
        return self.a + self.b

    def sub_c_b(self):
        return self.c - self.b

    def div_a_c(self):
        return self.a / self.c

test_1 = Test(1, 3, 5)

test_1.add_a_b()
test_1.sub_c_b()
test_1.div_a_c()
test_1.a
