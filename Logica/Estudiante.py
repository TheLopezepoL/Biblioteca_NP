import Libro

LAST_CARNET = 0


class Estudiante:
    # Informacion del estudiante
    nombre: str
    carnet: int
    librosPrestado: list
    moroso: bool

    # Inicio de sesion
    usuario: str
    contrasenha: str

    def __init__(self, pNombre: str, pUsuario: str, pContrasenha: str):
        global LAST_CARNET
        self.nombre = pNombre
        LAST_CARNET += 1
        self.carnet = LAST_CARNET
        self.librosPrestado = []
        self.moroso = False

        self.usuario = pUsuario
        self.contrasenha = pContrasenha
        return

    def changeMorosidad(self):
        if self.moroso:
            self.moroso = False
        else:
            self.moroso = True
        return

    def validarUsuario(self, pUsuario: str, pContrasenha: str):
        return self.usuario == pUsuario and self.contrasenha == pContrasenha

    def registrarPrestamoLibro(self, pLibro: Libro):
        if not self.moroso:
            pLibro.isDisponible = False
            self.librosPrestado.append(pLibro)
            return True
        else:
            return False

    def devolverLibro(self, pLibroID: int):
        libroxdevolver: Libro = None
        for libro in self.librosPrestado:
            if libro.id == pLibroID:
                libro.isDisponible = True
                libroxdevolver = libro
                self.librosPrestado.remove(libro)
                break
        return libroxdevolver
