class InitCarError(Exception):
    def __init__(self, *args: object) -> None:
        self.mensaje = "EL CARRO NO PUEDE INICIALIZAR EN ESTA POSICION"
        super().__init__(self.mensaje)


class LimitMapError(Exception):
    def __init__(self, *args) -> None:
        self.mensaje: str = "ESTAS SUPERANDO EL LIMITE DEL MAPA "
        super().__init__(self.mensaje)
