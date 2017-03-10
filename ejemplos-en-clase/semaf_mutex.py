#!/usr/bin/python3
# *-* Encoding: utf-8
from threading import Semaphore, Thread
from random import random
from time import sleep

s = Semaphore(1)
acum = 0

def Suma(cuanto):
    sleep(random())
    global acum
    s.acquire()
    print('Sumándole %d a %d' % (cuanto, acum))
    acum = acum + cuanto
    sleep(random())
    s.release()

for i in range(10):
    Thread(target=Suma, args=[i]).start()
