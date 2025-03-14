

class Gasto():
    def __init__(self, fecha, monto, tipo_gasto, id = None):
        self.id = id
        self.fecha = fecha
        self.monto = monto
        self.tipo_gasto = tipo_gasto

    def __str__(self):
        return "Gasto: {0} - {1} - {2}".format(self.fecha, self.monto, self.tipo_gasto)
