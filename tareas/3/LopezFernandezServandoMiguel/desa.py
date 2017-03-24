#!/usr/bin/python3 
from time import sleep
from random import randrange
from threading import Semaphore, Thread

class Colas:

	def __init__(self):
		self.colas = [[],[]]
		self.trabajando_con_cola= Semaphore(1)
		#self.sem_c = Semaphore(0)

	def tamanio_de(self, en):
		self.trabajando_con_cola.acquire()
		sz = len(self.colas[en])
		self.trabajando_con_cola.release()
		return sz 

	def encolar_en(self, a_quien):
		self.trabajando_con_cola.acquire()
		if a_quien.que_desarrollas == 'Linux':
			self.colas[0].append(a_quien)
		else:
			self.colas[1].append(a_quien)
		#self.trabajando_con_cola.release()
		self.sem_c.acquire()

	def sale(self, de_cual):
		self.trabajando_con_cola.acquire()
		quien= self.colas[de_cual].pop(0)
		self.trabajando_con_cola.release()
		#self.sem_c.release()
		return quien

class Balsa:

	cupo_maximo = 4
	contador = 0
	barrera = Semaphore(0)
	def __init__(self):
		self.hay_arriba = []
		self.no_te_muevas = Semaphore(1)
		self.colas = Colas()
		
		Thread(target=self.ingresan, args=[]).start()


	def cruza(self):
		for e in range(randrange(0,3)):
			print('\nCruzando!')
			sleep(1)

		print('\nArribo')
		self.bajan()

	def regresando(self):
		print('\nRegreso')

	def ingresan(self):
                while True:
                        self.no_te_muevas.acquire()
                        print('\nEsperando tripulantes.....')
                        while True:
                                
                                en = randrange(0,2)
                                if self.colas.tamanio_de(0) >= 2 and self.colas.tamanio_de(1) >= 2:
                                		for e in range(2):
                                			for i in range(2):
                                				self.hay_arriba.append(self.colas.sale(i))
                                		break
                                		#print('ENTRO A IF =>2 ')
                                
                                elif self.colas.tamanio_de(en) >= 4:
                                        for e in range(4):
                                                self.hay_arriba.append(self.colas.sale(en))
                                        #print('ENTRO A ELFI')
                                        break
                                sleep(1)

                        self.no_te_muevas.release()
                        self.cruza()

	def bajan(self):
		self.no_te_muevas.acquire()
		while len(self.hay_arriba) > 0:
			print('Bajo : {}   , '.format( self.hay_arriba.pop()), end='')
		self.no_te_muevas.release()

		self.regresando()

class Desarrolladores:

	nombres = ['Octavio Alatorre', 'Antonio Arizmendi', 'Emilio Cabrera',
           'Isaac Cruz', 'Fernando de la Torre', 'Jaziel Fuentes',
           'Iñaki Hernandez', 'Ivan Hernandez', 'Ricardo Hernandez',
           'Servando Lopez', 'Alberto Negrete', 'Omar Orozco', 'Diego Pacheco',
           'Jesus Pacheco', 'Afferny Ramirez', 'Eduardo Ramirez',
           'Alejandro Rivera', 'Baruch Rivera', 'Julio Rodriguez',
			'Antonio Schwuchow', 'Eduardo Stevens', 'Armando Valadez']
	so = ['Linux', 'Windows']

	def __init__(self, balsa):
		self.nombre = ''
		self.que_desarrollas = ''
		self.balsa = balsa

		self.balsa.colas.encolar_en(self.yo_soy())

		print('Nombre : {}  desarrollo en {}'.format(self.nombre, self.que_desarrollas))

	def __str__(self):
		return 'Nombre : {}  desarrollo en {}'.format(self.nombre, self.que_desarrollas)


	def yo_soy(self):
		self.nombre = Desarrolladores.nombres[randrange(0,len(Desarrolladores.nombres))]
		self.que_desarrollas = Desarrolladores.so[randrange(0,len(Desarrolladores.so))]
		return self

if __name__ == '__main__':
	b = Balsa()
	while True:
		Thread(target=Desarrolladores, args=[b]).start()
		sleep(1)

	input()
