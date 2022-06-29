from tkinter import messagebox
from tkinter.ttk import Combobox
from excepciones.ErrorAplicacion import *
from excepciones.ErrorAsignacion import *
from excepciones.ErrorFormato  import *
from tkinter import *
from FieldFrame import *
from gestorAplicacion.hospedaje.Hospedaje import Hospedaje
from gestorAplicacion.adminViajes.Transportadora import Transportadora

class VentanaSecundaria(Toplevel):

    en_uso = False 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ventana secundaria")
        self.option_add('*tearOff', FALSE)
        self.title("Sistema de tiquetes terminal")
        self.geometry("800x550")
        self.iconbitmap('./imagenes/icono.ico')
        self.ventanaInicio = None
        self.focus()

        #frames
        self.frame = Frame(self,relief="groove",bd=2)
        self.frame.pack(ipadx=50, padx=15,ipady=20,pady=15,expand=True,fill=BOTH)
        self.frame_proceso = Frame(self.frame,bg="gray80")
        self.frame_proceso.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
        self.frame_proceso.config(relief = "ridge")
        self.frame_proceso.config(bd=2)
        self.frame_descripcion = Frame(self.frame ,relief="ridge",bg="gray90")
        self.frame_descripcion.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)
        self.frame_descripcion.config(bd=2)
        self.ventana_operaciones = Frame(self.frame,relief="groove",bd=2)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=BOTH,expand = True)
        

        #menu
        self.menubar = Menu(self)

        self.menuArchivo = Menu(self.menubar)
        self.menuArchivo.add_command(label = "Aplicacion", command = self.descripcionApp)
        self.menuArchivo.add_command(label = "Salir", command = self.salirVentana)

        self.menuProcesos = Menu(self.menubar)
        self.menuProcesos.add_command(label = "Ver viajes disponibles por Transportadoras",command= self.mostrarViajesPorTransportadoras)
        self.menuProcesos.add_command(label = "Comprar tiquete para un viaje por destino y fecha", command = self.generarTiquete)
        self.menuProcesos.add_command(label = "Agregar hospedaje en el destino del viaje", command = self.agregarHospedajeTiquete )
        self.menuProcesos.add_command(label = "Modificar tiquete comprado", command = self.modificarTiquete)

#menuprocesos
        self.menuAdmin = Menu(self.menuProcesos)
        self.menuProcesos.add_cascade(menu = self.menuAdmin,label = "Ver opciones de administrador")
        self.menuAdmin.add_command(label= "Listar pasajeros",command=self.listarPasajeros)
        self.menuAdmin.add_command(label= "Agregar viaje",command=self.agregarViaje)
        self.menuAdmin.add_command(label= "Cancelar viaje",command=self.cancelarViaje)
        self.menuAdmin.add_command(label= "Retirar bus",command=self.retirarBus)
        self.menuAdmin.add_command(label= "Agregar hospedaje",command=self.agregarHospedaje)
        self.menuAdmin.add_command(label= "Eliminar Hospedaje",command=self.eliminarHospedaje)

        self.menuAyuda = Menu(self.menubar)
        self.menuAyuda.add_command(label = "Acerca de", command = self.ayuda)

        self.menubar.add_cascade(label = "Archivo", menu = self.menuArchivo)
        self.menubar.add_cascade(label = "Procesos y Consultas", menu = self.menuProcesos)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menuAyuda)
        self["menu"] = self.menubar
        
        
        
        

#***********************************
        #label
        self.label_proceso = Label(self.frame_proceso,text= "Administrador Sistema de compra de tiquetes ", font = ("Segoe UI", 12,"bold"),height=2, bg="gray80")
        self.label_proceso.pack(ipadx = 2, ipady =2, padx = 5, pady= 5)

        self.label_descripcion = Label(self.frame_descripcion, text = "Realiza reservaciones de viajes y hospedajes, y mantén la informacion actualizada en sistema  de viajes, buses y hospedajes", font = ("Segoe UI", 10), bg="gray90")
        self.label_descripcion.pack(ipadx = 2, ipady = 2, padx = 5, pady= 5)

        self.labelTexto = Label(self.ventana_operaciones, text = "Puedes realizarlo  con las acciones dispuestas en el menu <Procesos y consultas>", font = ("Segoe UI", 10))
        self.labelInicio = Label(self.ventana_operaciones)
        self.imagenInicio = PhotoImage(file = './imagenes/Reservacion.png')
        self.labelInicio["image"] = self.imagenInicio
        self.labelTexto.pack(ipadx = 10, ipady =10, padx = 10, pady= 10)
        self.labelInicio.pack(ipadx = 10, ipady =10, padx = 10, pady= 10)
        
