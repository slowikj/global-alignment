from typing import Dict


class IntConfigReader(object):

    def __init__(self):
        self.__config_attrs: Dict[str, int] = {}

    def get_attributes(self) -> Dict[str, int]:
        return self.__config_attrs

    def add_line(self, line: str):
        attr_key, attr_value = line.split(sep=" ", maxsplit=2)
        self.__raise_error_if_attr_repeats(attr_key)
        self.__config_attrs[attr_key] = int(attr_value)

    def __raise_error_if_attr_repeats(self, attr_key):
        if attr_key in self.__config_attrs:
            raise ValueError("{} is already in config".format(attr_key))
