#modulos
import curses
import psutil
import threading
import time
import platform

#varables
global num_hlos
global contador
global mutex
global barrera
#Varables para crear barrera y sncronzar los hlos
num_hlos = 4
contador = 0
mutex = threading.Semaphore(1)
barrera= threading.Semaphore(0)

#funcion que convierte los bytes en una cadena mas legible para el usuario
def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

#funcion que obtiene la informacion de los ultmos procesos en ejecucon
def procs(size):
	lstproc = psutil.pids()
	lstproc.reverse() 
	for x in xrange(0,size):

		myscreen.addstr(10+x, 2,"%d "%lstproc[x])
		myscreen.addstr(10+x, 8,psutil.Process(lstproc[x]).name())
		myscreen.addstr(10+x, 22,psutil.Process(lstproc[x]).status())
		myscreen.addstr(10+x, 35,"%d "%psutil.Process(lstproc[x]).num_threads())
		myscreen.addstr(10+x, 43,psutil.Process(lstproc[x]).username())
		myscreen.addstr(10+x, 53,"%.2f"%psutil.Process(lstproc[x]).cpu_percent(interval=0))
		myscreen.addstr(10+x, 63,sizeof_fmt(psutil.Process(lstproc[x]).memory_info().rss))
	sync()

#funcion para la inicalizacion de la barrera
def sync():
	global contador
	mutex.acquire()
	contador=contador+1
	mutex.release()

	if contador == num_hlos:
		barrera.release()
	barrera.acquire()
	barrera.release()

#funcion que dibuja las barras de porcentaje
def percentBar(source,y):
	size = 50
	percent = int(round(source/2))
	for i in range(0,percent):
		myscreen.addstr(y,i+18," ",curses.A_STANDOUT)
	myscreen.addstr(y,18+size,"| %d %%"%source)
	
	myscreen.refresh()
	
	sync()

#funcion que obtiene la memoria usada y disponible
def mem_usage():
	myscreen.addstr(7,45,sizeof_fmt(psutil.virtual_memory().available))
	myscreen.addstr(7,71,sizeof_fmt(psutil.virtual_memory().used))
	
	sync()

#funcion que inicia los hilos de las funciones que se estaran actualizando
def hilos():
	threading.Thread(target=mem_usage, args=[]).start()
	threading.Thread(target=procs, args=[13]).start()
	threading.Thread(target=percentBar, args=[psutil.cpu_percent(interval=1),2]).start()
	threading.Thread(target=percentBar, args=[psutil.virtual_memory().percent,4]).start()
	
#Funcion que dibuja toda la interfaz
def gui(args):
	global myscreen
	global contador
	global num_hlos
	
	
	
	while True:	

		myscreen = curses.initscr()
		
		myscreen.border(0)
		myscreen.addstr(0, 0, "Monitor de Procesos",curses.A_BOLD)
		myscreen.addstr(2, 1, "Uso de CPU:",curses.A_UNDERLINE)
		myscreen.addstr(4, 1, "Uso de MEMORIA:",curses.A_UNDERLINE)
		myscreen.addstr(6, 28, platform.system())
		myscreen.addstr(6, 34, platform.processor())
		myscreen.addstr(6, 43,"%d Nucleos"%psutil.cpu_count())
		myscreen.addstr(7, 3,"Memoria Total: "+sizeof_fmt(psutil.virtual_memory().total))
		myscreen.addstr(7, 30,"Memoria Libre:")
		myscreen.addstr(7, 55,"Memoria en Uso:")
		
		for j in xrange(1,79):
			myscreen.addstr(9, j, " ",curses.A_REVERSE)
		
		myscreen.addstr(9, 2,"PID",curses.A_REVERSE)
		myscreen.addstr(9,8,"Nombre",curses.A_REVERSE)
		myscreen.addstr(9,23,"Estado",curses.A_REVERSE)
		myscreen.addstr(9,32,"Threads",curses.A_REVERSE)
		myscreen.addstr(9,42,"Usuario",curses.A_REVERSE)
		myscreen.addstr(9,53,"% CPU",curses.A_REVERSE)
		myscreen.addstr(9,63,"Memoria",curses.A_REVERSE)
		
		
		hilos()
		mutex.acquire()
		contador-=num_hlos
		mutex.release()
		
		myscreen.refresh()
		
		
		curses.endwin()

curses.wrapper(gui)