#contador
        self.contador_mostrarViajesPorTransportadoras = 0
        self.__class__.en_uso = True


   #despliegue de msj con la descripcion 
    def descripcionApp(self):
        descripcion = messagebox.showinfo(title = "Informacion", message = "Sistema DE Reserva de viajes ",
        detail = "La aplicacion permite hacer reservaciones de un viaje y un hospedaje en el lugar de destino, también realiza algunas funciones  de administrador.")

   
   #venta de inicio 
    def salirVentana(self):
        self.__class__.en_uso = False
        self.ventanaInicio.deiconify()
        return super().destroy()

    #muestra viajes disponibles , frame **

    def mostrarViajesPorTransportadorasPorAerolineas(self):
        self.label_proceso.config(text = "Viajes disponibles por Transportadora")
        self.label_descripcion.config(text = "Aquí puede ver  los viajes que están disponibles por las transportadoras ")


        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones= Frame(self.frame,relief="groove",bd=2)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)

        #ejecutable next
        def siguiente():
            self.contador_mostrarViajesPorTransportadoras +=1
            if self.contador_mostrarViajesPorTransportadoras == len(lista_labels):
                self.contador_mostrarViajesPorTransportadoras =0
            lista_labels[self.contador_mostrarViajesPorTransportadoras-1].pack_forget()
            lista_labels[self.contador_mostrarViajesPorTransportadoras].pack()

        boton_siguiente = Button(self.ventana_operaciones,text= "continuar ",command=siguiente)
        boton_siguiente.pack()
        lista_labels=Admin.mostrarVuelosPorAerolineas(self.ventana_operaciones)
        lista_labels[0].pack()

 #muestra viajes disponibles por cada transortadora 

    def buscarViajes(self,formulario):
        try:
            hay_excepcion = formulario.aceptar()
        except ExcepcionStringNumero as owo:
            messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
            
            return
        if hay_excepcion:
            self.generarTiquete()
            return
