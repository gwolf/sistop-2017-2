
nombreGatos = ['Demostenes', 'Benito', 'Don Gato' , 'Cucho',
 				'Espanto','Panza', 'Tom', 'Marcia']
 nombreRaton = ['Speedy', 'Jerry', 'Micky', 'kirito']

 class Gato #En esta clase se define como será nuestro gato
 	def initialize(hambre, nombre)  #Bueno el gato tendra niveles de hambre y un nombre
 		@nombre = nombre
 		@hambre = hambre 
 		puts "Soy un gato y Me llamo %s" % @nombre + " Tengo un nivel %d de hambre"  % @hambre
 		if @hambre == 1 
 			puts "No tengo mucha hambre"
 		elsif @hambre == 2
 			puts "Tengo un hambre mediana"
 		else 
 			puts "Tengo muuuucha hambre"
 		end
 	end
 end

class Platos
	#En esta clase mi idea era como hacer una lista de los platos y en ella meter los hilos 
	#pero no he conseguido hacerlo, el nivel de hambre me iba a decir cuanto tiempo duraria cada
	#gato en su plato
	def initialize
		@platos = [rand(100)+1]
		@platos_mut = Mutex.new
		@semaf_platos = Concurrent::Semaphore.new(0)
	end
	def come(animal)
		#Aqui asegura el plato en el que come
		@platos_mut.lock
		@platos.push animal
		@platos_mut.unlock
		@semaf_platos.acquire
	end
	def termine
		#libera el plato
		@platos_mut.lock
		animal = @platos.shift
		@platos_mut.unlock
		@semaf_platos.release
		return animal
	end
end

def hambre()  #Para definir la cantidad de hambre que cada animal tendrá
	hambre = rand(3) + 1
	return hambre
end

class Raton 
	#Definimos nuestro pequeño roedor
	def  initialize(hambre, nombre)
		@nombre = nombre
		@hambre = hambre
		puts "Soy un ratón y Me llamo %s" % @nombre + " Y tengo un nivel de hambre %d " % @hambre
	end
end
#auxiliar
contador = 0
#Como segun era k gatos entonces ese k lo pondre en el intervalo de 1 a 100
numGatos = rand(100)+1
gatitos = Array.new
a = true
begin
	hambre1 = hambre #para cada que entre se genere un nivel de hambre
	gatitos<< Thread.new{Gato.new(hambre1, nombreGatos.sample)}   #crea un hilo simulando un gato independiente 
	sleep hambre1    #el gato tardara dependiendo cuanta hambre tenga
	contador = contador + 1
	puts numGatos
	puts contador
	if contador == numGatos
		puts 'termine'
		a = false
	else 
		a = true
	end

end while a != false

print gatitos




raton = Thread.new{Raton.new(hambre1, nombreRaton.sample)}
=begin
puts raton
while true do
	hambre1 = hambre #para cada que entre se genere un nivel de hambre
	Thread.new{Gato.new(hambre1, nombreGatos.sample)}   #crea un hilo simulando un gato independiente 
	sleep hambre1    #el gato tardara dependiendo cuanta hambre tenga
end
=end