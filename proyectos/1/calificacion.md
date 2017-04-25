# Calificación del primer proyecto parcial (monitor de sistema)

## Entregas en tiempo (_t_ ≤ 30.03.2017)

### Ivan Hernández
* **Lenguaje:** Python
* **Sincronización empleada para:** Mutex
* **Archivos:** [Documentación](./HernandezIvan/documentacion.txt), [programa](./HernandezIvan/Monitor1.py)
* **Comentarios:**
    * En general una muy buena implementación. ¡Felicidades! Te bajó
      un poco el manejo (correcto pero muy simplista) de la
      concurrencia y el no darle complejidad al manejo de la
      información recabada.
    * Tienes que trabajar un poco en tu redacción. Cuesta trabajo leer
      tu documentación; imagina si la estás consultando para un
      programa que buscas ejecutar *en producción*.
    * Me gusta que estés considerando información proveniente de
      diferentes fuentes. Es de las primeras veces que veo que emplean
      datos obtenidos de `platform` además de la ejecución de ciertos
      comandos ejecutados en el sistema
        * No estás *combinando* esta información, que es uno de los
          puntos requeridos (de alguna manera, *interpretar* lo que
          encuentras)
    * ¡Ugh! Este punto estoy seguro que lo voy a copiar a varios de
      tus compañeros: Abusas de las llamadas a ejecución de comandos.
        * ¿Limpiar la pantalla con `os.clear`? ¿Cuántas llamadas al
          sistema genera eso? ¿Por qué no te vas con algo más
          sencillo? Podrías usar la llamada ANSI, ya que estás usando
          `colorama` — `print(chr(27)+'c')`. Sí, no es obvio, pero es
          muchísimo más eficiente :-] Además de funciona incluso si no
          tengo `/usr/bin/clear` instalado.
        * Presentas el contenido de varios archivos de `/proc`
          llamando a `cat`. Podrías abrirlo como un archivo,
          imprimirlo de una, e incluso trabajar con cada una de las
          líneas que se van presentando:

			    f = open('/proc/meminfo')
				for line in f.readlines():
				  print(line),
    * Respecto al punto que preguntas de `colorama` y los archivos
      `.pyc`: Estos son archivos de Python compilados (de ahí la `c`
      del nombre). No *debería* ser necesario borrar manualmente a ese
      archivo; posiblemente haya sido causado porque lo compiló un
      Python 2.x y lo intentaste usar desde un 3.x (¡son en realidad
      lenguajes bastante distintos!)
	  
	  Como sea, dado que estás usando Ubuntu: Te ahorrarías este dolor
      de cabeza si en vez de instalar con `pip3` (mecanismo interno de
      Python) lo hicieras desde `apt`, que mantiene coherencia sobre
      toda la instalación: `apt install python3-colorama`. Ya
      hablaremos de los archivos y los *números mágicos*.
* **Calificación:**
  * *Requisitos:* 10
      * Cumplimiento: 10
  * *Proyecto:* 6.66
      * Creatividad: 5
      * Complejidad: 5
      * Interfaz usuario: 10
  * *Documentación:* 10
      * Documentación externa: 10
      * Entorno y dependencias: 10
      * Comentarios: 10
  * *Entrega:* 10
      * Historia en Git: 10
      * Directorio de proyecto: 10
      * Código válido: 10
  * *Concurrencia:* 6.25
      * Multiproceso: 7.5
      * Sincronización: 5
  * **Global:** 8.6


### Servando López
* **Lenguaje:** Python
* **Sincronización empleada para:** Señalización de obtención de datos
  a GUI, mutex para la obtención de datos
* **Archivos:**
  [Programa principal](./LopezFernandezServandoMiguel/monitor_system.py),
  [obtención de información](./LopezFernandezServandoMiguel/gathering_information.py),
  [interfaz usuario Glade](./LopezFernandezServandoMiguel/main_window1.glade)
  varias versiones previas(?)
  (`main_window.py`,`main_window1.py`,`main_window2.py`), y varios
  recursos gráficos
* **Comentarios:** 
  * ¡Excelente desarrollo! Y dado que lo comentamos en clase por un
    par de errores de manejo de Git, acepto tu entrega extemporánea de
    documentación como entrega en tiempo.
      * Considero para esto lo relativo a la documentación, no los
        comentarios y el manejo del árbol Git (que no fueron escritos
        como parte del proceso de desarrollo sino como respuesta a la
        evaluación recibida).
  * En `generate_cpu_info()`, asumes que tu CPU será Intel o AMD. Si
    corro tu programa en mi ARM me va a decir que es un AMD. Está
    bien, es sólo *eye candy*, pero le das mucho *protagonismo* a un
    dato no corroborado
  * En `pull_processes_list()`, usas `data.txt` como archivo temporal
    para recibir la información de un `ps aux`, para leerlo de
    inmediato y trabajarlo desde memoria. Podrías ahorrarlo con
    `io.popen`:

		with os.popen('ps aux', mode='r') as fl:
		  for line in fl:
		    haz_algo_con(line)
