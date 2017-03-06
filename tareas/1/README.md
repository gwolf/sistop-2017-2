# Tarea 1: Depuración por _trazas_

## Descripción del trabajo a realizar

Vimos en clase una introducción a lo que podemos aprender observando
las llamadas al sistema que hace un programa (pueden revisar un
ejemplo en las
[láminas 32 y 33 de la presentación](http://gwolf.sistop.org/laminas/03-relacion-con-el-hardware.pdf#page=32)
o en la
[sección 2.7.1 del libro](http://sistop.org/pdf/sistemas_operativos.pdf)).

Para esta primera tarea, quiero que ustedes realicen un ejercicio
similar a lo que demostré en clase. Esto es:

- Elijan un programa _sencillo_, y _tracen_ su ejecución
    - En Linux, con `strace`. En MacOS, pueden usar `ktrace` o
      `dtrace`.
    - En Windows hay muchos programas, aunque hasta donde puedo
      entender, ninguno viene preinstalado por default. Me encontré
      con el [Dr. Memory Framework](http://drmemory.org/), que dice
      tener un _Strace for Windows_.
    - Obviamente, si encuentran otra herramienta, ¡bienvenida!
- La salida de la ejecución probablemente va a ser _muy_
  grande. Hagan una revisión rápida a ojo para buscar una región
  interesante, y elijan unas _25 llamadas consecutivas_ en que se
  quieran enfocar
    - _Ojo:_ No hace falta que detallen las 25 llamadas una tras
      otra. Si tenemos grupos de llamadas relacionadas, ahórrense el
      describir a cada una de ellas. Hay llamadas obvias y aburridas,
      como `close` o `munmap` que no requieren profundizar.
- Expliquen qué comprenden o qué intuyen de esa porción de la
  ejecución.
    - ¿Línea por línea? ¿Explicando grupos de llamadas? De ustedes
      depende
- Intenten intuir qué _no_ aparece. Esto es, de ser posible, indiquen
  evidencia indirecta de procesamiento de algún conjunto de datos
  _dentro del programa_
    - El ejemplo que les puse en clase: Vimos el resultado de llamar
      `strace ls`. Hacia el final de la salida, vimos el siguiente
      resultado:

	        open(".", O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC) = 3
			fstat(3, {st_mode=S_IFDIR|S_ISVTX|0777, st_size=2182, ...}) = 0
			getdents(3, /* 65 entries */, 32768)    = 2632
			getdents(3, /* 0 entries */, 32768)     = 0
			close(3)                                = 0
			fstat(1, {st_mode=S_IFCHR|0666, st_rdev=makedev(1, 3), ...}) = 0
			ioctl(1, TCGETS, 0x7ffff35cf360)        = -1 ENOTTY (Inappropriate ioctl for device)
			write(1, "01-presentacion.org\n01-presentac"..., 1093) = 1093
			close(1)                                = 0
			close(2)                                = 0
			exit_group(0)                           = ?
			+++ exited with 0 +++
    - Les mencioné que la llamada a `getdents` me entregó las 65
      entradas que tiene el directorio actual (*g*et *d*irectory
      *ent*rie*s*), y le siguió un segundo `getdents` confirmando que
      no hay más información por leer. Posteriormente, hay una única
      llamada `write` que entrega el listado de directorios
    - Comentamos que entre estas dos llamadas hay una operación
      interna: El ordenamiento alfabético de los archivos antes de
      imprimir el resultado
    - ¿Qué _resulta necesario_ que haya procesado internamente el
      proceso que lanzaron?

## Instrucciones de entrega

- Esta tarea es para entrega individual.
- La entrega se hará por Git, siguiendo el esquema de directorios
  especificado en el
  [punto 4 de la práctica 1](https://github.com/gwolf/sistop-2017-2/blob/master/practicas/1/README.md),
  y se considera entregado en el momento en que generen el _pull
  request_ correspondiente.
- Pueden entregar un documento de texto, un archivo PDF, las
  fotografías de pantallazos impresos y anotados en pluma, _como les
  acomode realizar esta práctica_.
- Deben indicar:
    - En qué sistema operativo trabajaron
    - Qué programa emplearon para obtener la traza
    - Qué programa objetivo trazaron
        - ¿Por qué eligieron este programa?
    - Sus observaciones / resultados

## Recursos adicionales

- En sistemas Unix, recuerden la máxima: _man es tu amigo_. Si quieren
  saber qué hace una llamada al sistema, revisen la sección 2 del
  manual. Esto es, del ejemplo anterior: Si quieren saber qué hace
  `fstat`, basta con que escriban desde la terminal `man 2 fstat`, y
  el título de la página les indica `get file status` — Obtiene la
  información acerca de determinado archivo.
    - Claro está, pueden seguir leyendo el texto de la página para
      comprender qué significan los argumentos que recibe y los
      códigos de retorno que entrega.
- Si les interesa revisar una página del manual y no tienen un sistema
  Unix a la mano, pueden entrar a
  [Debian Manpages](https://manpages.debian.org/) y obtener la misma
  información para un sistema Debian
    - Con las ligas en la parte derecha de la pantalla pueden
      consultar las secciones y páginas relacionadas
- Las herramientas de traza son muchas veces importantes bloques de
  construcción para diferentes tareas de monitoreo. Pueden referirse
  por ejemplo a
  [Top 10 DTrace scripts for MacOS X](http://dtrace.org/blogs/brendan/2011/10/10/top-10-dtrace-scripts-for-mac-os-x/)
  como un ejemplo de cómo se obtiene esta información en MacOS
- La página de manual de `strace` les presenta cómo afinar sus
  consultas, obtener datos totalizados, ver cuánto tiempo toma cada
  llamada al sistema, etc. Pueden jugar con esta salida
  también. ¿Encontraron algo interesante especificando estas opciones?
  Con gusto les cuento algún puntito adicional ;-)
