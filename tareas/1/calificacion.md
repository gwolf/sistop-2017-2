# Calificación de la tarea 1 (depuración por _trazas_)

## Entregas en tiempo (_t_ ≤ 21.02.2017)

### Isaac Cruz
* **Archivo:** [DepuracionPorTrazas.pdf](./CruzIsaac/DepuracionPorTrazas.pdf)
* **Calificación:** 8
* **Comentarios:**
  * Si bien `access` sirve directamente para verificar permisos, en
    este caso está pidiendo el argumento `F_OK` — Meramente verifica
    si existe ese archivo.
  * El `read` que presentas no está aún leyendo el archivo `ejemplo`
    que especificaste; lo que ves es el encabezado de un archivo de
    biblioteca `/lib/x86_64-linux-gnu/libselinux.so.1` que abrió el
    `open` de la línea anterior: En este momento, aún se está dando
    cumplimiento al `execve`, estás viendo cómo se cargan en memoria
    las bibliotecas previas a la ejecución de tu `cp`. En particular,
    SELinux es un marco de seguridad que verifica que los programas
    cumplan con el patrón _normal_ de ejecución.
	
	Si ves que leyó 832 caracteres es porque únicamente _pidió_ esos
    832 caracteres: Es uno de los parámetros de la llamada. Es el
    tamaño del buffer donde está cargando. En mi sistema, este archivo
    mide 155400 bytes, pero todos estos conjuntos de `open`/`read`
    leen sólo el encabezado.
  * El trabajo "real" de copiado no empieza aún en la región que
    revisaste; hasta este momento, sigues únicamente en la carga de
    bibliotecas para la ejecución de `cp`. La _carnita_ de `cp` se ve
    a continuación, casi al final de la salida de `strace`:

		open("ejemplo", O_RDONLY)   = 3
		fstat(3, {st_mode=S_IFREG|0644, st_size=517, ...}) = 0
		open("ejemplo1", O_WRONLY|O_CREAT|O_EXCL, 0644) = 4
		fstat(4, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
		fadvise64(3, 0, 0, POSIX_FADV_SEQUENTIAL) = 0
		mmap(NULL, 139264, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f7d89134000
		read(3, "#+setupfile: setup_laminas.org\n#"..., 131072) = 517
		write(4, "#+setupfile: setup_laminas.org\n#"..., 517) = 517
		read(3, "", 131072)                     = 0
		close(4)                                = 0
		close(3)                                = 0
		munmap(0x7f7d89134000, 139264)          = 0

	Notarás que en este caso mi archivo `ejemplo` es más bien pequeño:
    el `read` está pidiendo leerlo en un buffer de hasta 128K
    (131072), pero el archivo mide 517 bytes. Claro, si fuera un
    archivo más grande verías parejas de `read`/`write` alternándose.
  * Te califico con 8 porque te apresuraste a presentar conclusiones
    que _no se obtienen_ del pedazo de código que presentas. Las
    explicaciones que presentas a las llamadas son correctas, pero de
    ellas _no se puede obtener_ la naturaleza de ejecución de `cp`.

### Ricardo Hernández
* **Archivo:** [tarea1.txt](./HernandezRicardo/tarea1.txt)
* **Calificación:** 8
* **Comentarios:**
  * Ojo con los formalismos: En tu explicación del `execve` indicas
    que _entra a la carpeta bin_ y _ejecuta el comando cat_. Eso
    tendría que hacerse mediante una llamada al sistema adicional
    (`chdir`); al especificar `execve("/bin/cat", ...)` estás en
    realidad ejecutando `/bin/cat` _sin cambiar tu directorio actual_.
  * Mapear una región de memoria (lo que hacen las llamadas `mmap`) lo
    que significa es _asignar_ regiones de memoria, no lee nada a
    ellas (no está especificando un archivo para mapeo a memoria; ese
    es un tema que abordaremos más adelante).
  * La traducción correcta de la función de `arch_prctl` es definir el
    estado de hilo _de forma específica a la arquitectura_ (configura
    la ejecución de algún detalle del hilo). De nuevo, no hemos
    hablado aún lo suficiente de hilos, pero revisando rápidamente el
    manual, esto modifica la dirección base del registro FS a la
    dirección especificada; no sabemos qué es esa dirección, pero cae
    dentro del segundo `mmap` inmediatamente precedente.
  * Te hago el mismo comentario que el que hice a Isaac: Elegiste
    comentar sobre el _principio_ de la ejecución del programa. Hasta
    donde llegó tu traza, todavía está atendiendo a la llamada
    `execve`, esto es, está cargando las bibliotecas y el entorno
    necesario para el proceso; no has llegado a la ejecución misma del
    `cat`. No puedes, entonces, explicar cómo opera el `cat` que a
    duras penas ha comenzado.

### Servando López
* **Archivo:** [Trace.pdf](./LopezFernandezServandoMiguel/Trace.pdf)
* **Calificación:** 10
* **Comentarios:**
  * ¡Muy buen trabajo!
  * Tengo que corregir algunos detalles: En español, no son
    _librerías_, sino _bibliotecas_. La diferencia semántica es
    grande, e importante.
  * Los errores producidos por las llamadas `access` no es porque no
    tengas permisos para leer esos archivos, sino porque esos archivos
    _sencillamente no existen_. Como vimos en clase, la jerarquía
    dentro de `/proc` es una ventana al kernel; el que el directorio
    `/proc/net/ax25` no exista significa que tu kernel no tiene
    _actualmente_ soporte para el protocolo de red AX.25 (el protocolo
    de radio por paquetes, conocido como HAM Radio, o
    radioaficionado). Es un protocolo histórico y mayormente obsoleto,
    pero de tenerlo configurado, `ifconfig` tendría que reportarte
    interfaces que lo utilicen como transporte. (Vale lo mismo para
    los demás protocolos también)
  * Efectivamente, los `ioctl` están leyendo de _algo_ que se comporta
    como un archivo, pero no viste ningún _open_ que les
    corresponda. Algunas líneas atrás (en tu listado de la página 3)
    puedes ver una llamada `socket(AF_INET, SOCK_DGRAM, IPPROTO_IP)`
    que entrega un valor `4`, y otro que va sobre AF_INET6 que entrega
    `5`. Estos son los descriptores de archivo que usan los `ioctl`;
    citando la página de manual, _ioctl manipula los parámetros
    subyecentes de los archivos especiales_. Lo que hizo `ifconfig` es
    abrir un socket sobre cada familia de redes que tiene soporte, y
    _preguntar_ acerca de las interfaces correspondientes —
    Incluyendo, como mencionas, los parámetros como la dirección
    física de la red (obtenido por la llamada `SIOCGIFHWADDR`)

### Afferny Ramírez
* **Archivo:** [tarea1.txt](./RamirezAfferny/tarea1.txt)
* **Calificación:** 7
* **Comentarios:**
  * Las llamadas relacionadas con `epoll` no verifican entrada/salida,
    sino que crean un espacio de notificación de eventos. Esto es
    porque la resolución de nombres típicamente manda las consultas de
    forma simultánea a los distintos servidores (y otras formas de
    resolución de nombres) que tengas configurados en
    `/etc/resolv.conf`, y basta con recibir la respuesta de
    _cualquiera_ de ellos.
  * `mmap` no tiene relación con la red, sino con mapear (asignar) un
    espacio de memoria
  * Dentro de las llamadas `open` que mencionas, nada indica que esté
    intentando todavía resolver el DNS
  * ¿Por qué asumes que un `open` sobre `/usr/bin/ssl/openssl.cnf`
    _reevisa la seguridad de la conexión_? ¿O que la lectura de esa
    configuración _prueba la configuración de la red_?
  * ¿Qué de lo que viste en la ejecución te lleva a deducir que Linux
    _realiza más revisiones de seguridad y certificados que Windows_?
    Aplicaste más prisa por llegar a conclusiones _interesantes_ que
    por fundamentarlas. Presentas la traza desde un punto interesante,
    pero presentas conclusiones que no vienen de lo observado.

### Jesús Rivera
* **Archivo:** [tarea1.txt](./RiveraJesus/tarea1.txt)
* **Calificación:** 10
* **Comentarios:**
  * En tu primer grupo de llamadas: No es que el `4` especifique la
    versión de protocolo de IP a utilizar, sino que (casualmente) es
    el primer descriptor de archivo libre que encuentra; está
    indicando IPv4 al emplear `PF_INET` (IPv6 usa la familia
    `PF_INET6`, la comunicación entre procesos por sockets usa
    `PF_UNIX`, y hay otras varias familias de protocolos (`PF_`).
  * No hemos hablado de las señales que pueden enviarse entre
    procesos; vamos a abordar más adelante las líneas de
    `rt_sigaction` que mencionas. Estas tres líneas, si no me
    equivoco, indican cómo manejar interrupciones a la ejecución (como
    un `Ctrl-C`).
  * El `setitimer` lo que hace es poner una _alarma_ para que, si no
    se recibió respuesta en el tiempo especificado (10 segundos), un
    paquete del _ping_ sea descartado y se deje de esperar a su
    respuesta.
  * Precisamente el mensaje que se envía sí se ve: Es el contenido del
    `msg_iov` que tiene el `sendmsg`
  * Si bien cometiste algunos (muy comprensibles) errores al
    interpretar algunas llamadas, tu análisis es bastante bueno y
    sigue bastante de cerca lo que les pedí en esta tarea.

### Julio Rodríguez
* **Archivo:** [tarea.txt](./RodriguezJulio/tarea.txt)
* **Calificación:** 8
* **Comentarios:**
  * Poquito texto, y de entrada hay que llamarte la atención sobre la
    ortografía... ¿Devian? ¡Debian! :-P Varias veces escribiste sin
    verificar que tu texto esté correcto — _apara_, _notificaion_, ...
  * ¿Trazar a Dolphin? Guau... Tarea titánica, en realidad. Un
    programa interactivo, parte de un marco "choncho" como KDE... Hace
    una cantidad monumental de llamadas. Estoy casi seguro de que lo
    que alcanzas a trazar ocurre mucho antes incluso de mostrar la
    interfaz. Pero, claro, nunca dije que eso no valiera. Y si te
    enseñó algo acerca del programa en cuestión, la tarea aplicó
    exitosamente.
  * Te refieras mucho a la _localidad de memoria_. En casi todos los
    casos (por ejemplo, en las llamadas de la familia `stat`) no se
    refiere a localidades de memoria (se indicarían con una dirección
    numérica, típicamente hexadecimal), sino que a archivos
    (`/root/.local/share/fonts`, `/root/.fonts`,
    `/usr/share/fonts/cmap`, etc.)
  * La llamada `read` donde indicas que _lee todos y manda una
    notificación de error_ esstá leyendo del descriptor de archivo 6
    (no de "todos", sino que de un archivo en particular, del recién
    abierto `/usr/share/fonts.cmap`). ¿De dónde obtienes que maneja
    algún tipo de notificación si hay errores?
  * Te califico con 8 por lo mismo que comenté a algunos compañeros
    anteriores a tí: Si bien no puedo esperar que _entiendan_ cada una
    de las llamadas al sistema, sí les estoy pidiendo que expliquen lo
    que ocurre a partir de lo que observan. Varias de las cosas que
    indicas (p.ej. la notificación de error) no pueden obtenerse a
    partir de la información que proporcionas. Ojo: No considero en
    este caso el error de hablar de _localidades de memoria_; no hemos
    abordado esto en clase, y puede ser una confusión de tu parte.

## Entregas extemporáneas ( 21.02.2017 < _t_ ≤ 28.02.2017)

Se califican sobre 8

### Octavio Alatorre
* **Archivos:**
  [global.2456.log](./AlatorreOctavio/DrMemory-wow.exe.2456.000/global.2456.log),
  [missing_symbols.txt](latorreOctavio/DrMemory-wow.exe.2456.000/missing_symbols.txt),
  [potential_errors.txt](./AlatorreOctavio/DrMemory-wow.exe.2456.000/potential_errors.txt),
  [results.txt](./AlatorreOctavio/DrMemory-wow.exe.2456.000/results.txt),
  [suppress.txt](./AlatorreOctavio/DrMemory-wow.exe.2456.000/suppress.txt),
  [conclusiones.txt](./AlatorreOctavio/conclusiones.txt)
* **Calificación:** 9 × 0.8 = 7.2
* **Comentarios:**
    * **GUAU**... Lanzarte a analizar algo tan complejo como un juego
        resulta...  impresionante :-) Claro, el volumen de información es
        demasiado como para encontrar qué está ocurriendo.
    * Lo que mencionas de los posibles _leaks_: Explico brevemente, ya
      lo platicaremos más adelante. Cuando obtienes memoria en C
      mediante un `malloc()`, el sistema te otorga un _apuntador_ a un
      espacio de memoria reservado. Como programador, tienes la
      obligación de mantener la contabilidad de la memoria que has
      pedido.
	  
	  Si en algún momento tienes un bloque de memoria asignado por
      `malloc()` y dejas de utilizarlo, debes liberarlo con
      `free()`. Si no lo liberaste, esa memoria se mantiene asignada y
      reservada durante el tiempo de vida de tu programa, pero no
      tienes cómo llegar a ella — Y así, paulatinamente, el espacio en
      memoria que tu programa ocupa va creciendo _sin sentido_. En un
      programa que ejecutas por largo tiempo, esto puede pegarle a la
      usabilidad.
	  
	  Vamos, los _memory leaks_ (_goteos_ de memoria) son un error de
      programación... Podrías verlos como relativamente menores, pero
      no por eso menos importantes de verificar. Ahora, lo que
      _DrMemory_ te está indicando es que es un _posible_ leak, no
      tiene certeza.
    * `RtlAllocateHeap`, y prácticamente todas las llamadas _normales_
      de la biblioteca estándar (RTL es del _RunTime Library_,
      _biblioteca en tiempo de ejecución_,
      [revisa la documentación de MSDN](https://msdn.microsoft.com/en-us/library/windows/hardware/ff553354%28v=vs.85%29.aspx))
      trabajan con la memoria _del sistema_. Para asignar y liberar
      memoria gráfica recuerda que son más bien llamadas que
      parecerían _de red_ o _de comunicación_ sobre un bus a un
      procesador especializado. Trazando un programa no puedes obtener
      información de lo que hace el GPU; si acaso, podrías _volcar_
      bloques de memoria que se "avientan" entre CPU y GPU, o hacer un
      análisis de frecuencia de _cada cuánto tiempo_ ocurren estas
      transferencias.
    * En efecto, creo que elegiste un mal candidato para trazar. La
      cantidad de llamadas que tiene que hacer, y la cantidad de
      niveles de abstracción que hay sobre de éstas,
      es... Sencillamente bestial :-]

## Entregas _muy_ extemporáneas ( 28.02.2017 < _t_ ≤ 14.03.2017)

Se califican sobre 5

### Ivan Hernández
* **Archivo:** [tareaSO.docx](./HernandezIvan/tareaSO.docx)
* **Calificación:** 8 × 0.5 = 4
* **Comentarios:** 
    * Veo que al no haber logrado un mayor avance en sólo una
      invocación, revisaste con tres comandos diferentes. ¡bien! :-)
    * Recuerda del ejemplo que les presenté en clase: La mayor parte
      de las primeras llamadas que ves son meramente _armar el
      ambiente_ para poder ejecutar el comando que pediste. Muchas de
      las llamadas que ves en las primeras decenas de líneas son las
      necesarias para inciar la ejecución que solicitó el `execve()`
        * Si comparas las tres ejecuciones, los primeros muchos pasos
          son los mismos: Cargar bibliotecas y algunos binarios que
          permiten la ejecución del programa mismo que te interesa
    * En tu primer caso, ¿cómo es que llega _exitosamente_ a la
      llamada `write` en que ilustras que _escribe los datos del día_?
        * Parte importante de la lógica interna de `date` es
          entregarte la fecha (que obtiene en este caso usando
          `gettime(&t)`) en tu zona horaria y formateada en el
          lenguaje del sistema que tú prefieres (en este caso, el
          español). Por eso ves lecturas a
          `/usr/lib/locale/locale-archive` y a `/etc/localtime`.
    * *Mapear* un espacio de memoria significa pedirle al sistema que
      te asigne una región de memoria del tamaño que le indiques, con
      los modos de lectura/escritura y otros detalles que presenta
      como argumentos.

### Antonio Arizmendi
* **Archivo:** [Traza.pdf](./ArizmendiAntonio/Traza.pdf)
* **Calificación:** 9 × 0.5 = 4.5
* **Comentarios:** 
    * Como pasó con varios de tus compañeros, iniciaste la traza al
      inicio de la ejecución — Lo que ves no llega aún a la ejecución
      de tu programa mismo, sino que está meramente _acomodando el
      universo_ para atender a tu solicitud
    * En todo caso, el programa habrá terminado en fracaso, ¿no?
      (porque no le indicaste el nombre de un directorio a crear: Tu
      línea 1 marca que llamaste `["mkdir"]`, sin indicar el nomrbe
      del directorio. Supongo que la ejecución habrá terminado
      aproximadamente así:

			write(2, "mkdir: ", 7mkdir: )                  = 7
			write(2, "missing operand", 15missing operand)         = 15
			write(2, "\n", 1)                       = 1
			write(2, "Try 'mkdir --help' for more info"..., 41Try 'mkdir --help' for more information.) = 41
			close(1)                                = 0
			close(2)                                = 0
			exit_group(1)                           = ?
			+++ exited with 1 +++

	* Si hubieras especificado un nombre de directorio (sea `cuac`),
      terminaría de la siguiente forma:

			mkdir("/tmp/cuac", 0777)                = 0
			close(1)                                = 0
			close(2)                                = 0
			exit_group(0)                           = ?
			+++ exited with 0 +++


## Pasado el 14.03.2017, *no se recibe la tarea*
