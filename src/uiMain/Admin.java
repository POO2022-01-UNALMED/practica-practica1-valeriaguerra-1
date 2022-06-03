// CLASE ADMIN PARA LA INTERACCION DEL USUARIO CON EL SISTEMA
//generación de tiquet

package uiMain;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Scanner;
import gestortaller.*;
import gestorviajes.*;
import gestorhospedaje.Hospedaje;

import java.lang.Math;

public class Admin {
	static Scanner sc = new Scanner(System.in);
	static GeneradorDeTablas generadorDeTablas = new TablasConsola();

	public static void main(String[] args) {	
		Transportadora Torcomora = new Transportadora("Torcomora");		
		Bus Bus_1 = new Bus("VGS-279",Torcomora);
		Bus Bus_2 = new Bus("D-777",Torcomora);
		Bus Bus_3 = new Bus("GHI-800", Torcomora);
		Bus Bus_4 = new Bus("JKL-690",Torcomora);
		Bus Bus_5 = new Bus("MN�-777",Torcomora);
		Buseta Buseta_1 = new Buseta("XXX-120",Torcomora);
		Buseta Buseta_2 = new Buseta("MDG-80",Torcomora);
		
		Viaje viaje1C = new Viaje(001, 300000, "Monteria", "Bogota", Bus_1, 214.88, "12-10-2022", "14:00");
		Viaje viaje2C = new Viaje(002, 320000, "Monteria", "Bogota", Bus_2, 214.88, "31-11-2022", "16:00");
		Viaje viaje3C = new Viaje(003,17000,"Monteria","Pica Pica",Buseta_1,8017,"11-12-2022","05:00");
		Viaje viaje4C = new Viaje(004,230000,"Pasto","Monteria",Buseta_2,1039,"24-12-2022","12:00");
		Viaje viaje5C = new Viaje(005,132000,"Medellin","Cartagena",Bus_3,973,"13-11-2022","07:00");
		Viaje viaje6C = new Viaje(006,1320000,"Monteria","Leticia",Bus_4,774,"29-10-2022","16:00");
		Viaje viaje7C = new Viaje(0077,290000,"Monteria","Bogota",Bus_4,233,"06-10-2022","13:00");
		
		Tiquete tiquete1C1 = new Tiquete(564, viaje1C.getPrecio(), viaje1C);
		Tiquete tiquete2C1 = new Tiquete(286, viaje1C.getPrecio(), viaje1C);
		Tiquete tiquete3C1 = new Tiquete(124, viaje1C.getPrecio(), viaje1C);
		Pasajero pasajero1C1 = new Pasajero( "AS1234", "Armando", tiquete1C1, 32, "Armando123@yahoo.es");
		Pasajero pasajero2C1 = new Pasajero( "AS2463", "Clara", tiquete2C1, 28, "ClaraLuna@gmail.com");
		Pasajero pasajero3C1 = new Pasajero( "BS2145", "Ana", tiquete3C1, 4, "ClaraLuna@gmail.com");
		tiquete1C1.setSilla(Bus_1.getSILLASEJECUTIVAS()[1]);
		tiquete2C1.setSilla(Bus_1.getSILLASEJECUTIVAS()[2]);
		tiquete3C1.setSilla(Bus_1.getSILLASEJECUTIVAS()[3]);
		
		Tiquete tiquete1C3 = new Tiquete(287, viaje3C.getPrecio(), viaje3C);
		Tiquete tiquete2C3 = new Tiquete(283, viaje3C.getPrecio(), viaje3C);
		Pasajero pasajero1C3 = new Pasajero( "AS1111", "Vanessa", tiquete1C3, 18, "VanessaG@gmail.com");
		Pasajero pasajero2C3 = new Pasajero( "CS1259", "Sara", tiquete2C3, 19, "SaraGeo@gmail.com");
		
		Tiquete tiquete1C4 = new Tiquete(441, viaje4C.getPrecio(), viaje4C);
		Pasajero pasajero1C4 = new Pasajero("AB7632","Sandra",tiquete1C4,36,"sandra123@gmail.com");
		tiquete1C4.setSilla(Buseta_2.getSILLASECONOMICAS()[1]);
		
		Tiquete tiquete1C7 = new Tiquete(661, viaje7C.getPrecio(), viaje7C);
		Tiquete tiquete2C7 = new Tiquete(662, viaje7C.getPrecio(), viaje7C);
		Tiquete tiquete3C7 = new Tiquete(663, viaje7C.getPrecio(), viaje7C);
		Pasajero pasajero1C7 = new Pasajero( "AS1254", "Alfonso", tiquete1C7, 32, "Alfonso123@yahoo.es");
		Pasajero pasajero2C7 = new Pasajero( "AS2433", "Carlos", tiquete2C7, 25, "carlos43@gmail.com");
		Pasajero pasajero3C7 = new Pasajero( "BS2143", "David", tiquete3C7, 14, "carlos43@gmail.com");
		tiquete1C7.setSilla(Bus_5.getSILLASEJECUTIVAS()[1]);
		tiquete2C7.setSilla(Bus_5.getSILLASEJECUTIVAS()[2]);
		tiquete3C7.setSilla(Bus_5.getSILLASEJECUTIVAS()[3]);
		
		
		Transportadora Montrapi = new Transportadora("Montrapi");
	
		Bus bus1A = new Bus("ArbusA330", Montrapi);
		Bus bus2A = new Bus("ATR72", Montrapi);
		Buseta buseta1A = new Buseta("fdsfasdf 787", Montrapi);
		Buseta buseta2A = new Buseta("Cessna120", Montrapi);
		Buseta buseta3A = new Buseta("Cessna172", Montrapi);
		
		Viaje viaje1A = new Viaje(213, 200000, "Cartago", "Cartagena", buseta1A, 473.22, "15-10-2022", "15:00");
		Viaje viaje2A= new Viaje(214, 1680000, "Monteria", "Cali",  bus1A, 8033.74, "11-12-2022", "17:00");
		Viaje viaje3A = new Viaje(215, 280000, "Monteria", "Bogota", bus2A, 214.88, "17-12-2022", "16:00");
		Viaje viaje4A = new Viaje(213, 495000, "Bucaramanga", "Cartagena", buseta2A, 773, "30-11-2022", "06:00");
		Viaje viaje5A = new Viaje(216, 648000, "Medellin", "Chucurri", buseta3A, 1039, "15-10-2022", "10:00");
		
		Tiquete tiquete1A1 = new Tiquete(442, viaje1A.getPrecio(), viaje1A);
		Tiquete tiquete2A1 = new Tiquete(443, viaje1A.getPrecio(), viaje1A);
		Tiquete tiquete3A1 = new Tiquete(447, viaje1A.getPrecio(), viaje1A);
		Pasajero pasajero1A1 = new Pasajero( "AS4234", "Alison", tiquete1A1, 32, "alison56@yahoo.es");
		Pasajero pasajero2A1 = new Pasajero( "AS5463", "Estiven", tiquete2A1, 11, "estiven@gmail.com");
		Pasajero pasajero3A1 = new Pasajero( "BS7145", "Camilo", tiquete3A1, 3, "alison56@gmail.com");
		tiquete1A1.setSilla(buseta1A.getSILLASEJECUTIVAS()[1]);
		tiquete2A1.setSilla(buseta1A.getSILLASEJECUTIVAS()[2]);
		tiquete3A1.setSilla(buseta1A.getSILLASEJECUTIVAS()[3]);
		
		Tiquete tiquete1A4 = new Tiquete(563, viaje4A.getPrecio(), viaje4A);
		Tiquete tiquete2A4 = new Tiquete(285, viaje4A.getPrecio(), viaje4A);
		Tiquete tiquete3A4 = new Tiquete(125, viaje4A.getPrecio(), viaje4A);
		Pasajero pasajero1A4 = new Pasajero( "AS1534", "Anderson", tiquete1A4, 32, "anderson76@yahoo.es");
		Pasajero pasajero2A4 = new Pasajero( "AS2763", "Cristian", tiquete2A4, 60, "cristian@gmail.com");
		Pasajero pasajero3A4 = new Pasajero( "BS2945", "Jorge", tiquete3A4, 33, "jorge1999@gmail.com");
		tiquete1A4.setSilla(buseta2A.getSILLASEJECUTIVAS()[1]);
		tiquete2A4.setSilla(buseta2A.getSILLASEJECUTIVAS()[2]);
		tiquete3A4.setSilla(buseta2A.getSILLASEJECUTIVAS()[3]);
	
		
		Transportadora Velozn = new Transportadora("Velozn");
		
		Bus bus1H = new Bus("Boeing737", Velozn);
		Bus bus2H = new Bus("PilatusPC-6", Velozn);
		Bus bus3H = new Bus("AirbusA350", Velozn);
		Bus bus4H = new Bus("AirbusA380", Velozn);
		Bus bus5H = new Bus("Boeing777", Velozn);
		Buseta buseta1H = new Buseta("Cessna",Velozn);
		
		Viaje viaje1H = new Viaje(329,1500000,"Medellin","SanAndres",bus1H,8806,"13-11-2022","15:00");
		Viaje viaje2H = new Viaje(328,1500000,"Cartagena","Cali",bus2H,773,"13-10-2022","11:00");
		Viaje viaje3H = new Viaje(327,1500000,"Medellin","Pasto",bus3H,731,"13-12-2022","08:00");
		Viaje viaje4H = new Viaje(326,1500000,"Rionegro", "Bogota",bus4H,214.88,"31-11-2022","07:00");
		Viaje viaje5H = new Viaje(325,1500000,"Medellin","Amazonas",bus5H,1792,"12-12-2022","17:00");
		Viaje viaje6H = new Viaje(324,1500000,"Amazonas","Cali",buseta1H,774,"13-11-2022","13:00");
		
		
		Tiquete tiquete5H6 = new Tiquete(563, viaje6H.getPrecio(), viaje6H);
		Tiquete tiquete6H6 = new Tiquete(285, viaje6H.getPrecio(), viaje6H);
		Tiquete tiquete7H6 = new Tiquete(125, viaje6H.getPrecio(), viaje6H);
		Pasajero pasajero5H6 = new Pasajero( "AS1234", "Andrey", tiquete5H6, 26, "andrey76@yahoo.es");
		Pasajero pasajero6H6 = new Pasajero( "AS1235", "Manuela", tiquete6H6, 19, "manuela123@gmail.com");
		Pasajero pasajero7H6 = new Pasajero( "BS1236", "Hugo", tiquete7H6, 37, "hugo@gmail.com");
		tiquete5H6.setSilla(buseta1H.getSILLASECONOMICAS()[1]);
		tiquete6H6.setSilla(buseta1H.getSILLASECONOMICAS()[2]);
		tiquete7H6.setSilla(buseta1H.getSILLASECONOMICAS()[3]);		
		
		Tiquete tiquete1H6 = new Tiquete(551,viaje6H.getPrecio(),viaje6H);
		Tiquete tiquete2H6 = new Tiquete(552,viaje6H.getPrecio(),viaje6H);
		Tiquete tiquete3H6 = new Tiquete(553,viaje6H.getPrecio(),viaje6H);
		Tiquete tiquete4H6 = new Tiquete(554,viaje6H.getPrecio(),viaje6H);
		Pasajero pasajero1H6 = new Pasajero("ABC111","Adolfo",tiquete1H6,18,"adolfo@gmail.com");
		Pasajero pasajero2H6 = new Pasajero("ABC112","Veronica",tiquete2H6,21,"veronica@gmail.com");
		Pasajero pasajero3H6 = new Pasajero("ABC113","Sebastian",tiquete3H6,22,"sebastian@gmail.com");
		Pasajero pasajero4H6 = new Pasajero("ABC114","Katherine",tiquete4H6,25,"katherine@gmail.com");
		tiquete1H6.setSilla(buseta1H.getSILLASEJECUTIVAS()[0]);
		tiquete2H6.setSilla(buseta1H.getSILLASEJECUTIVAS()[1]);
		tiquete3H6.setSilla(buseta1H.getSILLASEJECUTIVAS()[2]);
		tiquete4H6.setSilla(buseta1H.getSILLASEJECUTIVAS()[3]);
		
		Tiquete tiquete1H3 = new Tiquete(563, viaje3H.getPrecio(), viaje3H);
		Tiquete tiquete2H3 = new Tiquete(285, viaje3H.getPrecio(), viaje3H);
		Tiquete tiquete3H3 = new Tiquete(125, viaje3H.getPrecio(), viaje3H);
		Pasajero pasajero1H3 = new Pasajero( "AS1237", "Fabio", tiquete1H3, 32, "fabio001@yahoo.es");
		Pasajero pasajero2H3 = new Pasajero( "AS1238", "Leonardo", tiquete2H3, 40, "leonardo578@gmail.com");
		Pasajero pasajero3H3 = new Pasajero( "BS1239", "Vanessa", tiquete3H3, 21, "vane456@gmail.com");
		tiquete1H3.setSilla(bus3H.getSILLASECONOMICAS()[1]);
		tiquete2H3.setSilla(bus3H.getSILLASECONOMICAS()[2]);
		tiquete3H3.setSilla(bus3H.getSILLASECONOMICAS()[3]);
		
		Hospedaje hospedaje1 = new Hospedaje("Los Caracoles", "Monteria", 41885, 3);
		Hospedaje hospedaje2 = new Hospedaje("Las Margaras", "San Pelayo", 215000, 5);
		Hospedaje hospedaje3 = new Hospedaje("HouseCampero", "Caucasia", 30079, 2);
		Hospedaje hospedaje4 = new Hospedaje("Viajero", "Puerto Escondido", 66000, 4);
		Hospedaje hospedaje5 = new Hospedaje("Bocagrande", "Cartagena", 167270, 4);
		Hospedaje hospedaje6 = new Hospedaje("BellaMar", "Cartagena", 74029, 3);
		Hospedaje hospedaje7 = new Hospedaje("Ibis", "Cali", 155000, 5);
		Hospedaje hospedaje8 = new Hospedaje("Estelar", "Cartagena", 346378, 5);
		Hospedaje hospedaje9 = new Hospedaje("SeaAvenue", "SanAndres", 472388, 5);
		Hospedaje hospedaje10 = new Hospedaje("Ataraxy", "SanAndres", 280795, 4);
		Hospedaje hospedaje11 = new Hospedaje("SolCaribe", "SanAndres", 105000, 3);
		Hospedaje hospedaje12 = new Hospedaje("Monaco", "Pasto", 40000, 2);
		
		int opcion;
		do {
			System.out.println("---- TERMINAL TRANSPORTE MONTELIVANO ---");
			System.out.println("1. Administrador");
			System.out.println("2. Comprar tiquete para un viaje por destino y fecha");
			System.out.println("3. Agregar hospedaje en el destino del viaje");
			System.out.println("4. Modificar tiquete comprado");
			System.out.println("5. Ver disponibilidad de viajes por Transportadora");
			System.out.println("6. Terminar");
			System.out.println("Por favor escoja una opcion: ");
			opcion = sc.nextInt();
		
			switch (opcion) {
				case 1:
					;
					opcionesAdministrador();
					break;
				case 2:
					generarTiquete();
					break;
				case 3:
					agregarHospedaje();
					break;
				case 4:
					modificarTiquete();
					break;
				case 5:
					mostrarViajesPorTransportadoras();
					break;
				case 6:
					salirDelSistema();

					break;
			}
		} while (opcion != 6);
	}

