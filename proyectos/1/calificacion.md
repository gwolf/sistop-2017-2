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
  * ¡Excelente desarrollo! Es una lástima que no incluyera _nada_ de
    documentación ni de comentarios. ¡Merecías mucho mejor
    calificación!
  * Veo que incluyes versiones parciales de tu código. ¡Pero si para
    eso está Git! Si hubieras desarrollado tu programa sobre de tu
    primer `main_window.py` (en vez de dejarlo _de costadito_)
    tendrías los commits necesarios para ese punto completo
      * Además, vendría muy bien que usaras un `.gitignore` — Tu
        proyecto incluye un archivo temporal autogenerado `data.txt`,
        que podría darle a alguien hostil información acerca de tu
        sistema. Y cada vez que yo lo ejecuto, me marca que el árbol
        Git está *sucio*, pues este archivo se modifica.
      * También el directorio `__pycache__` completo debería estar en
        `.gitignore`
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
  * *Documentación:* 1.66
      * Documentación externa: 0
      * Entorno y dependencias: 5
      * Comentarios: 0
  * *Entrega:* 7.5
      * Historia en Git: 5
      * Directorio de proyecto: 7.5
      * Código válido: 10
  * *Concurrencia:* 8.75
      * Multiproceso: 10
      * Sincronización: 7.5
  * **Global:** 7.6

## Entregas extemporáneas (30.03.2017 < _t_ ≤ 06.04.2017)

### Antonio Arizmendi
* **Lenguaje:**
* **Sincronización empleada para:** 
* **Archivos:**
* **Comentarios:**
* **Calificación:**
  * *Requisitos:* 
      * Cumplimiento: 
  * *Proyecto:* 
      * Creatividad: 
      * Complejidad: 
      * Interfaz usuario: 
  * *Documentación:* 
      * Documentación externa: 
      * Entorno y dependencias: 
      * Comentarios: 
  * *Entrega:* 
      * Historia en Git: 
      * Directorio de proyecto: 
      * Código válido: 
  * *Concurrencia:* 
      * Multiproceso: 
      * Sincronización: 
  * **Global:** 

### Emilio Cabrera
* **Lenguaje:**
* **Sincronización empleada para:** 
* **Archivos:**
* **Comentarios:**
* **Calificación:**
  * *Requisitos:* 
      * Cumplimiento: 
  * *Proyecto:* 
      * Creatividad: 
      * Complejidad: 
      * Interfaz usuario: 
  * *Documentación:* 
      * Documentación externa: 
      * Entorno y dependencias: 
      * Comentarios: 
  * *Entrega:* 
      * Historia en Git: 
      * Directorio de proyecto: 
      * Código válido: 
  * *Concurrencia:* 
      * Multiproceso: 
      * Sincronización: 
  * **Global:** 

## Entregas _muy_ extemporáneas (06.04.2017 < _t_ ≤ 20.04.2017)

## Pasado el 20.04.2017 *no se recibe el proyecto*
