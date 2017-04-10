# *-* encoding: utf-8 *-*
import threading
import time
import commands
import os

semaforo = threading.Semaphore(0) #Uso de Semaforo para señalizar

def verSistema():
	os.system("clear")
	ver = commands.getoutput('cat /proc/version') #Se guarda la cadena de version en 'var' 
	print ver #Impresión de 'ver' para mostrar la version del sistema 
	print "\n\n\nPresione ctrl+c para regresar al menu\n"
	time.sleep(20)
	semaforo.release() #Libera al hilo opcion para regresar al hilo menu
	return 0


def datosMem():
	os.system("clear")
	aux = 0
        #Las siguientes 5 lineas almacenan los estados de memoria (total, libre, disponible, swap total y swap libre)
	mTotal=commands.getoutput('cat /proc/meminfo|grep "MemTotal:"|tr -s "'" "'"|cut -d "'" "'" -f 2')
	mLibre=commands.getoutput('cat /proc/meminfo|grep "MemFree:"|tr -s "'" "'"|cut -d "'" "'" -f 2')
	mDisp=commands.getoutput('cat /proc/meminfo|grep "MemAvailable:"|tr -s "'" "'"|cut -d "'" "'" -f 2')		
	sTotal=commands.getoutput('cat /proc/meminfo|grep "SwapTotal:"|tr -s "'" "'"|cut -d "'" "'" -f 2')
	sLibre=commands.getoutput('cat /proc/meminfo|grep "SwapFree:"|tr -s "'" "'"|cut -d "'" "'" -f 2')
	#En las siguientes 5 lineas se convierten mTotal (memoria total) y mLibre (memoria libre) en Enteros, para obtener mOcu (memoria ocupada)
	aux = int(mTotal)
	mTotal = str(aux)
	aux = int(mLibre)
	mLibre = str(aux)
	mOcu = str(int(mTotal) - int(mLibre))
	#Se imprimen las estadisticas de memoria en kiloBytes 'kB'
	print "\nEstadisticas de Memoria\n\n" 
	print "Memoria Total:         " + mTotal + " kB \n"
	print "Memoria Libre:         " + mLibre + " kB \n"
	print "Memoria Disponible:    " + mDisp + " kB\n"		
	print "Memoria Ocupada:       " + mOcu + " kB \n"
	print "Swap Total:            " + sTotal + " kB \n"
	print "Swap Libre:            " + sLibre + " kB \n"
	print "\n\n\nPresione ctrl+c para regresar al menu\n"
	time.sleep(20)
	semaforo.release() #Libera al hilo opcion para regresar al hilo menu
	return 0


def verProcesador():
	os.system("clear")
	#En las siguientes 4 lineas se almacena informacion del procesador
	modelo = commands.getoutput("cat /proc/cpuinfo | grep \"model name\"")
	numNucleos = commands.getoutput("cat /proc/cpuinfo | grep \"cpu cores\"")
	tamCache = commands.getoutput("cat /proc/cpuinfo | grep \"cache size\"")
	dirEspacio = commands.getoutput("cat /proc/cpuinfo | grep \"address sizes\"")
	#En las siguientes 4 lineas se imprime la informacion almacenada del cpu
	print "El modelo de procesador es:\n\n" + modelo + "\n"
	print "El numero de nucleos es:\n\n" + numNucleos + "\n"
	print "La cantidad de cache es:\n\n" + tamCache + "\n"
	print "Los espacios de direccionamiento son:\n\n" + dirEspacio + "\n"
	print "\n\n\nPresione ctrl+c para regresar al menu\n"
	time.sleep(20)
	semaforo.release()
	return 0

#Menu de las opciones disponibles a ver.
def Menu():	
	global semaforo
	opcion = '0'
	while opcion != '4':
		os.system("clear")
		opciones = {'1':verSistema,'2':datosMem,'3':verProcesador}
		print "\t---------------------------------------------------------"
		print "\t|	Universidad Nacional Autonoma de México		|"
		print "\t|		Facultad de Ingenieria			|"
		print "\t|	      Ingenieria en Computación			|"	
		print "\t|		 Sistemas Operativos			|"
		print "\t|	    Arizmendi Barriga Jose Antonio		|"
		print "\t|	    Proyecto 1: Monitor de Sistema		|"
		print "\t---------------------------------------------------------"
		print "Elija la opcion de acuerdo a la información que desee obtener. \n\n"
		print "1.- Versión del sistema.\n"
		print "2.- Estadisticas de la memoria.\n"
		print "3.- Modelo y caracteristicas del procesador.\n"
		print "4.- Salir.\n"
		print "\n\nDespues de 20 segundos de mostrar la opcion, el sistema regresa automaticamente al menu\n"
		opcion = raw_input('\nSelecciona una opción: \n')		
		try:
			resultado = opciones[opcion]()
			semaforo.acquire() #Espera el hilo menu, mientras se ejecutan los hilos opciones
		except:
			if opcion != '4':
				print("Opción invalida")
Menu()
