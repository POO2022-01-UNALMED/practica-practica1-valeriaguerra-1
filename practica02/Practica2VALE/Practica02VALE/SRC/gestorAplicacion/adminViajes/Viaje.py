from gestorAplicacion.parada import *
from gestorAplicacion.adminViajes.Tiquete import Tiquete


class Viaje():

   
    def __init__(self, iD, precio, origen, destino, terrestre, distancia, fecha_de_salida, hora_de_salida):
        self._ID = iD
        self._precio = precio
        self._origen = origen
        self._destino = destino
        self._terrestre =  terrestre
        self._distancia_en_km = distancia
        self._fecha_de_salida = fecha_de_salida
        self.setHora_de_salida(hora_de_salida)
        self.getTerrestre().getTerrestre().agregarViaje(self)
        self._tiquetes = []
        self._estaCompleto = False

    #buscat tiquete por ID
    def buscarTiquetePorID(self, tiquetes, ID):
        i = 0
        while i < len(tiquetes):
            if tiquetes[i].getId() == ID:
                return tiquetes[i]
            i += 1
        return None


 #metodos get and set

    def getID(self):
        return self._ID

    def setID(self, iD):
        self._ID = iD

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getOrigen(self):
        return self._origen

    def setOrigen(self, origen):
        self._origen = origen

    def getDestino(self):
        return self._destino

    def setDestino(self, destino):
        self._destino = destino


#modificar class abstract
    def getTerrestre(self):
        return self._terrestre

    def setAeronave(self, terrestre):
        self._terrestre = terrestre

    def getDistancia_en_km(self):
        return self._distancia_en_km

    def setDistancia_en_km(self, distancia_en_km):
        self._distancia_en_km = distancia_en_km

    def getFecha_de_salida(self):
        return self._fecha_de_salida

    def setFecha_de_salida(self, fecha_de_salida):
        self._fecha_de_salida = fecha_de_salida

    def getTiquetes(self):
        return self._tiquetes

    def setTiquetes(self, tiquetes):
        self._tiquetes = tiquetes

    def getHora_de_salida(self):
        return self._hora_de_salida

    def setHora_de_salida(self, hora_de_salida):
        self._hora_de_salida = hora_de_salida

    def isEstaCompleto(self):
        return self._estaCompleto

    def setEstaCompleto(self, estaCompleto):
        self._estaCompleto = estaCompleto