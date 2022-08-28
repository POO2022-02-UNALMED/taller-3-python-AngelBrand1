from mimetypes import init

class Marca:
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
