package uiMain;
import java.util.ArrayList;

import gestorhospedaje.Hospedaje;
import gestorviajes.Tiquete;
import gestorviajes.Transportadora;
import gestorviajes.Viaje;
public class TablasConsola implements GeneradorDeTablas {
public void mostrarTablaDeViajesDisponiblesPorTransportadoras(ArrayList<Transportadora> transportadoras)
	
	{
		for (int i = 0; i < transportadoras.size(); i++)
		{
			Transportadora transportadora = transportadoras.get(i);
			printEncabezadoTransportadora(transportadoras.get(i));
			printViajes(transportadora.viajesDisponibles(transportadora.getViajes())); 
			printSeparador();
		}	
	}
    @Override
	public void mostrarTablaDeViajesPorTransportadoras(ArrayList<Transportadora> transportadoras) 
	{
		for (int i = 0; i < transportadoras.size(); i++)
		{
			Transportadora transportadora = transportadoras.get(i);
			printEncabezadoTransportadora(transportadoras.get(i));
			printViajes(transportadora.getViajes()); 
			printSeparador();
		}	
	}
	
    @Override
    public void mostrarTablaDeViajes(Transportadora transportadora, ArrayList<Viaje> viajes) 
	{
		if (viajes.size() != 0)
		{
			printEncabezadoTransportadora(transportadora);
			printViajes(viajes);
			printSeparador();	
		}
	}
	
	@Override
	public void mostrarTablaDePasajeros(ArrayList<Tiquete> tiquetes) 
	{
		System.out.printf("%5s %12s %16s %17s","ID", "NOMBRE", "PASAPORTE", "EMAIL"+"\n");
		
		for (int i = 0; i < tiquetes.size(); i++){
			System.out.printf("%5s %13s %12s %26s",tiquetes.get(i).getId(), tiquetes.get(i).getPasajero().nombre, tiquetes.get(i).getPasajero().getPasaporte(), tiquetes.get(i).getPasajero().getEmail());
			System.out.println();  
		}
		System.out.println();
	}
	
	@Override
	public void mostrarTablaDeTransportadoras(ArrayList<Transportadora> transportadoras) 
	{
		System.out.println("TRANSPORTADORAS DISPONIBLES");

		for(Transportadora transportadora:transportadoras) 
		{
			System.out.printf("%14s",transportadora.getNombre());
			System.out.println();
		}
	}
	
	
	public void mostrarTablaDeHospedajes(ArrayList<Hospedaje> hospedajes)
	{
		System.out.println(); 
		System.out.printf("%10s %15s %18s %12s", "NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS");  
		System.out.println();  
		
		for (int j = 0; j < hospedajes.size(); j++) {
			System.out.format("%13s %11s %16s %11s", hospedajes.get(j).getNombre(), hospedajes.get(j).getLocacion(), hospedajes.get(j).getPrecio_dia(), hospedajes.get(j).getEstrellas());  
			System.out.println(); 
			}
		 
		System.out.println();
	}
	 
	static void printEncabezadoTransportadora(Transportadora transportadora) 
	{
		System.out.println("VIAJES DISPONIBLES DE LA TRANSPORTADORA " + transportadora.getNombre().toUpperCase());
		System.out.printf("%4s %13s %12s %14s %12s %22s %12s", "PLACA", "PRECIO", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA", "VEHICULO");  
		System.out.println();  
	
			}
	
	static void printViajes(ArrayList<Viaje> viajes) 
	{
		for (int j = 0; j < viajes.size(); j++) 
		{
			System.out.format("%5s %12s %13s %13s %15s %11s %21s", viajes.get(j).getID(), viajes.get(j).getPrecio(), viajes.get(j).getOrigen(),viajes.get(j).getDestino(), viajes.get(j).getFecha_de_salida(), viajes.get(j).getHora_de_salida(), viajes.get(j).getTerrestre());  
			System.out.println(); 
		}
	}
	
	static void printSeparador() 
	{
				System.out.println();	
	}





	
	

}
