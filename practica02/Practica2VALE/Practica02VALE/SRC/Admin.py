#esta clase es la interacion con el usuario 
#importamos esas librerias 
import random
import pickle
from tkinter import *
from excepciones.ErrorAsignacion import ExcepcionAgregarHospedaje, ExcepcionIdTiquete, ExcepcionIdViaje, ExcepcionModificarHospedaje
from excepciones.ErrorAplicacion import ErrorAplicacion
from excepciones.ErrorFormato import ExcepcionEnteroFloat, ExcepcionEnteroString

from gestorAplicacion.parada.Clase import Clase
from gestorAplicacion.hospedaje.Hospedaje import Hospedaje
from gestorAplicacion.adminViajes.Transportadora import Transportadora
from gestorAplicacion.adminViajes.Pasajero import Pasajero 
from gestorAplicacion.adminViajes.Tiquete import Tiquete
from gestorAplicacion.adminViajes.Viaje import Viaje
from gestorAplicacion.parada.Terrestre import Terrestre
from gestorAplicacion.parada.Bus import Bus
from gestorAplicacion.parada.Buseta import Buseta
from gestorAplicacion.parada.Silla import Silla
from gestorAplicacion.parada.Ubicacion import Ubicacion



class  Admin(object):

    # DESERIALIZACION DE DATOS
    picklefile = open('./baseDeDatos/Transportadoras','rb')
    picklefile2 = open('./baseDeDatos/Hospedajes','rb')
    Transportadora.setTransportadoras(pickle.load(picklefile))
    Hospedaje.setHospedajess(pickle.load(picklefile2))
    picklefile.close()
    picklefile2.close()
    
    #--------------------------------------------------------------------------------------------------------------------------------------
    # MUESTRA UNA TABLA POR CADA TRANSPORTADORA CON LOS VIAJES QUE SE TIENEN DISPONIBLES
    @staticmethod
    def mostrarViajesPorTransportadoras(frame_operaciones):
        TransportadorasDisponibles = Transportadora.getTransportadoras()
        return Admin.mostrarTablaDeViajesDisponiblesPorTransportadoras(TransportadorasDisponibles,frame_operaciones)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RESTITUIR LA LISTA DE HOSPEDAJES DISPONIBLES CON SU NOMBRE Y LOCACION    
    @staticmethod
    def obtenerHospedajes():
        lista_hospedajes= Hospedaje.getHospedajes()
        valores =[]
        
        for hospedaje in lista_hospedajes:
            valores.append(hospedaje.getNombre()+"---"+hospedaje.getLocacion())

        return valores

   
    def generarTiquete(viaje):
    
        ID_tiquete = 100 + random.random() * 900 
        try:
            while Transportadora.BuscarTiquete(int(ID_tiquete)) is not None:
                ID_tiquete = 100 + random.random() * 900
        except ExcepcionIdTiquete:
            tiquete = Tiquete(int(ID_tiquete), viaje.getPrecio(), viaje)
        return tiquete

    
    
    @staticmethod
    def asignarTiquete(datos,tiquete):

        nombre = datos[0]
        edad = int(datos[1])
        pasaporte = datos[2]
        correo = datos[-1]

        
        pasajero = Pasajero(pasaporte, nombre, tiquete, edad, correo)
        tiquete.setPasajero(pasajero)

 
    @staticmethod
    def buscarTiqueteYHospedaje(id,numero):
        tiqueteID = int(id)
        tiquete_solicitado = Transportadora.BuscarTiquete(tiqueteID)

        if tiquete_solicitado == None:
            raise ExcepcionIdTiquete(tiqueteID) 

        elif tiquete_solicitado.getHospedaje() != None:
            if numero == 1:
                raise ExcepcionAgregarHospedaje(tiqueteID) 
            else:
                return tiquete_solicitado
        else:
            if numero == 1:
                return tiquete_solicitado 
            else:
                raise ExcepcionModificarHospedaje(tiqueteID)
 
 
    @staticmethod
    def solicitarHospedaje(tiquete_solicitado,hospedaje_nombre):
        destino = tiquete_solicitado.getViaje().getDestino()
        hospedaje_solicitado = Hospedaje.buscarHospedajePorNombre(hospedaje_nombre)
        
        if hospedaje_solicitado == None:
            return hospedaje_solicitado 

        elif  hospedaje_solicitado.getLocacion().lower() != destino.lower():
            hospedaje_solicitado = None 
            return hospedaje_solicitado

        else:
            return hospedaje_solicitado 

 
    @staticmethod
    def agregarHospedaje(tiquete_solicitado,hospedaje_solicitado,num_dias):
        tiquete_solicitado.setHospedaje(hospedaje_solicitado)
        tiquete_solicitado.asignarPrecio(int(num_dias))

  
    @staticmethod
    def modificarSilla(numero, tiquete,silla):
        if numero ==1 :
            tiquete.setSilla(silla)
        else:    
            tiquete.getSilla().setEstado(True) 
            tiquete.setSilla(silla)
        tiquete.asignarPrecio() 

   
    @staticmethod
    def isFloat(s):
        try:
            float(s)
            raise ExcepcionEnteroFloat(s)
        except ValueError:
            return
    @staticmethod
    def listarPasajeros(valor,label):
        transportadoras=Transportadora.getTransportadoras()
        if not valor.isdigit():
            Admin.isFloat(valor)
            raise ExcepcionEnteroString(valor)

        IDBusqueda = int(valor)

        tiquetes = []
        viaje = None
        for i in transportadoras:
            if i.buscarViajePorID(i.getViajes(), IDBusqueda) != None:
                viaje = i.buscarViajePorID(i.getViajes(), IDBusqueda)
                break
        if viaje ==None:
            raise ExcepcionIdViaje(IDBusqueda)

        tiquetes = viaje.getTiquetes()
        label["text"]+="LISTA DE PASAJEROS PARA EL VIAJE " + str(IDBusqueda)

        if len(tiquetes) == 0:
            label["text"]+="\nEl viaje aun no tiene pasajeros asociados \n"
        else:
            Admin.mostrarTablaDePasajeros(tiquetes,label)

  
    
    @staticmethod
    def agregarNuevoViaje(valores):
        nombreTransportadora= valores[0]
        iD = int(valores[1])
        precio= int(valores[2])
        origen = valores[3]
        destino = valores[4]
        distancia = int(valores[5])
        fechaSalida=valores[6]
        horaSalida = valores[7]
        terrestre = valores[8]
        nombreTerrestre = valores[9]
        for transportadora in Transportadora.getTransportadoras():
            existe_viaje= transportadora.buscarViajePorID(transportadora.getViajes(),iD)
            if existe_viaje !=None:
                return True

        if terrestre.lower() == "bus":
            bus = Bus(nombreTerrestre, Transportadora.buscarTransportadoraPorNombre(nombreTransportadora))
            viaje = Viaje(iD, precio, origen, destino, bus, distancia, fechaSalida, horaSalida)
    
        elif terrestre.lower() == "buseta":
            buseta = Buseta(nombreTerrestre, Transportadora.buscarTransportadoraPorNombrePorNombre(nombreTransportadora))
            viaje = Viaje(iD, precio, origen, destino, buseta, distancia, fechaSalida, horaSalida)
        return False  

 

    @staticmethod
    def cancelarViajes(id):
        viaje_encontrado = False
        transportadoras = Transportadora.getTransportadoras()
        id = id
        for transportadoras in transportadoras:
            i = 0
            while i < len(transportadoras.getViajes()):
                if transportadora.buscarViajePorID(transportadora.getViajes(), id) != None:
                    transportadora.cancelarViaje(id)
                    viaje_encontrado = True
                    break 
                i += 1
        return viaje_encontrado

  

    @staticmethod
    def retirarBus(terrestre):
        terrestre_encontrada = False
        nombre_terrestre = terrestre
        aerolineasDisponibles = Transportadora.getTransportadoras()
        i = 0
        while i < len(transportadorasDisponibles):
            transportadora = transportadorasDisponibles[i]
            
            viaje = transportadora.buscarViajePorTerrestre(transportadora.getViajes(), nombre_terrestre)
            if viaje!= None:
                viaje.getTerrestre().setDescompuesto(True)
                transportadora.cancelarViaje(viaje.getID())
                terrestre_encontrada = True
                break
            i += 1
        
        return terrestre_encontrada

    @staticmethod
    def nuevoHospedaje(valores):

        nombre = valores[0]
        locacion = valores[1]
        precio = valores[2]
        estrellas = valores[3]

        nuevoHospedaje = Hospedaje(nombre, locacion, precio, estrellas)


    @staticmethod
    def retirarHospedaje(nombre):
        hospedaje_encontrado = False
        if Hospedaje.buscarHospedajePorNombre(nombre) != None:
            i = 0
            while i < len(HospedajegetHospedajes()):
                if Hospedaje.getHospedajes()[i].getNombre().lower() == nombre.lower():
                    Hospedaje.getHospedajes().pop(i)
                    hospedaje_encontrado = True
                    break
                i += 1
        return hospedaje_encontrado

  
    @staticmethod
    def salirDelSistema():
        picklefile = open('./baseDeDatos/Transportadoras', 'wb')
        picklefile2 = open('./baseDeDatos/Hospedajes','wb')
        pickle.dump(Transportadora._transportadoras, picklefile)
        pickle.dump(Hospedaje._hospedajes,picklefile2)
        picklefile.close()
        picklefile2.close()
        quit()



    @staticmethod
    def consultarViajesPorDestino(destino, frame_operaciones):
        lista_viajes_nombres = []
        viajes = []
        nombreTransportadoras =[]

        transportadorasDisponibles = Transportadora.getTransportadoras()
        i = 0
        while i < len(transportadorasDisponibles):
            transportadora = transportadorasDisponibles[i]
            viajesPorDestino = transportadora.buscarViajePorDestino(transportadora.viajesDisponibles(transportadora.getViajes()), destino)
            if len(viajesPorDestino) != 0:
                label = Label(frame_operaciones)
                Admin.mostrarTablaDeViajes(transportadora, viajesPorDestino, label)
                viajes.append(label)
                nombreTransportadoras.append(transportadora.getNombre())
            i += 1

        lista_viajes_nombres.append(viajes)
        lista_viajes_nombres.append(nombreTransportadoras)

        return lista_viajes_nombres

  
   

    @staticmethod
    def consultarViajesPorDestinoYFecha(destino, fecha, frame_operaciones):

        lista_viajes_nombres = []
        viajes = []
        nombreTransportadoras =[]

        transportadorasDisponibles = Transportadora.getTransportadoras()
        i = 0
        while i < len(transportadorasDisponibles):
            transportadora = transportadorasDisponibles[i]
            viajesPorDestino = transportadora.buscarViajePorDestino(transportadora.viajesDisponibles(transportadora.getViajes()), destino)
            if len(viajesPorDestino) != 0:
                viajesPorFecha = transportadora.buscarViajePorFecha(viajesPorDestino, fecha)
                if len(viajesPorFecha) != 0:
                    label = Label(frame_operaciones)
                    Admin.mostrarTablaDeViajes(transportadora, viajesPorFecha, label)
                    viajes.append(label)
                    nombreTransportadoras.append(transportadora.getNombre())
            i += 1
        
        lista_viajes_nombres.append(viajes)
        lista_viajes_nombres.append(nombreTransportadoras)

        return lista_viajes_nombres


  
    @staticmethod
    def elegirSilla(tiquete,datos_silla):
        clase =str( datos_silla[0])
        ubicacion = str(datos_silla[1])

        if ubicacion.lower() == "pasillo":
            ubicacion = Ubicacion.PASILLO
        elif ubicacion.lower() == "ventana":
            ubicacion = Ubicacion.VENTANA
        else:
            ubicacion = Ubicacion.CENTRAL

        return tiquete.getVuelo().getTerrestre().buscarSillaPorUbicacionyTipo(ubicacion,clase)

  
    @staticmethod
    def mostrarTablaDePasajeros(tiquetes,label):
        label["text"]+="\n---------------------------------------------------------------"
        label["text"]+="\n"+"{0:>5} {1:>12} {2:>16} {3:>17}".format("ID", "NOMBRE", "CEDULA", "EMAIL"+"\n")
        label["text"]+="---------------------------------------------------------------"

        i = 0
        while i < len(tiquetes):
            label["text"]+="\n"+"{0:>5} {1:>13} {2:>12} {3:>26}".format(str(tiquetes[i].getId()), tiquetes[i].getPasajero().nombre, tiquetes[i].getPasajero().getCedula(), tiquetes[i].getPasajero().getEmail())
            i += 1
        label["text"]+="\n---------------------------------------------------------------"
        label["text"]+="\n"

   
    @staticmethod
    def mostrarTablaDeHospedajes(hospedajes, label):
        label["text"]+="\n"
        label["text"]+="\n"+ "-------------------------------------------------------------"
        label["text"]+="\n"+"{0:>10} {1:>15} {2:>18} {3:>12}".format("NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS")
        label["text"]+="\n"
        label["text"]+="\n"+"-------------------------------------------------------------"

        j = 0
        while j < len(hospedajes):
            label["text"]+="\n"+"{0:>13} {1:>11} {2:>16} {3:>11}".format(hospedajes[j].getNombre(), hospedajes[j].getLocacion(), hospedajes[j].getPrecio_dia(), hospedajes[j].getEstrellas())
            label["text"]+="\n"
            j += 1

        label["text"]+="\n"+"-------------------------------------------------------------"
        label["text"]+="\n"

    @staticmethod
    def mostrarTablaDeViajesDisponiblesPorTransportadoras(transportadoras,frame_operaciones):
        i = 0
        lista = []
        while i < len(transportadoras):
            label = Label(frame_operaciones)
            transportadora = transportadoras[i]
            Admin.printEncabezadoTransportadora(transportadoras[i],label)
            Admin.printViajes(transportadora.viajesDisponibles(transportadora.getViajes()),label)
            Admin.printSeparador(label)
            lista.append(label)
            i += 1
        return lista


    @staticmethod
    def mostrarTablaDeViajes(transportadora,viajes,label):
        if len(viajes) != 0:
            Admin.printEncabezadoTransportadora(transportadora,label)
            Admin.printViajes(viajes,label)
            Admin.printSeparador(label)
        return label

    @staticmethod
    def printEncabezadoTransportadora(transportadora,label):
        label["text"]+="\n"+"VIAJES  DISPONIBLES DE LA transportadora " + transportadora.getNombre().upper()
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"
        label["text"]+="\n"+"{0:>4} {1:>13} {2:>12} {3:>14} {4:>12} {5:>22} {6:>12}".format("ID", "PRECIO", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA", "TERRESTRE")
        label["text"]+="\n"
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"


    @staticmethod
    def printViajes(viajes,label):
        j = 0
        while j < len(viajes):
            label["text"]+="\n"+"{0:>5} {1:>12} {2:>13} {3:>13} {4:>15} {5:>11} {6:>21}".format(viajes[j].getID(), viajes[j].getPrecio(), viajes[j].getOrigen(), viajes[j].getDestino(), viajes[j].getFecha_de_salida(), viajes[j].getHora_de_salida(), viajes[j].getTerrestre().getNombre())
            label["text"]+="\n"
            j += 1


#met para separar 

    @staticmethod
    def printSeparador(label):
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"
        label["text"]+="\n"

    





