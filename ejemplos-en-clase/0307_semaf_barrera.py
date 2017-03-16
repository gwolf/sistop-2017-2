#!/usr/bin/python3
# *-* Encoding: utf-8
from threading import Semaphore, Thread
from random import random
from time import sleep

num_hilos = 5
cuenta = 0
mutex = Semaphore(1)
barrera = Semaphore(0)

def mitrabajo(id):
    global cuenta
    sleep(random())
    mutex.acquire()
    cuenta = cuenta + 1

    if cuenta == num_hilos:
        for i in range(num_hilos):
            barrera.release()
        cuenta = 0
    mutex.release()

    barrera.acquire()

    print("Ya pasé la barrera con %d hilos; soy %d" % (cuenta, id))


for i in range(10):
    Thread(target=mitrabajo,args=[i]).start()