	static void mostrarViajesPorTransportadoras() {
		ArrayList<Transportadora> transportadorasDisponibles = Transportadora.getTransportadoras();
		generadorDeTablas.mostrarTablaDeViajesDisponiblesPorTransportadoras(transportadorasDisponibles);
	}

	static void generarTiquete() {
		System.out.println("Quieres buscar un viaje por:");
		System.out.println("1. Destino");
		System.out.println("2. Destino y fecha");
		System.out.println("3. Regresar");
		int opcion = sc.nextInt();
		while (opcion != 1 & opcion != 2 & opcion != 3) {
			System.out.println("Por favor ingresa una opcion valida");
			opcion = sc.nextInt();
		}

		if (opcion == 1) {
			System.out.println("Por favor ingrese un destino:");
			String destino_1 = sc.next();
			boolean hayViajes = consultarViajesPorDestino(destino_1);
			if (!hayViajes) {
				return;
			}
		} else if (opcion == 2) {
			System.out.println("Por favor ingrese un destino");
			String destino_2 = sc.next();
			System.out.println("Por favor ingrese una fecha (dd-mm-aaaa):");
			String fecha_2 = sc.next();
			boolean hayViajes = consultarViajesPorDestinoYFecha(destino_2, fecha_2);
			if (!hayViajes) {
				return;
			}
		} else {
			return;
		}

		System.out.println("Por favor ingrese el nombre de la transportadora con la que desea viajar");
		String nombre_transportadora = sc.next();
		Transportadora transportadora = Transportadora.buscarTransportadoraPorNombre(nombre_transportadora); 

		while (transportadora == null) {
			System.out.println("Por favor ingrese un nombre valido");
			nombre_transportadora = sc.next();
			transportadora = Transportadora.buscarTransportadoraPorNombre(nombre_transportadora);
		}

		System.out.println("Por favor ingrese el ID del viaje que desea comprar");
		int ID = sc.nextInt();
		Viaje viaje = transportadora.buscarViajePorID(transportadora.getViajes(), ID); 
		while (viaje == null) {
			System.out.println("Por favor ingrese un ID valido");
			ID = sc.nextInt();
			viaje = transportadora.buscarViajePorID(transportadora.getViajes(), ID);
		}

		double ID_tiquete = 100 + Math.random() * 900; 
		while (Transportadora.BuscarTiquete((int) ID_tiquete) != null) {
			ID_tiquete = 100 + Math.random() * 900;
		}

		System.out.println("Que tipo de silla desea comprar?");
		Silla silla = elegirSilla(viaje);
		if (silla == null) {
			System.out.println("Lo sentimos no se encuentran sillas disponibles con esas caracteristicas\n");
			return;
		}
		Tiquete tiquete = new Tiquete((int) ID_tiquete, viaje.getPrecio(), viaje);
		tiquete.setSilla(silla);

		System.out.println("DATOS DEL PASAJERO:");
		System.out.println("Ingrese el nombre:");
		String nombre = sc.next();
		System.out.println("Ingrese su edad:");
		int edad = sc.nextInt();
		System.out.println("Ingrese el numero de su cedula:");
		String pasaporte = sc.next();
		System.out.println("Ingrese un e-mail");
		String correo = sc.next();

		Pasajero pasajero = new Pasajero(pasaporte, nombre, tiquete, edad, correo);
		tiquete.setPasajero(pasajero);

		tiquete.asignarPrecio();
		System.out.println(tiquete);

	}

