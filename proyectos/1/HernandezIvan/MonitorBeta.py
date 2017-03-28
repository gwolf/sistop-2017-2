#Primer proyecto basado en monitoreo de procesos mediante multihilos

#En este archivo se intentara hacer uso de multiilos cuando se manden a llamar a ciertos comandos


#acquire() => adquirir || release() => soltar

import threading
import time
import os

semaforo = threading.Semaphore(1)
thr = 0


def SISTEMA():
  """Esta función sirve para ver el tipo de 
  sistema en el que se está, arquitectura, kernel y hardware """	
  global semaforo
  semaforo.acquire()
  print("********Información del sistema********\n")
  os.system("arch") #Mostrar arquitectura de la maquina
  os.system("uname -r") #Mostrar la version del kernel usado
  os.system("dmidecode -q") #Mostrar el hardware del sistema
  semaforo.release()

def HDD():
  """Para ver archivos que hay en el sistema"""
  global semaforo
  semaforo.acquire()
  print("********HDD********\n")
  os.system("du -h") #Descubre archivos mas grandes del sistema
  #os.system("tree") #Mostrar los ficheros y carpetas en forma de arbol comenzando por la raiz.NO lo consegui hacer funcionar o parece que en mi maquina no funciono xD
  semaforo.release()
  
def MEMORIA():
  global semaforo
  semaforo.acquire()
  print("********Memoria********\n")
  os.system("free") #Se visualiza la cantidad total de memoria libre, la memoria fisica utilizada y el intercambio en el sistema
  os.system("cat /proc/meminfo") #Verificar el uso de memoria
  semaforo.release()

def PROCESOS():
  global semaforo
  semaforo.acquire()
  print("********Procesos********\n")
  os.system("ps") #Muestra una instantanea de los procesos actuales
  os.system("pstree") #Muestra procesos actuales en forma de arbol
  semaforo.release()
  
def CPU():
  global semaforo
  semaforo.acquire()
  print("/////CPU/////\n")
  os.system("cat /proc/cpuinfo") #Mostar informacion del CPU
  semaforo.release()

def CLEAR():
  global semaforo
  semaforo.acquire()
  os.system("clear")
  semaforo.release()


def COMMAND(opcion):
  #Lanzador de hilos, muzak= hilo musical en frances
  global hilo
  if (opcion == "sistema"):
    muzak = threading.Thread(target = SISTEMA)
    muzak.start()
  elif (opcion == "disco"):
    muzak = threading.Thread(target = HDD)
    muzak.start()
  elif (opcion == "memoria"):
    muzak = threading.Thread(target = MEMORIA)
    muzak.start()
  elif (opcion == "procesos"):
    muzak = threading.Thread(target = PROCESOS)
    muzak.start()
  elif (opcion == "cpu"):
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
  while thr == 0:
      time.sleep(.5)
      print("********Escriba la opción que quiere ver********\n")
      print("-sistema\n-disco\n-memoria\n-procesos\n-cpu\n-limpiar\n-help\n-exit")
      opcion = input("wifislax@sudo$ ")
      COMMAND(opcion)
  semaforo.release()

MONITOR()
