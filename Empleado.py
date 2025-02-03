from Persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def imprimir_salario(self):
        print(f"El salario es: {self.salario}")

    def __lt__(self, other):
        return 'a'