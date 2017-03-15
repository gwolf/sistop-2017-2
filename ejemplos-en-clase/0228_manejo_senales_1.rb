#!/usr/bin/ruby
# coding: utf-8


Signal.trap('USR1') do
  puts 'Me pegó un USR1'
end

Signal.trap('INT') do
  puts '¿Crees que me puedes matar? ¡Jajajajajaja!'
end

Signal.trap('TERM') do
  puts 'Ok, ok, entendí. Ya me voy'
end

# Esto no tiene efecto: KILL, STOP, CONT y otros son inatrapables
Signal.trap('KILL') do
  puts 'INDESTRUCTIBLEEEEEEEEEEEEE'
end

# Vamos a hacer algo inutil y que no rellene demasiado rápido la
# pantalla...
while true do
  print '.'
  sleep(1)
end
