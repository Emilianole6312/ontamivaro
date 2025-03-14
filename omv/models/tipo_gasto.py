

class Tipo_gasto():
    def __init__(self, nombre, descripcion='', id = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f'({self.id}, {self.nombre}, {self.descripcion})'

    