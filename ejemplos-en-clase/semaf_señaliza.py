#!/usr/bin/python3
from threading import Semaphore, Thread
from time import sleep
from random import random

s = Semaphore(0)

def busca_torta():
    print("Bajando por una torta...")
    s.acquire()
    print("Pidiendo la torta")
    sleep(random())
    print("Ya tengo la torta. Vamos para arriba!")

def pide_cable():
    print("Bajando por el cable")
    if hay_cable():
        s.release()
        print("Subiendo de vuelta a clase con el cable")
    else:
        print("Profeeee... No hay cables :-(")

def hay_cable():
    if random > 0.7:
        return True
    else:
        return False

Thread(target=busca_torta, args=[]).start()
Thread(target=pide_cable, args=[]).start()