* **Calificación:** 
  * *Requisitos:* 10
      * Cumplimiento: 10
  * *Proyecto:* 10
      * Creatividad: 10
      * Complejidad: 10
      * Interfaz usuario: 10
  * *Documentación:* 6.66
      * Documentación externa: 10
      * Entorno y dependencias: 10
      * Comentarios: 0
  * *Entrega:* 7.5
      * Historia en Git: 5
      * Directorio de proyecto: 7.5
      * Código válido: 10
  * *Concurrencia:* 8.75
      * Multiproceso: 10
      * Sincronización: 7.5
  * **Global:** 8.6

## Entregas extemporáneas (30.03.2017 < _t_ ≤ 06.04.2017)

### Antonio Arizmendi
* **Lenguaje:** Python
* **Sincronización empleada para:** Señalización: Indica que una
  función terminó su ejecución. Resulta innecsario (pues no maneja
  múltiples hilos/procesos)
* **Archivos:**
  [Documentación](./ArizmendiAntonio/InformacionDePrograma.txt),
  [Programa](./ArizmendiAntonio/MonitorDeSistema1.py)
* **Comentarios:**
    * ¡Obtienes datos de forma muy subóptima!
        * Si únicamente vas a leer un archivo (como en tu línea 11),
          en vez de llamar a `cat` con ese archivo, es muy preferible
          usar `open` (directamente desde Python, evitando tu uso de
          `commands.getoutput`)
        * Piensa en la cantidad de procesos que tu prograba tiene que
          lanzar entre las líneas 23 y 27, o entre 51 y 54 — ¡Cuatro
          ejecuciones de procesos por línea!
        * Ahora, a pesar de todo: La forma en que lo haces es
          ingeniosa, y muestra que buscaste una manera _simple_ de
          procesar un archivo de texto. Como sea, va un ejemplo de
          cómo reemplazar las líneas 23-27 directamente en Python:

				import re
				data = {}
			    f = open('/proc/meminfo', 'r')
				for line in f.readlines():
				    m = re.match('(MemTotal|MemFree|MemAvailable|SwapTotal|SwapFree): *(\d+) ', line)
					if m:
					     data[m.group(1)] = m.group(2)

		  Sí, estoy usando las artes obscuras de las expresiones
          regulares (el módulo `re`). Pero con esta expresión obtengo
          en `data` un diccionario con la información tal como la
          requieres:

				{'MemAvailable': '2222208', 'SwapTotal': '3813372', 'MemFree': '450340', 'MemTotal': '5928484', 'SwapFree': '3684008'}

				    
* **Calificación:**
  * *Requisitos:* 10
      * Cumplimiento: 10
  * *Proyecto:* 8.33
      * Creatividad: 5
      * Complejidad: 10
      * Interfaz usuario: 10
  * *Documentación:* 7.5
      * Documentación externa: 7.5
      * Entorno y dependencias: 5
      * Comentarios: 10
  * *Entrega:* 8.33
      * Historia en Git: 5
      * Directorio de proyecto: 10
      * Código válido: 10
  * *Concurrencia:* 3.75
      * Multiproceso: 0
      * Sincronización: 7.5
  * **Global:** 7.58 × 0.8 = 6.06

### Emilio Cabrera
* **Lenguaje:** Python
* **Sincronización empleada para:** 
* **Archivos:**
  [Documentación](./CabreraEmilio/monitor-de-sistema/README.md),
  [Programa](./CabreraEmilio/monitor-de-sistema/monitor),
* **Comentarios:**
    * Umh, me llama la atención en tu documentación, mencionas:
        *  Python <= 3.6... Pero te aseguro que esto no funciona con
           Python 2.x
        *  psutil >= 3.2.1... Pero usas `psutil.cpu_freq`, que
           [dice la documentación](https://pythonhosted.org/psutil/)
           que apareció en 5.1.0 (y, ¡calamidad! en Debian Testing
           tenemos únicamente 5.0.0). Tuve que comentar tu llamada a
           esta función.
    *  No hay comentario alguno ☹
* **Calificación:**
  * *Requisitos:* 10
      * Cumplimiento: 10
  * *Proyecto:* 10
      * Creatividad: 10
      * Complejidad: 10
      * Interfaz usuario: 10
  * *Documentación:* 6.66
      * Documentación externa: 10
      * Entorno y dependencias: 10
      * Comentarios: 0
  * *Entrega:* 9.16
      * Historia en Git: 10
      * Directorio de proyecto: 10
      * Código válido: 7.5
  * *Concurrencia:* 7.5
      * Multiproceso: 10
      * Sincronización: 5
  * **Global:** 8.66 × 0.8 = 6.93

## Entregas _muy_ extemporáneas (06.04.2017 < _t_ ≤ 20.04.2017)

### Octavio Alatorre
* **Lenguaje:** Java
* **Sincronización empleada para:** 
    * Métodos `synchronized` de Java (Mutex)
* **Archivos:**
  [Documentación](./AlatorreOctavio/documentacion.txt),
  [Programa](./AlatorreOctavio/ProjectTest/src/projecttest/Monitor.java)
* **Comentarios:**
    * No logré hacer que compilara... Así que limito mi análisis a lo
      que puedo ver de tu código
        * Claro, siendo Java... Me espera un trabajo largo ;-)
    * A pesar de que usas Java (lenguaje multiplataforma) y Sigar
      (obtención portable de información de sistema), estás
      "amarrando" tu código a sólo funcionar desde sistemas Windows:
      Tu línea 129 llama a `sigar.getFileSystemUsage("C:")`. En vez de
      incluir en "duro" a `C:`, podrías haber elegido alguna partición
      de `sigar.df`
    * ¿La concurrencia se limita a crear tres hilos que irán haciendo
      lo mismo (mostrar los valores obtenidos) y durmiendo un tiempo
      aleatorio?
