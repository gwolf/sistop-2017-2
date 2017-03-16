# Calificación de la tarea 2 (Mapa conceptual de lectura)

## Entregas en tiempo (_t_ ≤ 07.03.2017)

### Octavio Alatorre
* **Archivos:**
  [descripcion.txt](./AlatorreOctavio/descripcion.txt),
  [mapa.jpg](./AlatorreOctavio/mapa.jpg),
  [conclusion.txt](./AlatorreOctavio/conclusion.txt)
* **Calificación:** 10
* **Comentarios:** Me gusta tu desarrollo, y me gusta que "aterrices"
  todo a un ámbito que se nota claramente que te apasiona, el de los
  videojuegos. Los videojuegos han sido de muchas maneras y en muchas
  ocasiones motores de desarrollo del cómputo; me permito invitarte a
  leer
  [un articulito que escribí al respecto](https://sg.com.mx/revista/los-juegos-clave-para-el-desarrollo-del-c%C3%B3mputo)
  hace algunos años en la revista _Software Gurú_.
  
  Y es aquí donde debo hacerte una pequeña corrección: Los
  desarrolladores de juegos _sí_ desarrollan al más bajo nivel, pues
  requieren aprovechar detalles de arquitectura del hardware. Claro,
  típicamente el desarrollo va en varias capas, y casi todos los
  juegos actuales están en realidad construidos sobre _motores_
  (engines) específicos; los motores sirven de pegamento, dándole al
  desarrollador _final_ una interfaz más sencilla, a la vez que
  eficientan el manejo de los recursos más intensivos.

### Isaac Cruz
* **Archivos:** [Mapa.jpg](./CruzIsaac/Mapa.jpg), [Tarea2.pdf](./CruzIsaac/Tarea2.pdf)
* **Calificación:** 10
* **Comentarios:** Me da gusto que te haya resultado de utilidad /
  interés el texto. Como les he dicho en clase, soy de la idea que no
  podemos quedarnos con un único punto de vista o con definiciones
  dogmáticas respecto dónde están los límites que necesariamente se
  ajustan al punto de vista de cada autor.

### Iván Hernández
* **Archivo:** [tarea2SO.docx](./HernandezIvan/tarea2SO.docx)
* **Calificación:** 10
* **Comentarios:** Un poco escueto, pero cumples con lo que
  menciono. Como les dije, desafortunadamente este artículo toca
  varios temas que no hemos visto. Me gusta que te llamara la atención
  la importancia de los grandes _cachés_ y la hipótesis del conjunto
  activo (_working set hypothesis_), tendremos que platicar al
  respecto... En cosa de un mes :-]

### Servando López
* **Archivo:** [No existe tal cosa como un procesador de propósito general.pdf](./LopezFernandezServandoMiguel/No existe tal cosa como un procesador de propósito general.pdf)
* **Calificación:** 10
* **Comentarios:** Haces un buen análisis con lo que mencionas del
  procesador gráfico. Ahora bien, estamos ya acostumbrados a que los
  gráficos sean procesados por procesadores dedicados, pero esto no
  siempre fue el caso — Hace unos 10 o 15 años todavía era común que
  la _memoria de video_ fuera meramente un _frame buffer_: la
  representación, bit a bit, de lo que estaba mostrándose en pantalla;
  obviamente, para esta representación, basta una fracción de lo que
  hoy tiene cualquier tarjeta de video (digamos, con una pantalla de
  1280×1024 y a 32 bits de color, requieres únicamente de 1280 × 1024
  × 32 / 8 = 5MB. ¿Cómo se explica que las tarjetas de video tengan
  decenas o cientos de veces la memoria? Sencillamente, porque tienen
  que procesar. No entro en detalles :-)
  
  Casi cualquier computadora actual, si no tienes el controlador que
  maneje a su GPU, puede también _exponer_ la memoria de video
  mediante un _frame buffer_. Es un modo de video a veces
  ridículamente lento, y podemos verlo por ejemplo en las placas ARM
  tipo Raspberry Pi y similares.
  
  El video, al igual que muchas otras cosas, podría seguirse
  controlando desde el procesador central; hace 30 años, no cualquiera
  tenía un _coprocesador matemático_, y nuestras computadoras eran
  ridículamente lentas (comparativamente) para hacer cálculos de punto
  flotante... Pero esto cambió hacia los 1990s. El soporte al punto
  flotante hoy es parte de prácticamente cualquier procesador... Sin
  embargo, para muchos casos resulta más conveniente (e incluso
  económico) en muchos casos crearle hardware dedicado y
  especializado.

