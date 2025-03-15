
class Gasto():
    def __init__(self, fecha, monto, tipo_gasto, descripcion = '', id = None):
        self.id = id
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion
        self.tipo_gasto = tipo_gasto

    @classmethod
    def from_tupla(cls, tupla):
        return cls(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])

    def __repr__(self):
        return f'({self.fecha}, {self.id}, {self.monto}, "{self.descripcion}", {self.tipo_gasto.id})'
