

class ingreso():
    def __init__(self, fecha, monto, id = None):
        self.id = id
        self.fecha = fecha
        self.monto = monto
    
    def __str__(self):
        return "Ingreso: {0} - {1}".format(self.fecha, self.monto)