### Jesús Rivera
* **Archivo:** [Tarea 2.pdf](./RiveraJesus/Tarea 2.pdf)
* **Calificación:** 10
* **Comentarios:** Me gusta el mapa conceptual que presentas; simple y
  claro, si bien enfocado en uno sólo de los aspectos del artículo.
  
  Me gusta también que critiques al punto de vista que les planteo: Es
  muy importante no _creerse_ cualquier idea sólamente por estar
  publicada. Yo sí soy de la idea que _existen_ los procesadores de
  propósito general, sin embargo (y como lo he comentado a algunos de
  tus compañeros acá mismo, o lo he mencionado en clase), ha surgido
  la necesidad de dotar a una computadora de una amplia gama de
  _procesadores específicos_ — Mencionas que sólo se refiere a GPUs y
  FPGAs; los FPGAs se emplean (hasta donde entiendo) en la fase de
  prototipado; ya al entrar a producción, se _queman_ a chips de
  propósito fijo. Pero considera el controlador que lleva cualquier
  medio de almacenamiento (desde un disco duro o SSD hasta la más
  baratita de las memorias USB que se te ocurra), la tarjeta de red,
  etcétera — Permiten economizar el tiempo dedicado a la computación
  "de primera" (el CPU central), delegando las tareas "aburridas" en
  procesadores dedicados, muchos de ellos mucho sencillos que el CPU,
  algunos de ellos no tanto.

### Afferny Ramírez
* **Archivo:** [tarea2.jpg](./RamirezAfferny/tarea2.jpg)
* **Calificación:** ?
* **Comentarios:** Enviaste un archivo incorrecto :-P

## Entregas extemporáneas (07.03.2017 < _t_ ≤ 14.03.2017)

### Julio Rodríguez
* **Archivo:** [TAREA2.odt](./RodriguezJulio/TAREA2.odt), [Tarea2.png](./RodriguezJulio/Tarea2.png)
* **Calificación:** 8 × 0.8 = 6.4
* **Comentarios:** No seguiste las indicaciones de entrega (antes /
  lectura / después), me habría gustado ver tu percepción comparada
  como en el caso de tus compañeros :-(

  Tu segundo y tercer párrafo se contradicen directamente: ¿Cómo es
  que en general las personas adquieren equipos de propósito general,
  si es muy dificil que éstos existan?

  ¿Cuál es tu opinión sobre la lectura?

  Me gustó mucho tu mapa conceptual.

### Antonio Schwuchow
* **Archivo:** [T2.txt](./SchwuchowAntonio/T2.txt)
* **Calificación:** 8 × 0.8 = 6.4
* **Comentarios:** ¿No hay mapa conceptual? :-(

  El texto se ve escrito muy a las apuradas; tienes varios _dedazos_
  no corregidos, y dificulta la lectura.

  Me gustan tus conclusiones; como le comenté a alguno de tus
  compañeros, se vale perfectamente decir _no me gusta la opinión de
  un autor_. No pierdas el espíritu crítico, por más técnico que sea
  el ámbito de aplicación.

## Entregas _muy_ extemporáneas (14.03.2017 < _t_ ≤ 28.03.2017)

## Pasado el 28.03.2017, *no se recibe la tarea*
