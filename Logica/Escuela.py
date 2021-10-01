from Logica.Estudiante import Estudiante


class Escuela:
    estudiantes: list

    def __init__(self):
        self.estudiantes = []
        return

    def agregarEstudiante(self, pNombre: str, pUsuario: str, pContrasenha: str):
        estudiante = Estudiante(pNombre, pUsuario, pContrasenha)
        self.estudiantes.append(estudiante)
        return

    def eliminarEstudiante(self, pEstudianteID: int):
        for index in range(len(self.estudiantes)):
            if self.estudiantes[index].carnet == pEstudianteID:
                return self.estudiantes.pop(index)
        return None