#self de genar tiquete
        self.label_proceso.config(text = "Viajes disponibles")
        self.label_descripcion.config(text = "Lista los viajes disponibles de acuerdo a los datos  ingresados")

        self.ventana_operaciones.pack_forget()

        hayFecha = False
        fecha = None
        destino = formulario.valor_entradas[0]
        lista_general = None

        if len(formulario.valor_entradas) == 2:
            hayFecha = True
            fecha = formulario.valor_entradas[1]

        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack()

        if hayFecha:
            label = Label(self.ventana_operaciones, text = "Estos son los viajes disponibles hacia: " + destino + " en la fecha " + fecha + " por nuestras transportadoras")
            label.pack()
            lista_general = Admin.consultarViajesPorDestinoYFecha(destino, fecha, self.ventana_operaciones)
        else:
            label = Label(self.ventana_operaciones, text = "Estos son los viajes disponibles hacia: " + destino + " por las transportadoras ")
            label.pack()
            lista_general = Admin.consultarViajesPorDestino(destino, self.ventana_operaciones)
        if len(lista_general[0]) ==0:
            if hayFecha:
                messagebox.showinfo(title="Viajes Disponibles",message= "Lo sentimos, no tenemos viajes diponibles hacia " + destino+" en la fecha: " +fecha )
            else:
                messagebox.showinfo(title="Viajes Disponibles",message= "Lo sentimos, no tenemos viajes diponibles hacia " + destino )
            self.generarTiquete()
            return

    #next label por pantalla

        def siguiente():
            self.contador_mostrarViajesPorTransportadoras +=1
            if self.contador_mostrarViajesPorTransportadoras == len(lista_labels):
                self.contador_mostrarViajesPorTransportadoras =0
            lista_labels[self.contador_mostrarViajesPorTransportadorass-1].pack_forget()
            lista_labels[self.contador_mostrarViajesPorTransportadoras].pack()

        boton_siguiente = Button(self.ventana_operaciones,text= "Siguiente",command = siguiente)
        boton_siguiente.pack()

        lista_labels = lista_general[0]
        lista_labels[0].pack()

        boton_siguiente = Button(self.ventana_operaciones,text= "Continuar con la compra", command = lambda: self.comprarTiquete(lista_general[1]))
        boton_siguiente.pack(side = BOTTOM)

        if len(lista_labels) == 0:
            messagebox.showinfo(title = "Buscar viajes", message = "Lo sentimos, no tenemos viajes hacia ese destino")
            return

   #muestrta resumen de la compra con disponibilidad de sillas  y viajes 
    def comprarTiquete(self, nombres_transportadoras):

        self.label_proceso.config(text = "Compra del viaje")
        self.label_descripcion.config(text = "Para concretar la compra, seleccione la transportadora con la que quiere viajar y el ID del viaje que quiere comprar")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack()

        labelNombreTransportadora = Label(self.ventana_operaciones, text = "Seleccione la transportadora  con la que desea viajar")
        labelNombreTransportadora.pack(ipadx = 5, ipady = 5, padx = 3, pady= 3)

       

        def transportadoraSeleccionada(e):
            nombre = str(transportadoras.get())
            transportadora = Transportadora.buscarTransportadoraPorNombre(nombre)
            transportadoras.config(state = DISABLED)
            label_id_tiquete = Label(self.ventana_operaciones,text="Ingrese el ID del viaje que desea comprar.")
            label_id_tiquete.pack()
            formulario = FieldFrame(self.ventana_operaciones,"Info",["ID viaje"],"valor",None,None,["int"])

       

            def idViajeIngresado():
                self.ventana_operaciones.pack_forget()
                self.ventana_operaciones = Frame(self.frame)
                self.ventana_operaciones.pack()

                try:
                    hay_excepcion = formulario.aceptar()
                except ExcepcionEnteroString as owo:
                    messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                    transportadoraSeleccionada(4)
                    return

                if hay_excepcion:
                    transportadoraSeleccionada(9)
                    return

                id_viaje = int(formulario.valor_entradas[0])
                viaje = transportadora.buscarViajePorID(transportadora.getViajes(),id_viaje)
                if viaje == None:
                    messagebox.showinfo(title="Elegir viaje",message="No existe un viaje con ese ID en la Transportadora"+transportadora.getNombre())
                    return

                self.label_proceso.config(text = "Toma de datos Pasajero")
                self.label_descripcion.config(text = "Recoge los datos del pasajero al que se le enlaza  el tiquete de compra")

                label_datos_pasajero = Label(self.ventana_operaciones,text="Ingrese los datos del pasajero.")
                label_datos_pasajero.pack()
                formulario_pasajero= FieldFrame(self.ventana_operaciones,"criterios",["Nombre","Edad","Cedula","E-mail"],"datos",None,None,["string","int","string","string"])

                def datosPasajero():

                    self.label_proceso.config(text = "Resumen de la compra")
                    self.label_descripcion.config(text = "Muestra un  resumen de la compra realizada, recogida en el tiquete")

                    try:
                        hay_excepcion = formulario_pasajero.aceptar()
                    except ExcepcionEnteroString as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        return
                    except ExcepcionEnteroFloat as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        return
                    except ExcepcionStringNumero as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        return

                    if hay_excepcion:
                        return

                    tiquete=Admin.generarTiquete(viaje)
                    formulario_pasajero.pack_forget()
                    Admin.asignarTiquete(formulario_pasajero.valor_entradas,tiquete)
                    self.modificarSilla(1,tiquete) 


                formulario_pasajero.botonAceptar.config(command=datosPasajero)

            formulario.botonAceptar.config(command=idViajeIngresado)

        transportadoras = Combobox(self.ventana_operaciones, values = nombres_transportadoras)
        transportadoras.pack(padx = 3, pady= 3)
        transportadoras.bind("<<ComboboxSelected>>",transportadoraSeleccionada)