	static void agregarHospedaje() {
		System.out.println("Deseas agregar un hospedaje a tu compra?");
		System.out.println("Por favor ingresa el ID del tiquete que se genero al comprar su viaje:");
		int tiqueteID = sc.nextInt();
		Tiquete tiquete_solicitado = Transportadora.BuscarTiquete(tiqueteID);
		
		if (tiquete_solicitado == null) { 
			System.out.println("Lo sentimos, no tenemos un tiquete identificado con ese ID");
			System.out.println();
		}else if(tiquete_solicitado.getHospedaje() != null) {
			System.out.println("El tiquete ya posee un hospedaje, si quiere cambiarlo hagalo desde la opcion 4.\n");
			return;
		} else { 
			String destino = tiquete_solicitado.getViaje().getDestino();
			boolean hayHospedajes = mostrarHospedajesPorUbicacion(destino);  
			if (!hayHospedajes) { 
				return;
			}
			System.out.println("Por favor ingresa el nombre del hospedaje que desea anadir a su compra:");
			String hospedaje = sc.next();
			Hospedaje hospedaje_solicitado = Hospedaje.buscarHospedajePorNombre(hospedaje);
			if (hospedaje_solicitado == null) { 
				System.out.println("Lo sentimos, no tenemos un hospedaje con ese nombre");
				System.out.println();
			}else if(!hospedaje_solicitado.getLocacion().equals(destino) ){ 
				System.out.println("Lo sentimos, no tenemos un hospedaje con ese nombre en esa locacion\n");
				return; }
			else { 
				System.out.println("Cuantos dias desea quedarse en el hospedaje?");
				int num_dias = sc.nextInt();
				tiquete_solicitado.setHospedaje(hospedaje_solicitado);
				tiquete_solicitado.asignarPrecio(num_dias);

				System.out.println("Perfecto! el hospedaje " + hospedaje_solicitado.getNombre()
						+ " se ha agregado correctamente a su tiquete de compra.");
				System.out.println();
				System.out.println(tiquete_solicitado);
			}
		}
	}
	
