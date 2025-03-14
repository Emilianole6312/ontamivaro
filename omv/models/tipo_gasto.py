

class Tipo_gasto():
    def __init__(self, nombre, descripcion='', id = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    @classmethod
    def from_tupla(cls, tupla):
        return cls(tupla[0], tupla[1], tupla[2])

    def __repr__(self):
        return f'({self.id}, {self.nombre}, {self.descripcion})'

    