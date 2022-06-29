from excepciones.ErrorAsignacion import ExcepcionIdTiquete
from gestorAplicacion.parada import *
from gestorAplicacion.adminViajes.Viaje import Viaje
from gestorAplicacion.adminViajes.Tiquete import Tiquete

#se guarda la inf de todas las transportadoras
class Transportadora():

    #ATRIBUTOS
    _transportadoras = []

    #CONSTRUCTOR
    def __init__(self, nombre):
        self._terrestres = []
        self._viajes = []

        self._nombre = nombre
        Transportadora._transportadoras.append(self)

    def toString(self):
        return self._nombre



#buscar Transportadora por nombre

    @staticmethod
    def buscarTransportadoraPorNombre(nombre2):
        retorno = None
        i = 0
        while i < len(Transportadora.getTransportadoras()):
            if Transportadora.getTransportadoras()[i].getNombre().lower() == nombre2.lower():
               
                retorno = Transportadora.getTransportadoras()[i]
            i += 1
        return retorno

#buscar viaje por id 
    def buscarViajePorID(self, viajes, ID):
        i = 0
        while i < len(viajes):
            if viajes[i].getID() == ID:
                return viajes[i]
            i += 1
        return None

#buscar viaje por terrestre 
    def buscarVueloPorTerrestre(self, vuelos, nombre_Terrestre):
        i = 0
        while i <len(viajes):
            if viajes [i].getTerrestre().getNombre().casefold() ==nombre_Terrestre.casefold():
                return viajes[i]
            i += 1
        return None

    
    def buscarViajePorDestino(self, viajes, destino):
        viajesPorDestino = []
        i = 0
        while i < len(viajes):
            if viajes[i].getDestino().casefold() == destino.casefold():
                viajesPorDestino.append(viajes[i])
            i += 1
        return viajesPorDestino

    
#buscar viaje por fechas 
    def buscarViajePorFecha(self, viajes, fecha):
        viajesPorFecha = []
        i = 0
        while i < len(viajes):
            if viajes[i].getFecha_de_salida() == fecha:
                viajesPorFecha.append(viajes[i])
            i += 1
        return viajesPorFecha

   
#viajes disponibles 
    def viajesDisponibles(self, viajes):
        viajesDisponibles = []
        i = 0
        while i < len(viajes):
            if not viajes[i].isEstaCompleto():
                viajesDisponibles.append(viajes[i])
            i += 1
        return viajesDisponibles

    

#agregarviajes
    def agregarViaje(self, viaje):
        self._viajes.append(viaje)

#cancelar viaje recibe un entero
    def cancelarViaje(self, viaje_a_eliminar):
        i = 0
        while i < len(self._viajes):
            if self._viajes[i].getID() == viaje_a_eliminar:
                self._viajes.pop(i)
                return True
            i += 1
        return False
#buscar tiquete por id 


    @staticmethod
    def BuscarTiquete(ID):
        tiquete_buscado = None
        transportadorasDisponibles = Transportadora.getTransportadoras()
        i = 0
        while i < len(transportadorasDisponibles):
            transportadora = transportadorasDisponibles[i]
            j = 0
            while j < len(transportadora.getViajes()):

                viaje = transportadora.getViajes()[j]
                tiquete_buscado = viaje.buscarTiquetePorID(viaje.getTiquetes(), ID)
                if tiquete_buscado is not None:
                    return tiquete_buscado
                j += 1
            i += 1
        
        if tiquete_buscado == None:
            raise ExcepcionIdTiquete(ID)
        return None

   

    def getNombre(self):
        return self._nombre


    def setNombre(self, nombre):
        self._nombre = nombre


    def getViajes(self):
        return self._viajes


    def setViajes(self, viajes):
        self._viajes = viajes

    def getTerrestres(self):
        return self._terrestres

    def setBuses(self, buses):
        self._terrestres = buses

    @staticmethod
    def getAerolineas():
        return Transportadora._transportadoras

    @staticmethod
    def setTransportadoras(transportadoras):
        Transportadora._transportadoras = transportadoras
