#!/usr/bin/ruby
# coding: utf-8
require 'concurrent'

class EjemploHilos
  def initialize
    @x = 0
    @mut = Mutex.new
    @s1 = Concurrent::Semaphore.new(0)
    @s2 = Concurrent::Semaphore.new(0)
  end
  def run
    t1 = Thread.new {f1}
    t2 = Thread.new {f2}
    sleep 0.1
    @s2.acquire
    @mut.lock
    print ' %d ' % @x
    @mut.unlock
  end
  def f1
    sleep 0.1
    @mut.lock
    print '+'
    @x += 3
    @mut.unlock
    @s1.release
  end
  def f2
    sleep 0.1
    @s1.acquire
    @mut.lock
    print '*'
    @x *= 2
    @mut.unlock
    @s2.release
  end
end

e = EjemploHilos.new
10.times { e.run }
