class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito

    def agregar(self, planta):
        if planta.idPlanta not in self.carrito.keys():
            self.carrito[planta.IdPlanta]={
                "planta_id": planta.idPlanta,
                "nombre": planta.nombre,
                "cantidad": 1,
                "precio":str(planta.precio),
                "total":planta.total
            }
        else:
            for key, value in self.carrito.items():
                if key==planta.idPlanta:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = planta.precio
                    value["total"]=value["total"]+planta.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"]= self.carrito
        self.session.modified=True

    def eliminar(self, planta):
        id = planta.idPlanta
        if id in self.carrito:
            del self.carriot[id]
            self.guardar_carrito()

    def resta(self, planta):
        for key, value in self.carriot.items():
            if key == planta.idPlanta:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- planta.precio
                if value["cantidad"] < 1:
                    self.eliminar(planta)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True