

class Gasto():
    def __init__(self, fecha, monto, tipo_gasto, id = None):
        self.id = id
        self.fecha = fecha
        self.monto = monto
        self.tipo_gasto = tipo_gasto

    def __repr__(self):
        return f"({self.id}, {self.fecha}, {self.monto}, {self.tipo_gasto.id})"
