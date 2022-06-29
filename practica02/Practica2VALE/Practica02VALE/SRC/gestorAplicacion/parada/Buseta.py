
import math
from gestorAplicacion.parada.Terrestre import Terrestre
from gestorAplicacion.parada.Silla import Silla
from gestorAplicacion.parada.Clase import Clase
from gestorAplicacion.parada.Ubicacion import Ubicacion


class Buseta(Terrestre):

    _NUM_SILLAS_ECONOMICAS = 12
    _NUM_SILLAS_EJECUTIVAS = 4

    def __init__(self, nombre, transportadora):
        super().__init__(nombre, transportadora)
        
        for numPosicion in range(0, Buseta._NUM_SILLAS_EJECUTIVAS):
            if numPosicion % 4 == 0 or numPosicion % 4 == 3:
                ubicacion = Ubicacion.VENTANA
            else:
                ubicacion = Ubicacion.PASILLO

            self.getSILLASEJECUTIVAS().append(Silla(Clase.EJECUTIVA, numPosicion, ubicacion))

     
        for numPosicion in range(0, Buseta._NUM_SILLAS_ECONOMICAS):
            if numPosicion % 12 == 0 or numPosicion % 12 == 11:
                ubicacion = Ubicacion.VENTANA
            elif math.fmod(numPosicion, 12) == 1 or math.fmod(numPosicion, 12) == 4:
                ubicacion = Ubicacion.CENTRAL
            else:
                ubicacion = Ubicacion.PASILLO

            self.getSILLASECONOMICAS().append(Silla(Clase.ECONOMICA, numPosicion, ubicacion))

    @staticmethod
    def getNumSillasEconomicas():
        return Buseta._NUM_SILLAS_ECONOMICAS

    @staticmethod
    def getNumSillasEjecutivas():
        return Buseta._NUM_SILLAS_EJECUTIVAS


    def Calcular_Sillas_Ocupadas(self):
        cont = 0
        for i in self.getSILLASECONOMICAS():
            if i.isEstado():
                cont += 1
        for j in self.getSILLASEJECUTIVAS():
            if j.isEstado():
                cont += 1
        return cont


#consumo de gasolina 

    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        consumido = self.getGastoGasolina() * distancia_en_km
        return consumido
