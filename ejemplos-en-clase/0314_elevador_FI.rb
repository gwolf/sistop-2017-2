#!/usr/bin/ruby
# coding: utf-8
require 'yaml'
require 'concurrent'
Pisos = 5
CupoMax = 5

# Hay que darle un sentido de realidad al planteamiento :-P
Nombres = ['Octavio Alatorre', 'Antonio Arizmendi', 'Emilio Cabrera',
           'Isaac Cruz', 'Fernando de la Torre', 'Jaziel Fuentes',
           'Iñaki Hernandez', 'Ivan Hernandez', 'Ricardo Hernandez',
           'Servando Lopez', 'Alberto Negrete', 'Omar Orozco', 'Diego Pacheco',
           'Jesus Pacheco', 'Afferny Ramirez', 'Eduardo Ramirez',
           'Alejandro Rivera', 'Baruch Rivera', 'Julio Rodriguez',
           'Antonio Schwuchow', 'Eduardo Stevens', 'Armando Valadez']

# La Cola "envuelve" el acceso a un arreglo, en el cual me puedo
# formar, y del cual puedo salir. Lo divertido de esta Cola es que
# #forma y #saca operan con un semáforo, y se invocan desde diferentes
# hilos: Cuando un hilo se forma, se duerme; cuando otro hilo saca a
# un elemento de la cola, lo despierta.
#
# Por comodidad y para imprimir mensajes más competos, le podemos
# preguntar su #tamaño o sencillamente si #hay_alguien formado.
class Cola
  def initialize
    @cola = []
    @cola_mut = Mutex.new
    @semaf_cola = Concurrent::Semaphore.new(0)
  end

  def hay_alguien?
    return tamaño != 0
  end

  def tamaño
    @cola_mut.lock
    res = @cola.size
    @cola_mut.unlock
    return res
  end

  def forma(alumno)
    @cola_mut.lock
    @cola.push alumno
    @cola_mut.unlock
    @semaf_cola.acquire
  end

  def saca
    @cola_mut.lock
    alumno = @cola.shift
    @cola_mut.unlock
    @semaf_cola.release
    return alumno
  end
end

# Cual debe ser, el Elevador es el que hace todo el trabajo en este
# cuento :-] Tras inicializarse, lanza un nuevo hilo con #mueve, que
# se encarga de subir y bajar (empleando a #_avanza) y a cada piso al
# que llega ve si hay que hacer algo — Primero deja bajar a quien
# quiera quedarse en este piso, con @pasajeros[@piso_actual].saca(), y
# luego hace subir a cuantos haya pendientes en la cola del piso, con
# @colas[@piso_actual].saca().
#
# Punto importante: Fue necesario hacer una señalización (mediante
# @abordando) entre el segundo while de #mueve y #aborda, porque si
# no, permitía sobrepasar el cupo :-O
#
# Todo lo demás es... Decoración :-]
class Elevador
  def initialize
    @min = 0
    @max = Pisos-1 # Recuerden... Trabajamos con índices base 0! :-P
    @piso_actual = 0
    @direccion = true
    @abordando = Concurrent::Semaphore.new(0)

    @pasajeros = {}
    @colas = []
    Pisos.times do |piso|
      @colas[piso] = Cola.new
      @pasajeros[piso] = Cola.new
    end

    Thread.new{mueve}
  end

  def _avanza
    if (@direccion and @piso_actual >= @max) or
      (! @direccion and @piso_actual <= @min)
      @direccion = !@direccion
    end
    if @direccion
      @piso_actual += 1
    else
      @piso_actual -= 1
    end
  end

  def mueve
    while true
      anterior = @piso_actual
      _avanza
      puts '%d→%d, %d pasajeros, caben %d' % [anterior, @piso_actual, num_pasajeros, cupo]

      while @pasajeros[@piso_actual].hay_alguien?
        @pasajeros[@piso_actual].saca()
      end

      while cupo >= 1 and @colas[@piso_actual].hay_alguien?
        @colas[@piso_actual].saca()
        @abordando.acquire
      end
      sleep 0.3
    end
  end

  def cupo
    CupoMax - num_pasajeros
  end

  def num_pasajeros
    @pasajeros.values.map {|v| v.tamaño}.reduce(:+)
  end

  def aborda(dest)
    @abordando.release
    @pasajeros[dest].forma(Thread.current)
  end

  def pide(piso)
    @colas[piso].forma(Thread.current)
  end

  def puts(msg)
    super 'E%s %s' % [(@direccion ? '↑' : '↓'), msg]
  end
end

# El alumno es el que la tiene más facilita de todos. Simplemente se
# para en la cola que le toca, con elevador.pide(@inicio), y se
# duerme. Después de un rato, lo despiertan, y se sube al elevador,
# con elevador.sube(@destino). Y por último, se va. No hay más que
# decir al respecto :)
class Alumno
  def initialize(elevador, nombre)
    @nombre = nombre
    @inicio = rand(Pisos)
    @destino = rand(Pisos)

    puts "¡Hola! ¿Dónde va la cola %d? " % @inicio
    if @inicio == @destino
      puts "¡Ups! Ya estaba en mi destino"
      return true
    end

    elevador.pide(@inicio)
    elevador.aborda(@destino)
    puts "¿Ya estamos en el %d? ¡Gracias!" % @destino
  end

  def puts(msg)
    super '* %20s (%d→%d): %s' % [@nombre, @inicio, @destino, msg]
  end
end

e = Elevador.new
while true do
  Thread.new {Alumno.new(e, Nombres.sample)}
  sleep 0.2
end

