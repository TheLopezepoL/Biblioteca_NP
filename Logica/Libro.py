LAST_ID = 0


class Libro:
    nombre: str
    id: int
    isDisponible: bool

    def __init__(self, pNombre: str):
        global LAST_ID
        self.nombre = pNombre
        LAST_ID += 1
        self.id = LAST_ID
        self.isDisponible = True
        return