#generacion de tiquete###

    def generarTiquete(self):
        self.label_proceso.config(text = "Compra de un tiquete")
        self.label_descripcion.config(text = "Permite realizar la compra de un tiquete para un viaje, buscando por destino o por destino y fecha.")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack()
        frame_botones = Frame(self.ventana_operaciones)
        frame_botones.pack(ipadx = 10, ipady =10, padx = 10, pady= 10)
        label = Label(frame_botones,text="Buscar viaje por:")
        label.grid(row = 0, column =0,columnspan=2)

        #buscar viaje por destino

        def buscarPorDestino():
            self.label_proceso.config(text = "Buscar por destino")
            self.label_descripcion.config(text = "Ingresa el destino al que quiere viajar")

            boton_destino["state"]=DISABLED
            boton_destino_fecha["state"]=DISABLED
            formulario_destino=FieldFrame(self.ventana_operaciones,"Criterio",["Destino"],"Valor",None,None,["string"])
            formulario_destino.botonAceptar.config(command=lambda:self.buscarViajes(formulario_destino))

        # se ejcuta si se eligió buscar un viaje por Destino y fecha
     

        def buscarPorDestinoYFecha():
            self.label_proceso.config(text = "Buscar por destino y fecha")
            self.label_descripcion.config(text = "Ingresa el destino y la fecha en la que quiere viajar")

            boton_destino_fecha["state"]=DISABLED
            boton_destino["state"]=DISABLED
            formulario_destino_fecha=FieldFrame(self.ventana_operaciones,"Criterio",["Destino","Fecha (DD-MM-AAAA)"],"Valor",None,None,["string","string"])
            formulario_destino_fecha.botonAceptar.config(command=lambda:self.buscarViajes(formulario_destino_fecha))

        boton_destino = Button(frame_botones,text = "Destino",font=("Segoe UI", 10),command=buscarPorDestino)
        boton_destino.grid(row=1,column=0,padx=2,ipadx=5)
        boton_destino_fecha = Button(frame_botones,text = "Destino y fecha",font = ("Segoe UI", 10),command=buscarPorDestinoYFecha)
        boton_destino_fecha.grid(row=1,column=1,padx=2,ipadx=5)

   
#agregar hospedaje

    def agregarHospedajeTiquete(self):
        self.label_proceso.config(text = "Añadir un hospedaje a su compra")
        self.label_descripcion.config(text = "Permite añadir un hospedaje a su tiquete,\nmostrando los hospedajes disponibles en el lugar de destino")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)
        formulario = FieldFrame(self.ventana_operaciones,"info",["ID del tiquete"],"",None,None,["int"])

   #que hospedaje se quiere escoger 

        def eventoAgregarHospedaje():
            self.label_descripcion.config(text = "Agregue un hospedaje a su tiquete de compra, seleccionando uno de la lista")
            formulario.pack_forget()

            try:
                hay_excepcion = formulario.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.agregarHospedajeTiquete()
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.agregarHospedajeTiquete()
                return

            if hay_excepcion:
                self.agregarHospedajeTiquete()
                return

            id_tiquete = formulario.valor_entradas[0]

            try:
                tiquete_solicitado =Admin.buscarTiqueteYHospedaje(int(id_tiquete), 1)

            except ExcepcionIdTiquete as awa:
                messagebox.showwarning(title="Advertencia",message= awa.mensaje_error_inicio)
                self.agregarHospedajeTiquete()
                return

            except ExcepcionAgregarHospedaje as uwu:
                messagebox.showwarning(title ="Advertencia",message = uwu.mensaje_error_inicio)
                self.agregarHospedajeTiquete()
                return

            lista_hospedajes=Hospedaje.buscarHospedajePorUbicacion(tiquete_solicitado.getVuelo().getDestino())
            if len(lista_hospedajes) == 0:
                mensaje = messagebox.showinfo(title = "Agregar Hospedaje",message = "No hay Hospedajes en ese destino.")
                return

        #disponibilidad segun hospedaje 
            def hospedajeSeleccionado(nombre):
                self.label_descripcion.config(text = "Ingrese los dias que se va a quedar en el Hospedaje seleccionado")

                self.ventana_operaciones.pack_forget()
                hospedaje_solicitado=Admin.solicitarHospedaje(tiquete_solicitado,nombre)
                if hospedaje_solicitado == None:
                    mensaje = messagebox.showinfo(title = "Agregar Hospedaje", message = "Ese Hospedaje no se encuentra  disponible")
                    return

                
                def diasDeEstadia():
                    self.label_descripcion.config(text = "Gracias por su compra! Este es su tiquete:")
                    self.ventana_operaciones.pack_forget()

                    try:
                        hay_excepcion =self.ventana_operaciones.aceptar()
                    except ExcepcionEnteroString as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        hospedajeSeleccionado(nombre)
                        return
                    except ExcepcionEnteroFloat as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        hospedajeSeleccionado(nombre)
                        return

                    if hay_excepcion:
                        hospedajeSeleccionado(nombre)
                        return

                    Admin.agregarHospedaje(tiquete_solicitado,hospedaje_solicitado,self.ventana_operaciones.valor_entradas[0])
                    self.ventana_operaciones = Label(self.frame)
                    self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)
                    self.ventana_operaciones.config(text=tiquete_solicitado.__str__())

                self.ventana_operaciones.pack_forget()
                self.ventana_operaciones = FieldFrame(self.frame,"Requisito",["Dias de estadia"],"valor",["1"],None,["int"])
                self.ventana_operaciones.botonAceptar.config(command=diasDeEstadia)
