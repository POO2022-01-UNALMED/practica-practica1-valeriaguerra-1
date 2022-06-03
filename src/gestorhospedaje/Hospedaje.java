package gestorhospedaje;
import java.io.Serializable;
import java.util.ArrayList;

public class Hospedaje implements Serializable {
	private static final long serialVersionUID = 1L;
	private String nombre;
	private String locacion;
	private long precio_dia;
	private int estrellas;
	private static ArrayList<Hospedaje> hospedajes = new ArrayList<Hospedaje>();

	//CONSTRUCTORES
	public Hospedaje(String nombre, String locacion, long precio_dia, int estrellas) {
		this.nombre = nombre;
		this.locacion = locacion;
		this.precio_dia = precio_dia;
		this.estrellas = estrellas;
		hospedajes.add(this);
	}
	public int calcularPrecio(int dias) {
		return (int)( dias * this.precio_dia);
	}

	public static ArrayList<Hospedaje> buscarHospedajePorUbicacion (String ubicacion) {
		ArrayList<Hospedaje> hospedajesEnUbicacion = new ArrayList<Hospedaje>();
		for (int i = 0; i < hospedajes.size(); i++)
		{
		  if (hospedajes.get(i).getLocacion().equalsIgnoreCase(ubicacion))
		  {
			  hospedajesEnUbicacion.add(hospedajes.get(i));
		  }
		}
		return hospedajesEnUbicacion;
	}
	
	public static Hospedaje buscarHospedajePorNombre(String nombre) {
		for (int i = 0; i < hospedajes.size(); i++)
		{
		  if (hospedajes.get(i).getNombre().equalsIgnoreCase(nombre))
		  {
			  return hospedajes.get(i);
		  }
		}
		return null;
	}


		public void setLocacion(String locacion) {
			this.locacion = locacion;
		}

		public void setPrecio_dias(long precio_dias) {
			this.precio_dia = precio_dias;
		}

		public static ArrayList<Hospedaje> getHospedajes() {
			return hospedajes;
		}

		public static void setAlojamientos(ArrayList<Hospedaje> hospedajes) {
			Hospedaje.hospedajes = hospedajes;
		}

		public long getPrecio_dia() {
			return precio_dia;
		}

		public void setPrecio_dia(long precio_dia) {
			this.precio_dia = precio_dia;
		}

		public String getLocacion() {
			return locacion;
		}

		public int getEstrellas() {
			return estrellas;
		}

		public void setEstrellas(int estrellas) {
			this.estrellas = estrellas;
		}

		public String getNombre() {
			return nombre;
		}

		public void setNombre(String nombre) {
			this.nombre = nombre;
		}

	}