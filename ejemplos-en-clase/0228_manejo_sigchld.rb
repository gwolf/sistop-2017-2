#!/usr/bin/ruby
# coding: utf-8

Signal.trap('CHLD') do
  puts "Uno de mis procesos hijo ya terminó"
end

pid_orig = $$
3.times do fork() end

if pid_orig == $$
  puts "Proceso padre... Mantenemos esto vivo"
  3.times do
    Process.wait
  end
  while true
    sleep 1
  end
else
  puts "Proceso hijo %d. Chau." % $$
  sleep 3
  exit 0
end
