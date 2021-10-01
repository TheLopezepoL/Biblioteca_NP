from Logica import Estudiante, Escuela


class Bibliotecario:
    libros: list
    escuela: Escuela

    def __init__(self):
        self.libros = []
        self.escuelas = []
        return

    def validarUsuario(self, pUsuario: str, pContrasenha: str):
        for estudiante in self.escuela.estudiantes:
            if estudiante.validarUsuario(pUsuario, pContrasenha):
                return True
        return False

    def returnEstudianteXID(self, pEstudianteID: int):
        for estudiante in self.escuela.estudiantes:
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
        return

    def realizarDevolucion(self, pEstudianteID: int, pLibroID: int):
        estudiante = self.returnEstudianteXID(pEstudianteID)
        if estudiante is not None:
            libro = estudiante.devolverLibro(pLibroID)
            if libro is not None:
                libro.isDisponible = True
                return libro
            else:
                print("Libro no fue prestado al estudiante")
        else:
            print("Estudiante no encontrado")
        return None
