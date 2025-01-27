class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregarContactoAgenda(this, nombre, telefono):
        if (nombre in self.contactos):
            return False
        else:
            self.contactos[nombre] = telefono

    def eliminarContactoAgenda(this, nombre):
        if (nombre in agenda):
            agenda.contactos[nombre] = null
