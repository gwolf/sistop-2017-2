#!/usr/bin/ruby
# coding: utf-8

class EjemploHilos
  require 'thread'
  def initialize
    @x = 0; @estado = 0
    @mut = Mutex.new
    @cv = ConditionVariable.new
  end
  def run
    @estado = 0
    t1 = Thread.new {f1}
    t2 = Thread.new {f2}
    sleep 0.1; @mut.lock
    @cv.wait(@mut) while
      (@estado != 2)
    puts ' %d ' % @x
    @mut.unlock
  end
  def f1
    sleep 0.1; @mut.lock
    @cv.wait(@mut) while
      (@estado != 0)
    @x += 3; @estado += 1
    @cv.broadcast()
    @mut.unlock
  end
  def f2
    sleep 0.1; @mut.lock
    @cv.wait(@mut) while
      (@estado != 1)
    @x *= 2; @estado += 1
    @cv.broadcast()
    @mut.unlock
  end
end
