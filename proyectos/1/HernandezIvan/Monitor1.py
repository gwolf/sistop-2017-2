"""
Universidad Nacional Autónoma de México
Facultad de Ingenieria
Primer proyecto basado en monitoreo de procesos mediante multihilos
En este programa se intentara hacer uso de multiilos cuando se manden a llamar a ciertos comandos
por: Hernandez Garcia Ivan Alejandro para la clase de Sistemas operativos de GWOLF
"""
#acquire() => adquirir || release() => soltar
from colorama import init, Fore, Back, Style,Cursor
import threading
import time
import os
import platform
import random
from time import sleep
from datetime import date 
import locale
semaforo1 = threading.Semaphore(1)
semaforo = threading.Semaphore(1)
semaforo2 = threading.Semaphore(1)
thr = 0
init()
hoy = date.today()



def SISTEMA():
  """Esta función sirve para ver el tipo de 
  sistema en el que se está, arquitectura, kernel y hardware """	
  global semaforo
  os.system("clear")
  semaforo.acquire()
  print(Style.BRIGHT + Fore.RED + Back.BLACK + "********Información del sistema********\n") 
  print(Style.BRIGHT + Fore.RED + Back.BLACK) #Donde se vea este tipo de sintaxis es porque aqui es donde se modifica el texto en negritas o normal, color de letra y fondo de la misma usando el modulo de colorama
  os.system("arch") #Mostrar arquitectura de la maquina
  os.system("uname -r") #Mostrar la version del kernel usado
  #os.system("dmidecode -q") #Mostrar el hardware del sistema
  print("Su sistema es de ",platform.architecture())
  print("Tiene un procesador ", platform.processor())
  print("Esta trabajando en un sistema ", platform.system())
  semaforo.release()

def SISTEMA_INTERFAZ():
  print(Style.BRIGHT + Fore.RED + Back.BLACK)
  print("Obteniendo...")
  for arch in ["SO","Kernel","Procesador","Arquitectura"]: #pequeño truco para que se vea como más coqueto el programa
    numero = random.randrange(1,2)
    sleep(numero-.5)
    print(Cursor.UP(1)+Cursor.FORWARD(20) +str(arch))
  
def HDD():
  """Para ver archivos que hay en el sistema"""
  global semaforo
  os.system("clear")
  semaforo.acquire()
  print(Style.BRIGHT + Fore.YELLOW + Back.BLACK +"********HDD********\n")
  print(Style.NORMAL + Fore.YELLOW + Back.BLACK)
  os.system("du -h") #Descubre archivos mas grandes del sistema
  #os.system("tree") #Mostrar los ficheros y carpetas en forma de arbol comenzando por la raiz.NO lo consegui hacer funcionar o parece que en mi maquina no funciono xD
  semaforo.release()
  
def MEMORIA():
  global semaforo
  os.system("clear")
  semaforo.acquire()
  print(Style.BRIGHT + Fore.BLUE + Back.WHITE + "********Memoria********\n")
  print(Style.NORMAL + Fore.BLUE + Back.WHITE)
  os.system("free") #Se visualiza la cantidad total de memoria libre, la memoria fisica utilizada y el intercambio en el sistema
  print("\n")
  os.system("cat /proc/meminfo") #Verificar el uso de memoria
  semaforo.release()

def MEMORIA_INTERFAZ():
  print(Style.BRIGHT + Fore.BLUE + Back.WHITE)
  print("Obteniendo...")
  for arch in ["cat", "proc", "meminfo"]:
    numero = random.randrange(1,2)
    sleep(numero-.5)
    print(Cursor.UP(1)+Cursor.FORWARD(20) +str(arch))

def PROCESOS():
  global semaforo
  os.system("clear")
  semaforo.acquire()
  print(Style.BRIGHT + Fore.WHITE + Back.CYAN + "********Procesos********\n")
  print(Style.NORMAL + Fore.WHITE + Back.CYAN)
  os.system("ps") #Muestra una instantanea de los procesos actuales
  print(Style.BRIGHT + Fore.CYAN + Back.BLACK)
  os.system("pstree") #Muestra procesos actuales en forma de arbol
  semaforo.release()
  
  
  
def CPU():
  os.system("clear")
  global semaforo
  semaforo.acquire()
  print(Style.BRIGHT + Fore.GREEN + Back.BLACK+ "**************CPU**************\n")
  print(Style.NORMAL + Fore.GREEN + Back.BLACK)
  os.system("cat /proc/cpuinfo") #Mostar informacion del CPU
  semaforo.release()

def CPU_INTERFAZ():
  print(Style.BRIGHT + Fore.GREEN + Back.BLACK)
  print("Obteniendo...")
  for arch in ["MHz","ide","cores","model","Etcétera"]:
    sleep(.2)
    print(Cursor.UP(1)+Cursor.FORWARD(20) +str(arch))

def CLEAR():
  global semaforo
  semaforo.acquire()
  os.system("clear")
  semaforo.release()


def COMMAND(opcion):
  #Lanzador de hilos, muzak= hilo musical en frances
  global hilo
  if (opcion == "sistema"):
    SISTEMA_INTERFAZ()
    muzak = threading.Thread(target = SISTEMA)
    muzak.start()
  elif (opcion == "disco"):
    muzak = threading.Thread(target = HDD)
    muzak.start()
  elif (opcion == "memoria"):
    MEMORIA_INTERFAZ()
    muzak = threading.Thread(target = MEMORIA)
    muzak.start()
  elif (opcion == "procesos"):
    muzak = threading.Thread(target = PROCESOS)
    muzak.start()
  elif (opcion == "cpu"):
    CPU_INTERFAZ()
    muzak = threading.Thread(target = CPU)
    muzak.start()
  elif (opcion == "limpiar"):
    muzak = threading.Thread(target = CLEAR)
    muzak.start()
  elif (opcion == "help"):
    print("\n********Escriba la opción que quiera ejecutar********\n")
  elif (opcion == "exit"):
    print("ADIOS :V")
    thr = thr + 1
  else:
   print("Opcion invalida\n")





def MONITOR():
  global opcion, thr, semaforo
  os.system("clear")
  print("\033[4;36m"+ Back.BLACK +"\t**Universidad Nacional Autónoma de México**")
  print("\033[4;36m"+ Back.BLACK +"\t***********Facultad de Ingenieria**********\n\t"+ "*******Materia de Sistemas OPerativos******")
  print("\033[4;36m"+ Back.BLACK +"\t************Monitor del sistema************\n\t"+ "**Nombre: Hernández García Ivan Alejandro**"+ "\n\t**************Fecha: " + hoy.strftime("%m/%d/%y")+ "**************")
  print("\033[4;36m"+ Back.BLACK +"\t*******************************************")
  while thr == 0:
      print(Style.RESET_ALL)
      time.sleep(.5)
      print(Style.BRIGHT + Fore.GREEN + Back.BLUE + "\n\t********Escriba la opción que quiere ver********\n")
      print("\t-sistema\t-disco\n")
      print("\t-memoria\tcpu\n")
      print("\t-procesos\t-help\n")
      print("\t-limpiar\t-exit")
      print("\n")
      opcion = input("Comando@@: ")
      #print(Style.RESET_ALL)
      COMMAND(opcion)
  semaforo.release()

MONITOR()
