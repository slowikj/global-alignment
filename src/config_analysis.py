from typing import Tuple, List


class IntConfigReader(object):

    def __init__(self):
        self.__config_attrs: List[Tuple[str, object]] = []

    def get_attributes(self) -> List[Tuple[str, object]]:
        return self.__config_attrs

    def add_line(self, line: str):
        attr_key, attr_value = line.split(sep=" ", maxsplit=2)
        self.__config_attrs.append((attr_key, int(attr_value)))
