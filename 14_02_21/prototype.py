import copy

class Template:
    def __init__(self, first_element, last_element, elements, private_elements):
        self.first_element = first_element
        self.last_element = last_element
        self.elements = elements
        self.__private_elements = private_elements

    def __str__(self):
        return f'{self.first_element}-{self.last_element}\n' \
               f'{self.elements}, {self.__private_elements}'

    def __copy__(self):
        private_prefix = f'_{self.__class__.__name__}__'
        copy_dict = {}
        for k, v in self.__dict__.items():
            if private_prefix in k:
                continue
            copy_dict[k] = v

        return Template(private_elements=[], **copy_dict)

    def __deepcopy__(self, memodict={}):
        pass

    def clone(self, **kwargs):
        private_prefix = f'_{self.__class__.__name__}__'
        copy_instance = copy.copy(self)
        for k, v in kwargs.items():
            if copy_instance.__dict__.get(private_prefix + k) is not None:
                del kwargs[k]
                kwargs[private_prefix + k] = v
        copy_instance.__dict__.update(kwargs)
        return copy_instance

class CopyManager:
    """ data_dict = {instance1: [kwargs1,kwargs2, ...], ...}"""
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def clone_instances(self):
        for instance, kwargs_list in self.data_dict.items():
            for kwargs in kwargs_list:
                yield instance.clone(**kwargs)


temp = Template(1, 2, [1, 2, 4, [2, 4]], [2, 3, 4, [5, 7]])
temp_copy = copy.copy(temp)
temp_deepcopy = copy.deepcopy(temp)
print(temp_copy)
print(temp_deepcopy)

temp.elements[0] = 0
temp.elements[3][0] = 0
temp.first_element = 9

print(temp)
print(temp_copy)
print(temp_deepcopy)

print('Clone with update')
data_to_copy = {temp: [{"first_element": 0, 'elements': [1, 2, 4]}, {"last_element": 23}]}
copy_manager = CopyManager(data_to_copy)
print(temp)

for cloned_temp in copy_manager.clone_instances():
    print(cloned_temp)
