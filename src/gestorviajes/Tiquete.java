package gestorviajes;
import java.io.Serializable;

import gestorhospedaje.Hospedaje;
import gestortaller.*;

public class Tiquete implements Serializable {

	private static final long serialVersionUID = 1L;
	private int id;
	private int precio;
	private Viaje viaje;
	private Silla silla;
	private Pasajero pasajero;
	private Hospedaje hospedaje;


	public Tiquete(int id, int precio, Viaje viaje) {
		this.id = id;
		this.precio = precio;
		this.viaje = viaje;
		viaje.getTiquetes().add(this);
	}
	public Tiquete(int id, int precio, Viaje viaje, Silla silla, Pasajero pasajero, Hospedaje hospedaje) {
		this.id = id;
		this.precio = precio;
		this.viaje = viaje;
		this.silla = silla;
		this.pasajero = pasajero;
		this.hospedaje = hospedaje;
		viaje.getTiquetes().add(this);
	}

	public boolean asignarPrecio() {
		boolean hayDescuento = false;
		int precio_total=viaje.getPrecio() + this.getSilla().getClase().getPrecio();
		if (pasajero.getEdad()<5) {
			hayDescuento = true;
			this.precio = (int) (precio_total - (precio_total*0.25));
		}else if (pasajero.getEdad()>5 && pasajero.getEdad()<=10){
			this.precio = (int) (precio_total - (precio_total*0.15));
			hayDescuento = true;
		}else {
			this.precio = precio_total;
		}
		return hayDescuento;
	}

	public void asignarPrecio(int num_dias) {
		int precio_total=viaje.getPrecio()+ hospedaje.calcularPrecio(num_dias) + this.getSilla().getClase().getPrecio();
		if (pasajero.getEdad()<5) {
			this.precio = (int) (precio_total - (precio_total*0.15));
		}else if (pasajero.getEdad()>5 && pasajero.getEdad()<=10){
			this.precio = (int) (precio_total - (precio_total*0.15));
		}else {
			this.precio = precio_total;
		}
	}
	
	public void confimarCompra() {
		this.viaje.getTiquetes().add(this);
	}

	public String toString()
	{
		if (this.hospedaje==null) {
			return  ""+
					"      Su compra ha sido exitosa\n"+
					"    Gracias por confiar en nostros\n"+
					""+

					""+
					"      Tiquete No."+ this.id + "\n"+
					""+
					"Nombre Pasajero: " + pasajero.nombre + "\n" +
					"Fecha: " + viaje.getFecha_de_salida() + "\n" +
					"Viaje: " + viaje.getID() + "\n" +
					"Num Silla: " + silla.getNumero_de_silla() + " "  + silla.getUbicacion() + "\n" +
					"Origen: " + viaje.getOrigen() + "\n" +
					"Destino: " + viaje.getDestino() + "\n" +
					"Precio Total: " + this.getPrecio() + "\n" +
					"";


		}else {
			
			return  ""+
					"      Su compra ha sido exitosa\n"+
					"    Gracias por confiar en nostros\n"+
					""+
					""+
					"      Tiquete No."+ this.id + "\n"+
					""+
					"Nombre Pasajero: " + pasajero.nombre + "\n" +
					"Fecha: " + viaje.getFecha_de_salida() + "\n" +
					"Viaje: " + viaje.getID() + "\n" +
					"Silla: " + silla.getNumero_de_silla() + " - "  + silla.getUbicacion()  + "\n" +
					"Origen: " + viaje.getOrigen() + "\n" +
					"Destino: " + viaje.getDestino() + "\n" +
					"Alojamiento: " + hospedaje.getNombre() + "\n" +
					"Precio Total: " + this.getPrecio() + "\n" +
					"";
		}
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getPrecio() {
		return precio;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
	}
	public Viaje getViaje() {
		return viaje;
	}
	public void setViaje(Viaje viaje) {
		this.viaje = viaje;
	}
	public Silla getSilla() {
		return silla;
	}
	public void setSilla(Silla silla) {
		this.silla = silla;
		silla.setEstado(false);
	}
	public Pasajero getPasajero() {
		return pasajero;
	}
	public void setPasajero(Pasajero pasajero) {
		this.pasajero = pasajero;
	}
	public Hospedaje getHospedaje() {
		return hospedaje;
	}
	public void setHospedaje(Hospedaje Hospedaje) {
		this.hospedaje = hospedaje;
	}
}
