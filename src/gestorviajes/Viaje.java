 
package gestorviajes;
import java.io.Serializable;
import java.util.ArrayList;

import gestortaller.*;

public class Viaje implements Serializable{

	private static final long serialVersionUID = 1L;
	
	private int ID;
	private int precio;
	private String origen;
	private String destino;
	private Terrestre terrestre;
	private double distancia_en_km;
	private String fecha_de_salida;
	private String hora_de_salida;
	private boolean estaCompleto;
	private ArrayList<Tiquete> tiquetes = new ArrayList<Tiquete>();
	
	public Viaje(int iD, int precio, String origen, String destino, Terrestre terrestre, double distancia, String fecha_de_salida, String hora_de_salida) {
		ID = iD;
		this.precio = precio;
		this.origen = origen;
		this.destino = destino;
		this.terrestre = terrestre;
		this.distancia_en_km = distancia;
		this.fecha_de_salida = fecha_de_salida;
		this.setHora_de_salida(hora_de_salida);
		this.getTerrestre().getTransportadora().agregarViaje(this);
	}

	
	public Tiquete buscarTiquetePorID(ArrayList<Tiquete> tiquetes, int ID)
	{
		for(int i = 0; i < tiquetes.size(); i++)
		{
			if (tiquetes.get(i).getId() == ID)
			{
				return tiquetes.get(i);
			}
		}
		return null;
	}


	//GETTERS Y SETTERS

	public int getID() {
		return ID;
	}

	public void setID(int iD) {
		ID = iD;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}

	public String getOrigen() {
		return origen;
	}

	public void setOrigen(String origen) {
		this.origen = origen;
	}

	public String getDestino() {
		return destino;
	}

	public void setDestino(String destino) {
		this.destino = destino;
	}

	//mirar la clase abstracta se organiza 
	public Terrestre getTerrestre() {
		return terrestre;
	}

	public void setAeronave(Terrestre terrestre) {
		this.terrestre = terrestre;
	}

	public double getDistancia_en_km() {
		return distancia_en_km;
	}

	public void setDistancia_en_km(double distancia_en_km) {
		this.distancia_en_km = distancia_en_km;
	}

	public String getFecha_de_salida() {
		return fecha_de_salida;
	}

	public void setFecha_de_salida(String fecha_de_salida) {
		this.fecha_de_salida = fecha_de_salida;
	}

	public ArrayList<Tiquete> getTiquetes() {
		return tiquetes;
	}

	public void setTiquetes(ArrayList<Tiquete> tiquetes) {
		this.tiquetes = tiquetes;
	}

	public String getHora_de_salida() {
		return hora_de_salida;
	}

	public void setHora_de_salida(String hora_de_salida) {
		this.hora_de_salida = hora_de_salida;
	}

	public boolean isEstaCompleto() {
		return estaCompleto;
	}

	public void setEstaCompleto(boolean estaCompleto) {
		this.estaCompleto = estaCompleto;
	}
}