* **Calificación:**
  * *Requisitos:* 10
      * Cumplimiento: 10
  * *Proyecto:* 7.5
      * Creatividad: 7.5
      * Complejidad: 10
      * Interfaz usuario: 5
  * *Documentación:* 10
      * Documentación externa: 10
      * Entorno y dependencias: 10
      * Comentarios: 10
  * *Entrega:* 5
      * Historia en Git: 5
      * Directorio de proyecto: 5
      * Código válido: 5
  * *Concurrencia:* 7.5
      * Multiproceso: 7.5
      * Sincronización: 7.5
  * **Global:** 8 × 0.5 = 4

### Isaac Cruz y Afferny Ramírez
* **Lenguaje:** Python
* **Sincronización empleada para:**
  * Barrera, para que todos los elementos de la interfaz se actualicen
    a la vez
* **Archivos:**
  [Documentación](./CruzIsaacRamirezAfferny/README.md)
  [Programa](./CruzIsaacRamirezAfferny/monitor.py)
* **Comentarios:**
  * Muy buen programa... Lástima que lo entregaran tan tarde y la
    calificación bajara tanto :-(
  * Respecto al comentario final en la documentación (que habla de la
    sensible muerte de la laptop de Afferny), de acuerdo: Tomo los
    commits del repositorio que mencionan por buenos. Sin embargo,
    podrían haber llevado el desarrollo dentro del directorio
    `proyectos/1/CruzIsaacRamirezAfferny` del repositorio común. ¡Para
    eso está!
  * Al lanzar el programa, me indica un error porque hacen una llamada
    a la función `sync()` antes de definirla:

		Traceback (most recent call last):
		  File "monitor.py", line 49, in <module>
		    sync()
		NameError: name 'sync' is not defined

	Basta comentar esa llamada para que el programa funcione.
  * El programa funciona mayormente bien, y tiene una interfaz bien
    lograda. Pero por alguna razón, de rato en rato (después de unos
    10-30 segundos) se muere de formas bastante bizarras (desde
    simples "segmentation faults" hasta errores de `curses`). No
    encuentro ninguna razón obvia de este error...

* **Calificación:**
  * *Requisitos:* 10
      * Cumplimiento: 10
  * *Proyecto:* 9.16
      * Creatividad: 7.5
      * Complejidad: 10
      * Interfaz usuario: 10
  * *Documentación:* 9.16
      * Documentación externa: 10
      * Entorno y dependencias: 10
      * Comentarios: 7.5
  * *Entrega:* 9.16
      * Historia en Git: 10
      * Directorio de proyecto: 10
      * Código válido: 7.5
  * *Concurrencia:* 8.75
      * Multiproceso: 7.5
      * Sincronización: 10
  * **Global:** 9.24 × 0.5 = 4.62

### Jesús Rivera
* **Lenguaje:** Python
* **Sincronización empleada para:** No se emplea; se ve que buscaba
  hacerlo, pero la función `main()` (desde donde crearía a todos los
  hilos) está comentada ☹
* **Archivos:**
  [Documentación](./RiveraJesus/README.md),
  [Programa](./RiveraJesus/monitor.py)
* **Comentarios:**
  * El proyecto se veía de lo más pulido y bonito... Pero se ve que
    tuviste problemas para terminarlo en un tiempo incluso cercano al
    máximo
* **Calificación:**
  * *Requisitos:* 5
      * Cumplimiento: 5
  * *Proyecto:* 9.16
      * Creatividad: 7.5
      * Complejidad: 10
      * Interfaz usuario: 10
  * *Documentación:* 8.33
      * Documentación externa: 10
      * Entorno y dependencias: 10
      * Comentarios: 5
  * *Entrega:* 8.33
      * Historia en Git: 5
      * Directorio de proyecto: 10
      * Código válido: 10
  * *Concurrencia:* 0
      * Multiproceso: 0
      * Sincronización: 0
  * **Global:** 6.16 × 0.5 = 3.1

## Pasado el 20.04.2017 *no se recibe el proyecto*
