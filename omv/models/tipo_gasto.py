

class Tipo_gasto():
    def __init__(self, nombre, descripcion, id = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return "Tipo de gasto: {0} - {1}".format(self.nombre, self.descripcion)

    