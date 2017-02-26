#!/usr/bin/python3
from os import fork
from os import getpid
from os import execve

print("Hola, iniciando ejecución")
resultado = fork()

if (resultado == 0):
    # Proceso hijo
    print("... hijo blah blah PID %d" % getpid())
    print("Reemplacemos el espacio de memoria...")
    execve('/bin/ls', ('','-l',), {'': ''})
else:
    # Proceso padre
    print("Mi procesito %d ya camina!" % resultado)
    print("Ahora, a ver qué hay en el directorio...")

print("Y acá estamos de vuelta en la base")
