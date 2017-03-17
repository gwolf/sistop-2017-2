#!/usr/bin/ruby
# coding: utf-8
l = ['A', 'B', 'C', 'D', 'E']; # Todos los procesos del sistema
s = []; # Secuencia segura

reclamado = {'A' => 4, 'B' => 2, 'C' => 2, 'D' => 1, 'E' => 5}
asignado = {'A' => 1, 'B' => 1, 'C' => 2, 'D' => 0, 'E' => 3}
libres = 2

puts 'Iniciando algoritmo del Banquero.'
print 'Reclamo (solicitud máxima): '
puts reclamado.map {|proc, num| '%s: %d' % [proc, num]}.join(', ')
print 'Asignado:                   '
puts asignado.map {|proc, num| '%s: %d' % [proc, num]}.join(', ')
puts 'Número de recursos disponibles: %d' % libres

while ! l.empty? do
  p = l.select do |id|
    puts "Considerando %s" % id
    reclamado[id] - asignado[id] <= libres
  end.first
  raise Exception, 'Estado inseguro' if p.nil?
  puts 'Agregando %s a la potencial secuencia segura' % p
  libres += asignado[p]
  l.delete(p)
  s.push(p)
end
puts "La secuencia segura encontrada es: " + s.to_s
