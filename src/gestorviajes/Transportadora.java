package gestorviajes;
import java.io.Serializable;
import java.util.ArrayList;

import gestortaller.*;
public class Transportadora implements Serializable{

	private static final long serialVersionUID = 1L;
	
	private String nombre;
	private ArrayList<Terrestre> terrestres = new ArrayList<Terrestre>();
	private ArrayList<Viaje> viajes = new ArrayList<Viaje>();
	private static ArrayList<Transportadora> transportadoras = new ArrayList<Transportadora>();

	//CONSTRUCTOR
	public Transportadora(String nombre) {
		this.nombre = nombre;
		transportadoras.add(this);
	}

	@Override
	public String toString() {
		return this.nombre;
	}


	public static Transportadora buscarTransportadoraPorNombre(String nombre2)
	{
		Transportadora retorno = null;
		for (int i = 0; i <Transportadora.getTransportadoras().size(); i++)
		{
			if( Transportadora.getTransportadoras().get(i).getNombre().equalsIgnoreCase(nombre2))
			{
				retorno=  Transportadora.getTransportadoras().get(i);
			}
		}
		return retorno;
	}


	public Viaje buscarViajePorID (ArrayList<Viaje> viajes, int ID)
	{
		for (int i = 0; i < viajes.size(); i++)
		{
		  if (viajes.get(i).getID() == ID )
		  {
			  return viajes.get(i);
		  }
		}
		return null;
	}
	
	
	public Viaje buscarViajePorTerrestre (ArrayList<Viaje> viajes, String nombre_Terrestre)
	{
		for (int i = 0; i < viajes.size(); i++)
		{
		  if (viajes.get(i).getTerrestre().getNombre().equals(nombre_Terrestre) )
		  {
			  return viajes.get(i);
		  }
		}
		return null;
	}
	
	
	public ArrayList<Viaje> buscarViajePorDestino (ArrayList<Viaje> viajes, String destino)
	{
		ArrayList<Viaje> viajesPorDestino = new ArrayList<Viaje>();
		for (int i = 0; i < viajes.size(); i++)
		{
		  if (viajes.get(i).getDestino().equalsIgnoreCase(destino)) 
		  {
			  viajesPorDestino.add(viajes.get(i));
		  }
		}
		return viajesPorDestino;
	}

	public ArrayList<Viaje> buscarViajePorFecha (ArrayList<Viaje> viajes, String fecha)
	{
		ArrayList<Viaje> viajesPorFecha = new ArrayList<Viaje>();
		for (int i = 0; i < viajes.size(); i++)
		{
		  if (viajes.get(i).getFecha_de_salida().equals(fecha))
		  {
			  viajesPorFecha.add(viajes.get(i));
		  }
		}
		return viajesPorFecha;
	}

	

	public ArrayList<Viaje> viajesDisponibles(ArrayList<Viaje> viajes)
	{
		ArrayList<Viaje> viajesDisponibles = new ArrayList<Viaje>();
		for (int i = 0; i < viajes.size(); i++)
		{
			if (!viajes.get(i).isEstaCompleto())
			{
				viajesDisponibles.add(viajes.get(i));
			}
		}
		return viajesDisponibles;
	}

	public void agregarViaje(Viaje viaje)
	{
		viajes.add(viaje);
	}

	
	public Boolean cancelarViaje(int viaje_a_eliminar)
	{
		for (int i = 0; i < viajes.size(); i++)
		{
		  if (viajes.get(i).getID() == viaje_a_eliminar )
		  {
			  viajes.remove(i);
			  return true;
		  }
		}
		return false;
	}

	
	public static Tiquete BuscarTiquete(int ID)
	{
		ArrayList<Transportadora> transportadorasDisponibles = Transportadora.getTransportadoras();
		for (int i = 0; i < transportadorasDisponibles.size(); i++)
		{
			Transportadora transportadora = transportadorasDisponibles.get(i);
			for (int j = 0; j < transportadora.getViajes().size(); j++)
			{

				Viaje viaje = transportadora.getViajes().get(j);
				Tiquete tiquete_buscado = viaje.buscarTiquetePorID(viaje.getTiquetes(), ID);
				if (tiquete_buscado != null)
				{
					return tiquete_buscado;
				}
			}
		}
		return null;
	}
	  

	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public ArrayList<Viaje> getViajes() {
		return viajes;
	}


	public void setViajes(ArrayList<Viaje> viajes) {
		this.viajes = viajes;
	}

	public ArrayList<Terrestre> getTerrestres() {
		return terrestres;
	}

	public void setBuses(ArrayList<Terrestre> buses) {
		this.terrestres = buses;
	}

	public static ArrayList<Transportadora> getTransportadoras() {
		return transportadoras;
	}

	public static void setTransportadoras(ArrayList<Transportadora> transportadoras) {
		Transportadora.transportadoras = transportadoras;
	}
}