	static void modificarTiquete() {
		System.out.println("Ingrese el ID del tiquete que desea modificar.");
		int ID = sc.nextInt();
		Tiquete tiquete = Transportadora.BuscarTiquete(ID);
		if (tiquete == null) {
			System.out.println("El ID ingresado no se encuentra\n");
		} else {
			System.out.println("Que aspectos de su tiquete desea modificar?");
			System.out.println("1: Modificar hospedaje");
			System.out.println("2: Modificar Silla");

			int opcion = sc.nextInt();
			switch (opcion) {
				case 1:
					int dias = modificarHospedaje(tiquete);
					if (dias > 0) {
						tiquete.asignarPrecio(dias);
						System.out.println(tiquete);
					}
					break;
				case 2:
					modificarSilla(tiquete);
			}
		}
	}


	private static void modificarSilla(Tiquete tiquete) {

		System.out.println("A que tipo de silla desea cambiar?");
		Silla silla = elegirSilla(tiquete.getViaje());
		if (silla == null) {
			System.out.println("Lo sentimos no se encuentran sillas disponibles con esas caracteristicas\n");
			return;
		}
		tiquete.getSilla().setEstado(true);
		tiquete.setSilla(silla);

		System.out.println("*************************************");
		System.out.println("SU SILLA HA SIDO MODIFICADA CON EXITO");
		System.out.println("*************************************\n");
		tiquete.asignarPrecio();
		System.out.println(tiquete);

	}

