
# *-* Encoding: utf-8
"""Script creado por:
    Isaac Cruz Santos
    Afferny Ramírez Canales

    Problema de cruce de rio usando primitivas de sincronización"""

from threading import Semaphore, Thread # Usamos threading para manejar hilos, Semaphore para usar mutex y colas.
from time import sleep #Usamos sleep para generar un retraso cada que la balza avance



numHackers = 0  #Contador usado para revisar el numero de hackers que abordan.
numSerfs = 0    #Contador usado para revisar el numero de serfs que abordan.
pasajeros = 0   #Contador usado para revisar el numero de pasajeros totales en la balsa.
filaHackers = Semaphore(0)  #Fila de Hackers.
filaSerfs = Semaphore(0)    #Fila de Serfs.
mutex = Semaphore(1)        #Mutex usado para proteger la lectura y escritura en las variables numHackers y numSerfs.
mutexBalsa = Semaphore(1)   #Mutex usado para proteger la escritura y lectura de la variable pasajeros.

##########
def hacker():             
    global numHackers
    global numSerfs
    mutex.acquire()
    numHackers+=1
    if numHackers==4:         #Si llega el cuarto hacker se sube y se liberan 3 lugares en la fila. la fila pasa de semaphore(-3) a semaphore(0)
        filaHackers.release() 
        filaHackers.release()
        filaHackers.release()
        numHackers-=4         #Reiniciamos el contador a cero
        mutex.release()       #Liberamos el Mutex
        aborda("Hacker")      #Abordamos
        
    elif (numHackers==2 and numSerfs==2): #Si llega el segundo hacker y ya hay 2 o mas serfs esperando, se libera un lugar en la fila de hackers y
        filaHackers.release()             # 2 en la de Serfs.
        filaSerfs.release()
        filaSerfs.release()
        numHackers-=2                     #Reiniciamos el contador de Hackers y Serfs 
        numSerfs-=2
        mutex.release()                   #Liberamos el mutex       
        aborda("Hacker")                  #Abordamos
    else:
        
        mutex.release()                   #Lputs 'Afferny hizo todo'iberamos el mutex
        filaHackers.acquire()             #Ocupamos un lugar en la fila
        aborda("Hacker")                  #Abordamos

################################# Esta funcion serf tiene la misma logica que la de hacker.
def serf():
    global numHackers
    global numSerfs
    mutex.acquire()
    numSerfs+=1
    
    if numSerfs==4:
        filaSerfs.release()
        filaSerfs.release()
        filaSerfs.release()

        numSerfs-=4
        mutex.release()
        aborda("Serf")
    elif (numHackers==2 and numSerfs==2):
        filaHackers.release()
        filaHackers.release()
        filaSerfs.release()
        numHackers-=2
        numSerfs-=2
        mutex.release()
        aborda("Serf")
    else:
        mutex.release()
        filaSerfs.acquire()
        aborda("Serf")

############### Función que representa la forma de abordar toma como argumento "soy"
############### que nos indica quien abordo,aumenta en uno el numero de pasajeros hasta llegar a 4 y entonces avanza
############### usamos un mutex para proteger la variable pasajeros

def aborda(soy):
    global pasajeros
    mutexBalsa.acquire()
    pasajeros+=1
    print("Soy un "+soy+" y estoy abordo")
    if pasajeros==4:
        avanzar()
        pasajeros=0

    mutexBalsa.release()
##############################################################################3
def avanzar():
    print("--Vamonos que aqui espantan!--")
    sleep(1)

for i in range(16):
    Thread(target = hacker, args = []).start()
    Thread(target = hacker, args = []).start()
    Thread(target = serf, args = []).start()
    

    