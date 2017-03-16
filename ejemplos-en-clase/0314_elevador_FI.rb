#!/usr/bin/ruby
# coding: utf-8
require 'concurrent'
Pisos = 5
CupoMax = 5


class Cola
  def initialize
    @cola = []
    @cola_mut = Mutex.new
    @semaf_cola = Concurrent::Semaphore.new(0)
  end
  def hay_alguien?
    @cola_mut.lock
    res = @cola.empty?
    @cola_mut.unlock
    return ! res
  end
  def forma(alumno)
    @cola_mut.lock
    @cola.append alumno
    @cola_mut.unlock
    @semaf_cola.acquire
  end
  def sale()
    @cola_mut.lock
    alumno = @cola.pop
    @cola_mut.unlock
    @semaf_cola.release
    return alumno
  end
end

class Alumno
  def initialize(elevador)
    @inicio = rand(Pisos)
    @destino = rand(Pisos)
    @actual = @inicio
    puts "¡Hola! Ambiciono ir del piso %d al piso %d " % [@inicio, @destino]
    if @actual == @destino
      puts "¡Listo! Llegué a %d. ¡Gracias!" % @destino
      return true
    end

    @colas[@actual].forma
    elevador.aborda

    puts "Ya llegué!"
  end
end

class Elevador
  def initialize
    @min = 0
    @max = Pisos
    @piso_actual = 0
    @direccion = 0
    @cupo = CupoMax
    @mut_cupo = Mutex.new
    Thread.new{mueve}
  end

  def mueve
    while true
      anterior = @piso_actual
      if @direccion == 0
        if @piso_actual <= @min
          @direccion = 1
        else
          @piso_actual -= 1
        end
      else
        if @piso_actual >= @max
          @direccion = 0
        else
          @piso_actual += 1
        end
      end
      puts 'Dejé el piso %d, estoy en %d' % [anterior, @piso_actual]
      sleep 1

      puts "Me quedan %d lugares. Hay alguien? %s" % [@cupo, @colas[@piso_actual].hay_alguien? ? 'Sí' : 'No']
      while @colas[@piso_actual].hay_alguien? and @cupo >= 1
        puts "Sacando a alguien de la cola del piso %d" % @piso_actual
        @colas[@piso_actual].sale()
      end
    end
  end

  def aborda
    @mut_cupo.acquire
    @cupo -= 1
    @mut_cupo.release
  end
end

e = Elevador.new()
@colas = Pisos.times {Cola.new}
while true do
  Thread.new {Alumno.new(e)}
  sleep 1
end
