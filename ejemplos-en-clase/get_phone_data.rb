#!/usr/bin/ruby
# coding: utf-8
#
# Presenté este programa ejemplo de cómo resolví la necesidad de hacer
# hasta 512 conexiones simultáneas (a todos los teléfonos IP que hay
# en dos bloques de red) para obtener información de ellos.
#
# Hay varios detalles que no resultan relevantes el procesamiento
# mismo de la información que recibo), lo que me pareció importante
# recalcar es que lanzo las 512 solicitudes en paralelo
require 'net/http'
require 'nokogiri'
require 'ipaddr'
require 'yaml'

class Phone < Hash
  def add_info(line)
    if (line.def =~ /Identidad.1.Estado/ and line.data =~ /(\d+)\@([\d\.]+):/)
      self['phone'] = $1
      self['pbx'] = $2
    elsif (line.def == 'Dirección-MAC' and line.data =~ /^([\dABCDEF]{2})([\dABCDEF]{2})([\dABCDEF]{2})([\dABCDEF]{2})([\dABCDEF]{2})([\dABCDEF]{2})/)
      self['mac'] = '%s:%s:%s:%s:%s:%s' % [$1,$2,$3,$4,$5,$6]
    end
    self[line.def] = line.data
  end
end

class TableLine
  attr_accessor(:def, :data)
  def initialize(string)
    string =~ /^([^:]+):(.+)$/ or
      raise RuntimeError, 'Invalid table line: %s' % string
    @def, @data = $1, $2
  end
end

conf = YAML.load_file '/tmp/phone_conf.yaml'
@networks = conf[:nets].map {|net| IPAddr.new(net)}
@cred = conf[:cred]
@phones = {}
@mutex = Mutex.new

# Función que es lanzada de forma paralela: Abrir la conexión HTTP,
# obtener la información, procesarla y registrarla en el arreglo @phones
def get_phone_info(host)
  p = Phone.new
  uri = URI('http://%s/info.htm' % host)
  req = Net::HTTP::Get.new(uri)
  req.basic_auth(@cred[:login], @cred[:pass])
  http = Net::HTTP.new(uri.hostname, uri.port)
  http.open_timeout = 2
  http.read_timeout = 5
  begin
    res = http.request(req)
  rescue Net::OpenTimeout, Errno::ECONNREFUSED
    return 0
  end

  # Ojo: Desconozco si Nokogiri (que procesa un documento HTML como un
  # árbol y me permite buscar información dentro de este) puede
  # manejarse confiablemente de forma concurrente, así que lo incluyo
  # como parte de mi sección crítica. Claro, también entra el agregar
  # cada elemento a @phones.
  @mutex.lock
  doc = Nokogiri(res.body)
  doc.search('table.bubbleTable tr').
    map    {|tr| tr.inner_text}.
    reject {|tr| tr.nil? or tr.empty? or tr =~ /^\s*$/}.
    map    {|line| TableLine.new(line) rescue nil}.
    reject {|line| line.nil?}.
    each   {|line| p.add_info(line) }
  @phones[host.to_s] = p
  @mutex.unlock
end


i=0
@networks.each do |net|
  puts 'Red: %s (%d direcciones)' % [net, net.to_range.map{1}.reduce(&:+)]
  net.to_range.each do |host|
    i+=1
    print '.'
    puts i if i%50 == 0
    Thread.new{ get_phone_info(host) }
  end
  puts ''
end
# Espero a que termine (t.join) cada uno de los hilos que lancé, a
# excepción del actual.
Thread.list.each {|t| next if Thread.current == t; t.join}

i=0
puts '%-5s  %-15s  %-15s' % ['Tel', 'IP', 'MAC']
puts '=' * 50
@phones.each do |entry|
  ip,phone = entry[0],entry[1]
  i+=1
  puts '%5s  %-15s  %15s' % [phone['phone'], phone['Dirección-IP'], phone['mac']]
end
