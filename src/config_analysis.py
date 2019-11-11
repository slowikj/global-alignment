from typing import Tuple, List, Dict


class IntConfigReader(object):

    def __init__(self):
        self.__config_attrs: Dict[str, int] = {}

    def get_attributes(self) -> Dict[str, int]:
        return self.__config_attrs

    def add_line(self, line: str):
        attr_key, attr_value = line.split(sep=" ", maxsplit=2)
        if attr_key in self.__config_attrs:
            raise ValueError("{} is already in config")
        self.__config_attrs[attr_key] = int(attr_value)
