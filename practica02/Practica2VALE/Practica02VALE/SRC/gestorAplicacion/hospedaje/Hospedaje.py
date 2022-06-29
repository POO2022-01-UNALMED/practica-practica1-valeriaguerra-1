class Hospedaje:
    
    _hospedajes = []

    
    def __init__(self, nombre, locacion, precio_dia, estrellas):
        self._nombre = nombre
        self._locacion = locacion
        self._precio_dia = precio_dia
        self._estrellas = estrellas
        Hospedaje._hospedajes.append(self)



#calcular precio de hospedaje
    def calcularPrecio(self, dias):
        return int((dias * self._precio_dia))

 

    @staticmethod
    def buscarHospedajePorUbicacion(ubicacion):
        hospedajesEnUbicacion = []
        i = 0
        while i < len(Hospedaje._hospedajes):
            if Hospedaje._hospedajes[i].getLocacion().casefold() == ubicacion.casefold():
                hospedajesEnUbicacion.append(Hospedaje._hospedajes[i])
            i += 1
        return hospedajesEnUbicacion

    @staticmethod
    def buscarHospedajePorNombre(nombre):
        i = 0
        while i < len(Hospedaje._hospedajes):
            if Hospedaje._hospedajes[i].getNombre().casefold() == nombre.casefold():
                return Hospedaje._hospedajes[i]
            i += 1
        return None


    def setLocacion(self, locacion):
        self._locacion = locacion

    def setPrecio_dias(self, precio_dias):
        self._precio_dia = precio_dias

    @staticmethod
    def getHospedajes():
        return Hospedaje._hospedajes

    @staticmethod
    def setHospedajes(hospedajes):
        Hospedaje._hospedajes = hospedajes
    def getPrecio_dia(self):
        return self._precio_dia

    def setPrecio_dia(self, precio_dia):
        self._precio_dia = precio_dia

    def getLocacion(self):
        return self._locacion

    def getEstrellas(self):
        return self._estrellas

    def setEstrellas(self, estrellas):
        self._estrellas = estrellas

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
