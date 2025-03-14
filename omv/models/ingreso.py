

class Ingreso():
    def __init__(self, fecha, monto, descripcion='', id = None):
        self.id = id
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion
    
    def __repr__(self):
        return f'({self.id}, {self.fecha}, {self.monto}, {self.descripcion})'