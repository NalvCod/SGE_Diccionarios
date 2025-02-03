class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregarContactoAgenda(self, nombre, telefono):
        if nombre in self.contactos:
            return False
        else:
            self.contactos[nombre] = telefono
            return True

    def eliminarContactoAgenda(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]

    def buscarContactoAgenda(self, nombre):
        if nombre in self.contactos:
            return self.contactos[nombre]
        return None