	private static int modificarHospedaje(Tiquete tiquete_solicitado) {
		if (tiquete_solicitado.getHospedaje() == null) {
			System.out.println("Aun no tiene un hospedaje asociado a su tiquete, puede agregar uno en la opcion 3.");
			System.out.println();
			return 0;
		}
		String destino = tiquete_solicitado.getViaje().getDestino();
		mostrarHospedajesPorUbicacion(destino);
		System.out.println("Por favor ingresa el nombre del hospedaje al que desea cambiar");
		String hospedaje = sc.next();
		Hospedaje hospedaje_solicitado = Hospedaje.buscarHospedajePorNombre(hospedaje);
		if (hospedaje_solicitado == null) {
			System.out.println("Lo sentimos, no tenemos un hospedaje con ese nombre\n");
			return -1;
		}else if(!hospedaje_solicitado.getLocacion().equals(destino) ){
			System.out.println("Lo sentimos, no tenemos un hospedaje con ese nombre en esa locacion\n");
			return -1;
			
		}else {
			System.out.println("Por favor ingrese el numero de dias que se va a quedar en el hospedaje");
			int dias = sc.nextInt();
			tiquete_solicitado.setHospedaje(hospedaje_solicitado);
			System.out.println("Perfecto! su hospedaje ha sido modificado a " + hospedaje_solicitado.getNombre()
					+ " exitosamente.");
			System.out.println();
			return dias;
		}
	}

