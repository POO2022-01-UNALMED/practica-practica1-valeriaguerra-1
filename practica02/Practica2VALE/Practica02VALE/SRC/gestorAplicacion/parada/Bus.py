import math
from gestorAplicacion.parada.Terrestre import Terrestre
from gestorAplicacion.parada.Silla import Silla
from gestorAplicacion.parada.Clase import Clase
from gestorAplicacion.parada.Ubicacion import Ubicacion


class Bus(Terrestre):
    _NUM_SILLAS_ECONOMICAS = 32
    _NUM_SILLAS_EJECUTIVAS = 12

  
    def __init__(self, nombre, transportadora):
        super().__init__(nombre, transportadora)
       
        ubicacion = None

     
        for numPosicion in range(0,Bus._NUM_SILLAS_EJECUTIVAS):
            if numPosicion%4 == 0 or numPosicion % 4 == 3:
                ubicacion = Ubicacion.VENTANA
            else:
                ubicacion = Ubicacion.PASILLO

            self.getSILLASEJECUTIVAS().append( Silla(Clase.EJECUTIVA, numPosicion, ubicacion))

       
        for numPosicion in range(0, Bus._NUM_SILLAS_ECONOMICAS):
            if numPosicion % 6 == 0 or numPosicion% 6 == 5:
                ubicacion = Ubicacion.VENTANA
            elif numPosicion % 6 == 1 or numPosicion % 6 == 4:
                ubicacion = Ubicacion.CENTRAL
            elif numPosicion % 6 == 2 or numPosicion % 6 == 3:
                ubicacion = Ubicacion.PASILLO
            self.getSILLASECONOMICAS().append(Silla(Clase.ECONOMICA, numPosicion, ubicacion))

    def getNombre(self):
        texto = super().getNombre() + "_V"
        return texto

    @staticmethod
    def getNumSillasEconomicas():
        return Bus._NUM_SILLAS_ECONOMICAS

    @staticmethod
    def getNumSillasEjecutivas():
        return Bus._NUM_SILLAS_EJECUTIVAS

    # METODOS

    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        consumido = None
        consumido = self.getGastoGasolina() * distancia_en_km
        return consumido
