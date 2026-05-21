from abc import ABC, abstractmethod

class ReglaTransformacion(ABC):

    def __init__(self, token: int):
        self.token = token

    @abstractmethod
    def transformar(self, partitura: str) -> str:
        pass

    @abstractmethod
    def revertir(self, partitura: str) -> str:
        pass

    @abstractmethod
    def partitura_valida(self, partitura: str) -> bool:
        pass

    def encontrar_numeros_partitura(self, partitura: str) -> list:
        return [(i, c) for i, c in enumerate(partitura) if c.isdigit()]

    def encontrar_caracteres_invalidos(self, partitura: str) -> list:
        return [(i, c) for i, c in enumerate(partitura) if ord(c) > 127]