	static void opcionesAdministrador() {

		int opcion;
		do {

			System.out.println("Que opcion desea realizar como administrador?");
			System.out.println("1. Listar Pasajeros.");
			System.out.println("2. Agregar Viaje.");
			System.out.println("3. Cancelar viaje.");
			System.out.println("4. Retirar un bus.");
			System.out.println("5. Agregar hospedaje.");
			System.out.println("6. Eliminar hospedaje.");
			System.out.println("7. Salir del administrador.");
			System.out.println("Por favor escoja una opcion mostrada en pantalla: ");

			opcion = sc.nextInt();

			switch (opcion) {
				case 1:
					listarPasajeros();
					break;
				case 2:
					agregarNuevoViaje();
					break;
				case 3:
					cancelarViajes();
					break;
				case 4:
					retirarBus();
					break;
				case 5:
					nuevoHospedaje();
					break;
				case 6:
					retirarHospedaje();
					break;
				case 7:
					salirDelAdministrador();
					break;
			}
		} while (opcion != 7);
	}

	private static void listarPasajeros() {
		ArrayList<Transportadora> transportadoras = Transportadora.getTransportadoras();
		generadorDeTablas.mostrarTablaDeViajesPorTransportadoras(transportadoras);

		System.out.println("Ingrese el ID del viaje: ");
		int IDBusqueda = sc.nextInt();

		ArrayList<Tiquete> tiquetes = new ArrayList<Tiquete>();
		Viaje viaje = null;
		for (Transportadora i : transportadoras) {
			if (i.buscarViajePorID(i.getViajes(), IDBusqueda) != null) {
				viaje = i.buscarViajePorID(i.getViajes(), IDBusqueda);
				break;
			}
		}
		if (viaje == null) {
			System.out.println("No tenemos viajes con ese ID.\n");
			return;
		}
		tiquetes = viaje.getTiquetes();
		System.out.println("LISTA DE PASAJEROS PARA EL VIAJE " + IDBusqueda);

		if (tiquetes.size() == 0) {
			System.out.println("El viaje aun no tiene pasajeros asociados \n");
		} else {
			generadorDeTablas.mostrarTablaDePasajeros(tiquetes);
		}
	}


	private static void agregarNuevoViaje() {
		ArrayList<Transportadora> transportadoras = Transportadora.getTransportadoras();
		System.out.println("AGREGAR NUEVO VIAJE \n");
		generadorDeTablas.mostrarTablaDeTransportadoras(transportadoras);
		System.out.println("Ingrese el nombre de la transportadora para agregar viaje\n");
		String nombreTransportadora = sc.next();

		ArrayList<String> list = new ArrayList<>();
		for (Transportadora i : transportadoras) {
			list.add(i.getNombre());
		}
		boolean existe = list.contains(nombreTransportadora);

		while (existe == false) {
			System.out.println("\nESA TRANSPORTADORA NO EXISTE");
			System.out.println("Ingrese un nombre del listado anterior\n");
			String nombreTransportadorax = sc.next();
			existe = list.contains(nombreTransportadorax);
		}
		System.out.println();

		System.out.println("Ingrese el ID del nuevo viaje (3 cifras):");
		int iD = sc.nextInt();
		Transportadora transportadora_busqueda = Transportadora.buscarTransportadoraPorNombre(nombreTransportadora);
		while (Integer.toString(iD).length() != 3) {
			System.out.println("Por favor ingrese un ID de 3 cifras.");
			iD = sc.nextInt();
		}
		while (transportadora_busqueda.buscarViajePorID(transportadora_busqueda.getViajes(), iD) != null) {
			System.out.println("El ID que ingreso ya esta en uso, por favor ingrese uno distinto.");
			iD = sc.nextInt();
		}

		System.out.println("\nIngrese el precio:");
		int precio = sc.nextInt();
		System.out.println();

		System.out.println("Ingrese el origen:");
		String origen = sc.next();
		System.out.println();

		System.out.println("Ingrese el destino:");
		String destino = sc.next();
		System.out.println();

		System.out.println("Ingrese la distancia (KM):");
		double distancia = sc.nextDouble();
		System.out.println();

		System.out.println("Ingrese fecha de salida (DD-MM-AAAA):");
		String fechaSalida = sc.next();
		System.out.println();

		System.out.println("Ingrese hora de salida (24:00):");
		String horaSalida = sc.next();
		System.out.println();

		System.out.println("Que tipo de vehiculo es?");
		System.out.println("Ingrese 1 para bus" + "\n" + "Ingrese 2 para buseta");
		int terrestre = sc.nextInt();

		if (terrestre == 1) {
			System.out.println("Ingrese el nombre del bus:");
			String nombreBus = sc.next();
			System.out.println();

			Bus bus = new Bus(nombreBus, Transportadora.buscarTransportadoraPorNombre(nombreTransportadora));
			Viaje viaje = new Viaje(iD, precio, origen, destino, bus, distancia, fechaSalida, horaSalida);
			System.out.println("");
			System.out.println("SU VIAJE SE HA REGISTRADO CORRECTAMENTE");
			System.out.println("\n");

		} else if (terrestre == 2) {
			System.out.println("INGRESE EL NOMBRE DE LA BUSETA:");
			String nombreBuseta = sc.next();
			System.out.println();
			Buseta buseta = new Buseta(nombreBuseta, Transportadora.buscarTransportadoraPorNombre(nombreTransportadora));
			Viaje viaje= new Viaje(iD, precio, origen, destino, buseta, distancia, fechaSalida, horaSalida);
			System.out.println("***************************************");
			System.out.println("SU VIAJE SE HA REGISTRADO CORRECTAMENTE");
			System.out.println("***************************************\n");
		} else {
			System.out.println("No manejamos ese tipo de vehiculo");
		}
	}

