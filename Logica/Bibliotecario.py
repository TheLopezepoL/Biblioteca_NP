from Logica import Estudiante


class Bibliotecario:
    libros: list
    escuelas: list

    def __init__(self):
        self.libros = []
        self.escuelas = []
        return

    def validarUsuario(self, pUsuario: str, pContrasenha: str):
        for escuela in self.escuelas:
            for estudiante in escuela.estudiantes:
                if estudiante.validarUsuario(pUsuario, pContrasenha):
                    return True
        return False

    def returnEstudianteXID(self, pEstudianteID: int):
        for escuela in self.escuelas:
            for estudiante in escuela.estudiantes:
                if estudiante.carnet == pEstudianteID:
                    return estudiante
        return None

    def returnLibroXID(self, pLibroID: int):
        for libro in self.libros:
            if libro.id == pLibroID:
                return libro
        return None

    def realizarPrestamo(self, pEstudianteID: int, pLibroID: int):
        estudiante = self.returnEstudianteXID(pEstudianteID)
        libro = self.returnLibroXID(pLibroID)
        if estudiante is not None and libro is not None:
            if libro.isDisponible:
                if estudiante.registrarPrestamoLibro(libro):
                    libro.isDisponible = False
                else:
                    print("Estudiante moroso")
            else:
                print("Libro no disponible")
        else:
            print("Estudiante y/o libro no encontrado(s)")

    def realizarDevolucion(self, pEstudianteID: int, pLibroID: int):
        return
