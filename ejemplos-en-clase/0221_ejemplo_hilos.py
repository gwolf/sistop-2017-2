#!/usr/bin/python3
from threading import *
from time import sleep
from random import random

a=1

def monitorea_vars():
    while True:
        print("a = %f" % a)
        sleep(1)

def modifica_vars():
    global a
    while True:
        mod = random() - 0.5
        a = a + mod
        sleep(1)

Thread(target=monitorea_vars, args=[]).start()
Thread(target=modifica_vars, args=[]).start()

while True:
    sleep(1)