	public static void cancelarViajes() {
		System.out.println("Estos son los viajes que tenemos:\n");
		ArrayList<Transportadora> transportadoras = Transportadora.getTransportadoras();
		generadorDeTablas.mostrarTablaDeViajesPorTransportadoras(transportadoras);
		System.out.println("Ingrese el ID del viaje a eliminar:");
		int id = sc.nextInt();

		for (Transportadora transportadora : transportadoras) {
			for (int i = 0; i < transportadora.getViajes().size(); i++) {
				if (transportadora.buscarViajePorID(transportadora.getViajes(), id) != null) {
					transportadora.cancelarViaje(id);
					System.out.println("El viaje se ha eliminado correctamente.");
					return;
				}
			}
		}
		System.out.println("No tenemos un viaje identificado con ese ID \n");
	}

	public static void retirarBus() {
		boolean terrestre_encontrada = false;
		System.out.println("Ingrese el nombre del Vehiculo que se desea retirar:");
		String nombre_terrestre = sc.next();
		ArrayList<Transportadora> transportadorasDisponibles = Transportadora.getTransportadoras();
		for (int i = 0; i < transportadorasDisponibles.size(); i++) {
			Transportadora transportadora = transportadorasDisponibles.get(i);
			Viaje viaje = transportadora.buscarViajePorTerrestre(transportadora.getViajes(), nombre_terrestre);
			if (viaje != null) {
				viaje.getTerrestre().setDescompuesto(true);
				transportadora.cancelarViaje(viaje.getID());
				System.out.println("Se ha retirado el vehiculo descompuesto y el viaje que tenia este.");
				System.out.println();
				terrestre_encontrada = true;
				break;
			}
		}
		if (!terrestre_encontrada) {
			System.out.println("Lo sentimos, no encontramos un vehiculo asociado al nombre que ingreso.");
			System.out.println();
		}
	}

	public static void nuevoHospedaje()
	{
		System.out.println("Ingrese el nombre del hospedaje que desea agregar a nuestra lista:");
		String nombre = sc.next();
		System.out.println();
		
		System.out.println("Ingrese la locacion:");
		String locacion = sc.next();
		System.out.println();
		
		System.out.println("Ingrese el precio por dia:");
		long precio = sc.nextLong();
		System.out.println();
		
		System.out.println("Ingrese el numero de estrellas (1-5):");
		int estrellas = sc.nextInt();
		System.out.println();
		
		Hospedaje nuevoHospedaje = new Hospedaje(nombre, locacion, precio, estrellas);
		System.out.println("Perfecto! El hospedaje " + nuevoHospedaje.getNombre() + " se ha agregado a nuestra lista.");
		
	}
	
	public static void retirarHospedaje()
	{
		System.out.println("Estos son los hospedajes que tenemos asociados:");
		generadorDeTablas.mostrarTablaDeHospedajes(Hospedaje.getHospedajes());
	
		System.out.println("Ingrese el nombre del hospedaje que desea retirar de nuestra lista:");
		String nombre = sc.next();
		
		if (Hospedaje.buscarHospedajePorNombre(nombre) != null)
		{
			for (int i = 0; i < Hospedaje.getHospedajes().size(); i++ )
			{
				if (Hospedaje.getHospedajes().get(i).getNombre().equalsIgnoreCase(nombre))
				{
					Hospedaje.getHospedajes().remove(i);
					System.out.println("El hospedaje " + nombre + " se ha eliminado correctamente.");
					System.out.println();
				}
			}	
		}
		else
		{
			System.out.println("Lo sentimos, no tenemos un hospedaje con este nombre.");
			System.out.println();
		}
	}
	
	private static void salirDelAdministrador() {
		System.out.println("Gracias por usar nuestras opciones de administrador! \n");
	}
	
