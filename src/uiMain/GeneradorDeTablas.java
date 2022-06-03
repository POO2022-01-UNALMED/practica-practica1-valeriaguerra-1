
package uiMain;
import java.util.ArrayList;

import gestorhospedaje.*;
import gestorviajes.*;
public interface GeneradorDeTablas{
	public abstract void mostrarTablaDeViajesDisponiblesPorTransportadoras(ArrayList<Transportadora> transportadoras);
	public abstract void mostrarTablaDeViajesPorTransportadoras(ArrayList<Transportadora> transportadoras);
	public abstract void mostrarTablaDeViajes(Transportadora transportadoras, ArrayList<Viaje> viajes);
	public abstract void mostrarTablaDePasajeros(ArrayList<Tiquete> tiquetes);
	public abstract void mostrarTablaDeTransportadoras(ArrayList<Transportadora> transportadoras);
	public abstract void mostrarTablaDeHospedajes(ArrayList<Hospedaje> hospedajes);
}