#tabla label
            label= Label(self.ventana_operaciones)
            label.pack()
            label["text"]+="\n"+ "-------------------------------------------------------------"
            label["text"]+="\n"+"{0:>10} {1:>15} {2:>18} {3:>12}".format("NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS")
            label["text"]+="\n"+"-------------------------------------------------------------"

            j = 0
            while j < len(lista_hospedajes):
                label_repetido =Label(self.ventana_operaciones)
                label_repetido.pack()
                label_repetido["text"]+="{0:>13} {1:>11} {2:>16} {3:>11}".format(lista_hospedajes[j].getNombre(), lista_hospedajes[j].getLocacion(), lista_hospedajes[j].getPrecio_dia(), lista_hospedajes[j].getEstrellas())
                label_repetido.bind("<ButtonPress-1>",lambda event,a=lista_hospedajes[j].getNombre():hospedajeSeleccionado(a))
                j += 1

            label_repetido["text"]+="\n"+"-------------------------------------------------------------"
            label_repetido["text"]+="\n"
            return

        formulario.botonAceptar.config(command=eventoAgregarHospedaje)

   #MODIFICA TIQUETE

    def modificarTiquete(self):
        self.label_proceso.config(text = "Modificar Tiquete")
        self.label_descripcion.config(text = "Puede modificar los atributos Silla y hospedajes (si ya tiene uno) de un tiquete comprado previamente")
        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)

       

        def editarTiquete():

            try:
                hay_excepcion = formulario.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.modificarTiquete()
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.modificarTiquete()
                return

            if hay_excepcion:
                self.modificarTiquete()
                return

            try:
                tiquete = Transportadora.BuscarTiquete(int(formulario.valor_entradas[0]))
            except ExcepcionIdTiquete as awa:
                messagebox.showwarning(title="Advertencia",message= awa.mensaje_error_inicio)
                self.modificarTiquete()
                return

            self.ventana_operaciones.pack_forget()
            self.ventana_operaciones = Frame(self.frame,relief="ridge",bd=2)
            self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2)
            label = Label(self.ventana_operaciones,text="Que opcion desea cambiar de su tiquete",font = ("Segoe UI", 10))
            label.grid(row =0,column=0 ,columnspan=2,ipadx=10,ipady=10)
            boton_modificar_hospedaje = Button(self.ventana_operaciones,text = "Modificar hospedaje",font=("Segoe UI", 10),command=lambda:modificarHospedaje(tiquete))
            boton_modificar_hospedaje.grid(row=1,column=0,padx=2,ipadx=5)
            boton_modificar_silla = Button(self.ventana_operaciones,text = "Modificar silla",font = ("Segoe UI", 10),command=lambda:self.modificarSilla(2,tiquete))
            boton_modificar_silla.grid(row=1,column=1,padx=2,ipadx=5)

        #modificahospedaje

        def modificarHospedaje(tiquete):
            self.label_proceso.config(text = "Modificar hospedajes")
            self.label_descripcion.config(text = "Cambie el hospedajes que agrego a su tiquete de compra, seleccionando uno nuevo de la lista")

            self.ventana_operaciones.pack_forget()
            self.ventana_operaciones = Frame(self.frame)
            self.ventana_operaciones.pack()

            try:
                tiquete_solicitado = Admin.buscarTiqueteYHospedaje(int(tiquete.getId()),2)

            except ExcepcionModificarHospedaje as uwu:
                messagebox.showwarning(title ="Advertencia",message = uwu.mensaje_error_inicio)
                self.modificarTiquete()
                return

            lista_hospedajes= Hospedaje.buscarHospedajePorUbicacion(tiquete_solicitado.getViaje().getDestino())
            if len(lista_hospedajes) == 0:
                mensaje = messagebox.showinfo(title = "Modificar hospedaje",message = "No hay hospedajes en ese destino.")
                return


            def hospedajeSeleccionado(nombre):
                self.label_descripcion.config(text = "Ingrese los dias que se va a quedar en el hospedaje seleccionado")

                hospedaje_solicitado=Admin.solicitarHospedajes(tiquete,nombre)
                if hospedaje_solicitado == None:
                    mensaje = messagebox.showinfo(title = "Modificar hospedaje", message = "no está disponible")
                    return
                self.ventana_operaciones.pack_forget()

               

                def diasDeEstadia():
                    self.label_descripcion.config(text = "Gracias por su compra! Este es su tiquete,feliz viaje :")
                    try:
                        hay_excepcion = self.ventana_operaciones.aceptar()
                    except ExcepcionEnteroString as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        hospedajeSeleccionado(nombre)
                        return
                    except ExcepcionEnteroFloat as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        hospedajeSeleccionado(nombre)
                        return

                    if hay_excepcion:
                        hospedajeSeleccionado(nombre)
                        return
                    self.ventana_operaciones.pack_forget()

                    Admin.agregarHospedaje(tiquete,hospedaje_solicitado,self.ventana_operaciones.valor_entradas[0])
                    messagebox.showinfo(title="Modificar hospedaje",message= "Su hospedajesha sido modificado con exito.")
                    self.ventana_operaciones = Label(self.frame)
                    self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)
                    self.ventana_operaciones.config(text=tiquete.__str__())

                self.ventana_operaciones = FieldFrame(self.frame,"Requisito",["Dias de estadia"],"valor",["1"],None,["int"])
                self.ventana_operaciones.botonAceptar.config(command=diasDeEstadia)

             #TABLE DE hospedajes
            label= Label(self.ventana_operaciones)
            label.pack()
            label["text"]+="\n"+ "-------------------------------------------------------------"
            label["text"]+="\n"+"{0:>10} {1:>15} {2:>18} {3:>12}".format("NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS")
            label["text"]+="\n"+"-------------------------------------------------------------"

            j = 0
            while j < len(lista_hospedajes):
                label_repetido =Label(self.ventana_operaciones)
                label_repetido.pack()
                label_repetido["text"]+="{0:>13} {1:>11} {2:>16} {3:>11}".format(lista_hospedajes[j].getNombre(), lista_hospedajes[j].getLocacion(), lista_hospedajes[j].getPrecio_dia(), lista_hospedajes[j].getEstrellas())
                label_repetido.bind("<ButtonPress-1>",lambda event,a=lista_alojamientos[j].getNombre():alojamientoSeleccionado(a))
                j += 1

            label_repetido["text"]+="\n"+"-------------------------------------------------------------"
            label_repetido["text"]+="\n"
            return

        formulario = FieldFrame(self.ventana_operaciones,"info",["ID del tiquete"],"",None,None,["int"])
        formulario.botonAceptar.config(command=editarTiquete)

 #MODIFICACION DE SILLAS

    def modificarSilla(self,numero, tiquete):
            self.ventana_operaciones.pack_forget()
            self.ventana_operaciones = Frame(self.frame)
            self.ventana_operaciones.pack()
            label_seleccion_silla = Label(self.ventana_operaciones,text="Seleccione el tipo de silla que desea.")
            label_seleccion_silla.pack()
            formulario=FieldFrame(self.ventana_operaciones,"Valores",["Clase","Ubicacion"],"Entradas",None,[True,False,False],["string","string"])
            formulario.botonBorrar.config(command=lambda:self.modificarSilla(numero,tiquete))

          
            def envioDatos():

                try:
                    hay_excepcion = formulario.aceptar()
                except ExcepcionStringNumero as owo:
                    messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                    self.modificarSilla(numero,tiquete)
                    return

                if hay_excepcion:
                    self.modificarSilla(numero,tiquete)
                    return

                self.label_descripcion.config(text = "Gracias por su compra! Este es su tiquete:")

                datos_silla= formulario.valor_entradas
                silla = Admin.elegirSilla(tiquete,datos_silla)

                if silla == None:
                    mensaje = messagebox.showinfo(title = "Elegir silla",message = "No tenemos sillas disponibles con esas caracteristicas.")
                    self.modificarSilla(numero,tiquete)
                    return

                formulario.pack_forget()
                Admin.modificarSilla(numero,tiquete,silla)
                messagebox.showinfo(title="Elegir",message = "Su silla ha sido asignada con exito.")
                self.ventana_operaciones.pack_forget()
                self.ventana_operaciones = Frame(self.frame)
                self.ventana_operaciones.pack()
                label_tiquete = Label(self.ventana_operaciones,text=tiquete.__str__())
                label_tiquete.pack()

            formulario.botonAceptar.config(command=envioDatos)


            def claseElegida(a):
                texto= formulario.entradas["Clase"].get()
                if str(texto).lower() == "ejecutiva":
                    formulario.entradas["Ubicacion"].grid_forget()
                    formulario.entradas["Ubicacion"] = Combobox(formulario,values=["Pasillo","Ventana"])
                    formulario.entradas["Ubicacion"].grid(row=2,column=1)
                else:
                    formulario.entradas["Ubicacion"].grid_forget()
                    formulario.entradas["Ubicacion"] = Combobox(formulario,values=["Pasillo","Ventana","Central"])
                    formulario.entradas["Ubicacion"].grid(row=2,column=1)

            formulario.entradas["Clase"].grid_forget()
            formulario.entradas["Clase"] =Combobox(formulario,values=["Ejecutiva","Economica"])
            formulario.entradas["Clase"].grid(row = 1, column = 1)
            formulario.entradas["Clase"].bind("<<ComboboxSelected>>",claseElegida)


    def listarPasajeros(self):
        self.label_proceso.config(text = "Listar pasajeros")
        self.label_descripcion.config(text = "Permite listar los pasajeros de un viaje al ingresar su respectivo ID")


        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)
        fromulario = FieldFrame(self.ventana_operaciones,"info",["ID del viaje"],"",["324"],None,["int"])
        label = Label(self.ventana_operaciones,justify=LEFT)
        label.pack()

    

        def tablaPasajeros():
            label["text"]=""

            try:
                hay_excepcion = fromulario.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.listarPasajeros()
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.listarPasajeros()
                return

            if hay_excepcion:
                self.listarPasajeros()
                return

            try:
                Admin.listarPasajeros(fromulario.valor_entradas[0],label)
            except ExcepcionEnteroString as awa:
                messagebox.showerror(title = "Error", message = awa.mensaje_error_inicio)
                self.listarPasajeros()
                return
            except ExcepcionEnteroFloat as awa:
                messagebox.showerror(title="Error",message=awa.mensaje_error_inicio)
                self.listarPasajeros()
                return
            except ExcepcionIdVuelo as awa:
                messagebox.showwarning(title="Aviso",message=awa.mensaje_error_inicio)
                self.listarPasajeros()
                return

        fromulario.botonAceptar.config(command=tablaPasajeros)

 

    def agregarViaje(self):
        self.label_proceso.config(text = "Agregar un viaje")
        self.label_descripcion.config(text = "Permite agregar un viaje para ser programado y ofrecido por una de nuestras transportadoras")


        criterios_vuelo = ["Transportadora","ID (3 cifras)","Precio","Origen","Destino","Distancia (km)","Fecha de salida (DD-MM-AAAA)","Hora de salida (24:00)","Terrestre","Nombre terrestre"]
        valores_def = ["","","","","","","","","Bus",""]
        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = FieldFrame(self.frame,"Datos",criterios_viaje,"Valores",valores_def,None,["string","int","int","string","string","int","string","string","string","string"])
        self.ventana_operaciones.entradas["Terrestre"].grid_forget()
        self.ventana_operaciones.entradas["Terrestre"] = Combobox(self.ventana_operaciones,values=["Bus","Buseta"] )
        self.ventana_operaciones.entradas["Terrestre"].grid(row = 9,column=1)

        self.ventana_operaciones.entradas["Transportadora"].grid_forget()
        self.ventana_operaciones.entradas["Transportadora"] = Combobox(self.ventana_operaciones,values=["Torcoroma","SolCaribe","Coonorte"] )
        self.ventana_operaciones.entradas["Transportadora"].grid(row = 1,column=1)

       

        def crearViaje():

            try:
                hay_excepcion =self.ventana_operaciones.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                return
            except ExcepcionStringNumero as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                return

            if hay_excepcion:
                return

            existe_viaje = Admin.agregarNuevoViaje(self.ventana_operaciones.valor_entradas)
            if existe_viaje:
                messagebox.showinfo(title="Agregar Viaje", message= "Ya existe un viaje con el ID ingresado.")
                return

            mensaje = messagebox.showinfo(title = "Agregar Viaje", message = "El viaje se ha agregado a la transportadora " + self.ventana_operaciones.valor_entradas[0] + " Exitosamente!")
        self.ventana_operaciones.botonAceptar.config(command=crearViaje)

    

    def cancelarViaje(self):
        self.label_proceso.config(text = "Cancelar un viaje")
        self.label_descripcion.config(text ="Puedes retirar un viaje de la lista de viajes disponibles, escribiendo el nombre del viaje\n (Puede ver el ID de cada viaje en opcion <Ver viajes disponibles por TRANSPORTADORA>)")

        criterios_cancelar_vuelo =["ID"]
        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = FieldFrame(self.frame,"Info",criterios_cancelar_viaje,"Valor",None,None,["int"])

    

        def eliminarViaje():

            try:
                hay_excepcion =self.ventana_operaciones.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.cancelarViaje()
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.cancelarViaje()
                return

            if hay_excepcion:
                self.cancelarViaje()
                return

            iD = int(self.ventana_operaciones.valor_entradas[0])
            viaje_encontrado = Admin.cancelarViajes(iD)

            if viaje_encontrado:
                mensaje = messagebox.showinfo(title = "Cancelar Viaje", message = "El viaje se ha cancelado exitosamente!")
            else:
                mensaje = messagebox.showinfo(title = "Cancelar Viaje", message = "No existe un viaje con ese ID.")

        self.ventana_operaciones.botonAceptar.config(command=eliminarViaje)


    def retirarBus(self):
        self.label_proceso.config(text = "Retirar un bus")
        self.label_descripcion.config(text = "Retira un bus que esté descompuesto y el viaje asociado a este\n (Puede ver los nombres de las terrestres en la opcion <Ver viajes  disponibles por Transportadoras>) ")

        criterios_retirar_bus=["Nombre Terrestre"]
        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = FieldFrame(self.frame,"Info",criterios_retirar_avion,"",None,None,["string"])

      

        def eliminarTerrestre():

            try:
                hay_excepcion =self.ventana_operaciones.aceptar()
            except ExcepcionStringNumero as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.retirarBus()
                return

            if hay_excepcion:
                self.retirarBus()

                return

            terrestre = self.ventana_operaciones.valor_entradas[0]
            terrestre_encontrada = Admin.retirarBus(terrestre)

            if terrestre_encontrada:
                mensaje = messagebox.showinfo(title = "Retirar bus", message = "Elbus  ha sido retirado.")
            else:
                mensaje = messagebox.showinfo(title = "Retirar bus ", message = "No tenemos un bus  con ese nombre.")

        self.ventana_operaciones.botonAceptar.config(command=eliminarTerrestre)

    

    def agregarHospedaje(self):
        self.label_proceso.config(text = "Agregar un Hospedaje")
        self.label_descripcion.config(text = "Permite agregar un Hospedaje a la lista de Hospedajes asociados")

        criterios_hospedaje =["Nombre Hospedaje","Locacion","Precio por dia","Numero de estrellas (1-5)"]
        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = FieldFrame(self.frame,"Datos",criterios_hospedaje,"VALORES",None,None,["string","string","int","int"])

     

        def crearHospedaje():

            try:
                hay_excepcion =self.ventana_operaciones.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.agregarHospedaje()
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.agregarHospedaje()
                return
            except ExcepcionStringNumero as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.agregarHospedaje()
                return

            if hay_excepcion:
                self.agregarHospedaje()
                return

            Admin.nuevoAlojamiento(self.ventana_operaciones.valor_entradas)
            mensaje = messagebox.showinfo(title = "Agregar Hospedaje", message = "El Hospedaje se ha agregado a nuestra lista exitosamente!")

        self.ventana_operaciones.botonAceptar.config(command=crearHospedaje)

   

    def eliminarHospedaje(self):
        self.label_proceso.config(text = "Eliminar un Hospedaje")
        self.label_descripcion.config(text = "Permite eliminar un Hospedaje de la lista de Hospedajes asociados, escribiendo el nombre del Hospedaje que se desea retirar")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)
        lista_hospedajess= Admin.obtenerHospedajes()

    

        def hospedajeSeleccionado(event):
            texto = combobox.get()
            nombre_hospedaje = texto.split("---")[0]
            hospedaje_encontrado = Admin.retirarHospedaje(nombre_hospedaje)
            if hospedaje_encontrado:
                mensaje = messagebox.showinfo(title = "Eliminar Hospedaje", message = "El Hospedaje se ha eliminado de nuestra lista exitosamente!")
            else:
                mensaje = messagebox.showinfo(title = "Eliminar Hospedaje", message = "El Hospedaje ya ha sido eliminado.")
        combobox = Combobox(self.ventana_operaciones,values=lista_hospedajes,width=50)
        combobox.pack()
        combobox.bind("<<ComboboxSelected>>",hospedajeSeleccionado)

    
    def ayuda(self):
        ayudaPopUp = messagebox.showinfo(title = "Programadores", message = "Valeria Guerra Sotomayor \n")


from Admin import Admin



