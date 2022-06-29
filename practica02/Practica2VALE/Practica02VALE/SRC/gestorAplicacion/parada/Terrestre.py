
class Terrestre:
   

 
    def __init__(self, nombre, transportadora):
       
        self.Gasto_gasolina = 120
        self._descompuesto = False
        self._SILLAS_ECONOMICAS = []
        self._SILLAS_EJECUTIVAS = []
        self._nombre = nombre
        self._transportadora= transportadora

    
    def getTransportadora(self):
        return self._transportadora

    def setTransportadora(self, transportadora):
        self._transportadora = transportadora

    def getSILLASECONOMICAS(self):
        return self._SILLAS_ECONOMICAS

    def setSILLASECONOMICAS(self, sILLAS_ECONOMICAS):
        self._SILLAS_ECONOMICAS = sILLAS_ECONOMICAS

    def getSILLASEJECUTIVAS(self):
        return self._SILLAS_EJECUTIVAS

    def setSILLASEJECUTIVAS(self, sILLAS_EJECUTIVAS):
        self._SILLAS_EJECUTIVAS = sILLAS_EJECUTIVAS

    def getGastoGasolina(self):
        return self.Gasto_gasolina

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre



    def isDescompuesto(self):
        return self._descompuesto

    def setDescompuesto(self, descompuesto):
        self._descompuesto = descompuesto

    def __str__(self):
        return self._nombre


    def buscarSillaPorUbicacionyTipo(self, ubicacion, tipo):

        if tipo.lower() == "ECONOMICA".lower():
            for i in self._SILLAS_ECONOMICAS:
                if i.isEstado() and i.getUbicacion() == ubicacion:
                    return i
        elif tipo.lower() == "EJECUTIVA".lower():
            for i in self._SILLAS_EJECUTIVAS:
                if i.isEstado() and i.getUbicacion() == ubicacion:
                    return i
        return None
  
    
    def Calcular_Sillas_Ocupadas(self):
        pass

#gasolina
    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        pass
