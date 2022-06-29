class Pasajero:

    def __init__(self, cedula, nombre, tiquete, edad, email):
        self._cedula = cedula
        self.nombre = nombre
        self._tiquete = tiquete
        self._edad = edad
        self._email = email
        tiquete.setPasajero(self)


    def getCedula(self):
        return self._cedula

    def setCedula(self, cedula):
        self._cedula = cedula

    def getTiquete(self):
        return self._tiquete

    def setTiquete(self, tiquete):
        self._tiquete = tiquete

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getEmail(self):
        return self._email
        
    def setEmail(self, email):
        self._email = email