	private static void salirDelSistema() {
		System.out.println("Gracias por usar nuestro servicio!");
		System.exit(0);
	}
	
	static boolean consultarViajesPorDestino(String destino) 
	{
		System.out.println("Estos son los viajes disponibles hacia " + destino + " por nuestras transportadoras:" );
		System.out.println();
		boolean hayViajes = false;
		
		ArrayList<Transportadora> transportadorasDisponibles = Transportadora.getTransportadoras();
		for (int i = 0; i < transportadorasDisponibles.size(); i++)
		{
			Transportadora transportadora = transportadorasDisponibles.get(i);
			ArrayList<Viaje> viajesPorDestino = transportadora.buscarViajePorDestino(transportadora.viajesDisponibles(transportadora.getViajes()), destino);
			if (viajesPorDestino.size() != 0)
			{
				generadorDeTablas.mostrarTablaDeViajes(transportadora, viajesPorDestino);
				hayViajes = true;	
			}
		}
		if (hayViajes == false) 
		{
		System.out.println("Lo sentimos, no tenemos viajes disponibles para ese destino");
		System.out.println();
		}
		return hayViajes;
	}
	
	
	static boolean consultarViajesPorDestinoYFecha(String destino, String fecha) 
	{
		System.out.println();
		System.out.println("Estos son los viajes disponibles hacia " + destino + " en la fecha " + fecha + " por nuestras transportadoras:" );
		System.out.println();
		boolean hayViajes = false;
		
		ArrayList<Transportadora> transportadorasDisponibles = Transportadora.getTransportadoras();
		for (int i = 0; i < transportadorasDisponibles.size(); i++)
		{
			Transportadora transportadora = transportadorasDisponibles.get(i);
			ArrayList<Viaje> viajesPorDestino = transportadora.buscarViajePorDestino(transportadora.viajesDisponibles(transportadora.getViajes()), destino);
			if (viajesPorDestino.size() != 0)
			{
				ArrayList<Viaje> viajesPorFecha = transportadora.buscarViajePorFecha(viajesPorDestino, fecha);
				if(viajesPorFecha.size() != 0 ){
					generadorDeTablas.mostrarTablaDeViajes(transportadora, viajesPorFecha);
					hayViajes = true;
				}
			}
		}
		if (hayViajes == false) {
			System.out.println("Lo sentimos, no tenemos viajes disponibles para ese destino y fecha especificos");
			System.out.println();
		}
		return hayViajes;
	}
	
	static boolean mostrarHospedajesPorUbicacion(String ubicacion) 
	{
		System.out.println("Estos son los hospedajes disponibles en " + ubicacion + ":" );
		boolean hayHospedajes = false;
		ArrayList<Hospedaje> hospedajesDisponibles = Hospedaje.buscarHospedajePorUbicacion(ubicacion);
		if (hospedajesDisponibles.size() != 0) {
			hayHospedajes = true;
			generadorDeTablas.mostrarTablaDeHospedajes(hospedajesDisponibles);		
		}else {
			System.out.println("Lo sentimos, no tenemos hospedajes disponibles para ese destino");
			System.out.println();
		}
		return hayHospedajes;
	}
	
		static Silla elegirSilla(Viaje viaje) 
		{
			System.out.println("1: Con sobrecarga");
			System.out.println("2: Sin carga");
			
			int nombre_clase = sc.nextInt();
			int num_ubicacion;
			String clase;
			while(nombre_clase != 1 & nombre_clase!=2) {
				System.out.println("Por favor ingrese una opcion valida");
				nombre_clase = sc.nextInt();
			}
			
			System.out.println("Cual de las siguientes capacidades prefiere?");
			System.out.println("1: +200 kg");
			System.out.println("2: -100 kg");
			
			if(nombre_clase == 2)  {
				clase = "ECONOMICA";
				num_ubicacion  = sc.nextInt();
				while(num_ubicacion!=1 & num_ubicacion!=2 & num_ubicacion!=3) {
					System.out.println("Por favor ingrese una opcion valida");
					num_ubicacion = sc.nextInt();
				}
			}
			else {clase = "EJECUTIVA";
				num_ubicacion  = sc.nextInt();
				while(num_ubicacion!=1 & num_ubicacion!=2) {
					System.out.println("Porfavor ingrese una opcion valida");
					num_ubicacion = sc.nextInt();
				}
			}

			Ubicacion ubicacion;
			if(num_ubicacion == 1) {
				ubicacion = Ubicacion.PASILLO;
			}
			else if (num_ubicacion == 2) {
				ubicacion = Ubicacion.VENTANA;
			}
			else {ubicacion = Ubicacion.CENTRAL;
			}
			
			return viaje.getTerrestre().buscarSillaPorUbicacionyTipo(ubicacion,clase );
		}

}