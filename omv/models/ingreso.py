

class Ingreso():
    def __init__(self, fecha, monto, descripcion='', id = None):
        self.id = id
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion

    @classmethod
    def from_tupla(cls, tupla):
        return cls(tupla[0], tupla[1], tupla[2], tupla[3])
    
    def __repr__(self):
        return f'({self.id}, {self.fecha}, {self.monto}, {self.descripcion})'