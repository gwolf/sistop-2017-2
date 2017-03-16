#!/usr/bin/python3
# *-* Encoding: utf-8
from threading import Semaphore, Thread
from random import random
from time import sleep

mult = Semaphore(3)
mutex = Semaphore(1)
lista = []

def Juega(quien):
    sleep(random())
    print("%d quiere entrar" % quien)
    mult.acquire()
    mutex.acquire()
    lista.append(quien)
    mutex.release()
    sleep(random())
    print("Estamos jugando: %s" % lista)
    mutex.acquire()
    lista.remove(quien)
    mutex.release()
    mult.release()

for i in range(30):
    Thread(target=Juega, args=[i]).start()
