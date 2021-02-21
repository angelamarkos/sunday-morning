from abc import ABC, abstractmethod

# class Prototype(ABC):
#     @abstractmethod
#     def clone(self):
#         pass
#
#
class Config():
    def __init__(self, log_path, microservice_1_ip, microservice_2_ip, database_configs: dict = {}):
        self.log_path = log_path
        self.microservice_1_ip = microservice_1_ip
        self.microservice_2_ip = microservice_2_ip
        self.database_configs = database_configs

    def __str__(self):
        return f'{self.log_path} \n {self.microservice_1_ip}, {self.microservice_2_ip} \n' \
               f'{self.database_configs}'


class Prototype:
    def __init__(self, objects_to_update : dict, class_name: object):
        self.__objects_to_clone = objects_to_update
        self.class_name = class_name

    def clone(self, object, **kwargs):
        copy_object = self.class_name(**{**object.__dict__, **kwargs})
        return copy_object

    def copy_objects(self):
        for obj, kwargs_list in self.__objects_to_clone.items():
            for kwargs in kwargs_list:
                yield self.clone(obj, **kwargs)


config_to_clone = Config('\logs\dev', '123.45.67.12', '100.45.0.12', {"username": 'user',
                                                             "password": '1d2We32',
                                                             'database': "employee",
                                                             "host": "12.5.45.4",
                                                             "posr": "1345"})

print(config_to_clone)

prototype = Prototype({config_to_clone: [{"microservice_2_ip": '123.9.34.4'},
                                         {"microservice_1_ip": '198.0.0.4'}]}, Config)

for config in prototype.copy_objects():
    print(config)
