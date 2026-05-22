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


class ReglaTransposicion(ReglaTransformacion):

    def partitura_valida(self, partitura: str) -> bool:

        errores = []

    numeros = self.encontrar_numeros_partitura(partitura)
    if numeros:
        errores.append(
            ContieneNumero(
                f"Números encontrados: {numeros}"
            )
        )

    invalidos = self.encontrar_caracteres_invalidos(partitura)
    if invalidos:
        errores.append(
            ContieneCaracterInvalido(
                f"Caracteres inválidos: {invalidos}"
            )
        )

    texto = partitura.lower().split()

    notas_validas = NOTAS + ["|", "-"]

    if not any(t in NOTAS for t in texto):
        errores.append(SinNotas("La partitura no tiene notas"))

    for t in texto:
        if t not in notas_validas:
            errores.append(
                ContieneCaracterInvalido(
                    f"Token inválido: {t}"
                )
            )
            break

    if errores:
        raise ExceptionGroup("Errores", errores)

    return True