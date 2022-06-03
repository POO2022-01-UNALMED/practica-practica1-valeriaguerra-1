package gestortaller;
import java.io.Serializable;

import gestorviajes.*;
public abstract class Terrestre implements Serializable{

	
	
	protected final  int GASTO_GASOLINA = 120;
	private String nombre;
	private Transportadora transportadora;
	private boolean descompuesto;
	private Silla[] SILLAS_ECONOMICAS;
	private Silla[] SILLAS_EJECUTIVAS;

	protected Terrestre(String nombre, Transportadora transportadora) {
		this.nombre = nombre;
		this.transportadora = transportadora;
	}

	public Transportadora getTransportadora() {
		return transportadora;
	}

	public void setTransportadora(Transportadora transportadora) {
		this.transportadora = transportadora;
	}

	public Silla[] getSILLASECONOMICAS() {
		return SILLAS_ECONOMICAS;
	}

	public void setSILLASECONOMICAS(Silla[] sILLAS_ECONOMICAS) {
		SILLAS_ECONOMICAS = sILLAS_ECONOMICAS;
	}

	public Silla[] getSILLASEJECUTIVAS() {
		return SILLAS_EJECUTIVAS;
	}

	public void setSILLASEJECUTIVAS(Silla[] sILLAS_EJECUTIVAS) {
		SILLAS_EJECUTIVAS = sILLAS_EJECUTIVAS;
	}

	public int getGastoGasolina() {
		return GASTO_GASOLINA;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public boolean isDescompuesto() {
		return descompuesto;
	}

	public void setDescompuesto(boolean descompuesto) {
		this.descompuesto = descompuesto;
	}

	public String toString() {
		return this.nombre;
	}

	public Silla buscarSillaPorUbicacionyTipo(Ubicacion ubicacion, String tipo) {
		if (tipo.equalsIgnoreCase("ECONOMICA")) {
			for (Silla i : SILLAS_ECONOMICAS) {
				if (i.isEstado() & i.getUbicacion().equals(ubicacion)) {
					return i;
				}
			}
		} else if (tipo.equalsIgnoreCase("EJECUTIVA")) {
			for (Silla i : SILLAS_EJECUTIVAS) {
				if (i.isEstado() & i.getUbicacion().equals(ubicacion)) {
					return i;
				}
			}
		}
		return null;
	}
	
	public String Calcular_Sillas_Ocupadas() {
		int cont = 0;
		for (Silla i : this.getSILLASECONOMICAS()) {
			if (i.isEstado()) {
				cont += 1;
			}
		}
		for (Silla j : this.getSILLASEJECUTIVAS()) {
			if (j.isEstado()) {
				cont += 1;
			}
		}
		return "Esta es la cantidad de silla ocupadas:"+cont;
	}

	public abstract double Calcular_Consumo_Gasolina(double distancia_en_km);
}
