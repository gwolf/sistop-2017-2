import threading
import time
#esto esta bajo python 2, solo este codigo, todo lo demás esta en python 3
#Aqui lo unico que hice fue ir viendo como se implementaban los hilos en python
def trabajador():
  print threading.currentThread().getName(), 'Lanzado'
  print "Estoy trabajando :V  paapu" 
  time.sleep(2)
  print threading.currentThread().getName(), 'Deteniendo'
def servicio():
  print threading.currentThread().getName(), 'Lanzado :V'
  print threading.currentThread().getName(), 'Deteniendo :V'

t = threading.Thread(target=servicio, name='Servicio')
w = threading.Thread(target=trabajador, name='Trabajador')
z = threading.Thread(target=trabajador)
w.start()
z.start()
t.start()    