

from excepciones.ErrorAplicacion import ErrorAplicacion


class ErrorAsignacion(ErrorAplicacion):
    
    def __init__(self, mensaje):
        self.mensaje_error_asigancion = f" Error de existencia: {mensaje}"
        super().__init__(self.mensaje_error_asigancion)


class ExcepcionAgregarHospedaje(ErrorAsignacion):

    def __init__(self, id):
        self.mensaje_error = f"\nEl tiquete con ID {id} ya posee un hospedaje, si quiere cambiarlo debe hacerlo desde la opcion <Modificar tiquete>"
        super().__init__(self.mensaje_error)

class ExcepcionModificarHospedaje(ErrorAsignacion):
    
    def __init__(self, id):
        self.mensaje_error = f"\nEl tiquete con ID {id} aun no posee Hospedaje, si desea agregar uno debe hacerlo desde la opcion <Agregar Hospedaje>"
        super().__init__(self.mensaje_error)

class ExcepcionIdViaje(ErrorAsignacion):

     def __init__(self, id):
         self.mensaje_error = f"\nNo existe un viaje con el ID: {id}"
         super().__init__(self.mensaje_error)

class ExcepcionIdTiquete(ErrorAsignacion):

    def __init__(self, id):
        self.mensaje_error = f"\nNo existe un tiquete con el ID: {id}"
        super().__init__(self.mensaje_error)