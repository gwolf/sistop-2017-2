# Calificación de la tarea 3 (ejercicios de concurrencia)

## Entregas en tiempo (_t_ ≤ 21.03.2017)

### Isaac Cruz y Afferny Ramírez
* **Problema a resolver:** El cruce del río
* **Archivos:**
  [CruceRio.py](./CruzIsaacRamirezAfferny/CruceRio.py),
  [CruceRioDoc.md](./CruzIsaacRamirezAfferny/CruceRioDoc.md)
* **Lenguaje:** Python
* **Calificación:** 10
* **Comentarios:** 
  * Solución limpia y fácil de comprender; el nivel de comentarios en
    el código es justo y ayuda bien a la comprensión. ¡Bien!
      * Ojo, Isaac: El comentario en la línea 46 parece haber llegado
        para quitarte méritos ;-)
  * Emplearon la bibliografía y tal vez tomaron parte de su lógica,
    pero se ve que la implementación es propia. ¡Muy bien!
  * La ejecución es limpia y correcta; llama mi atención que generan
    un escenario asimétrico (48 desarrolladores, 32 linuxeros y 16
    windowseros). Todo bien, sólo es curioso ver el balance de fuerzas
    ;-)

### Iván Hernández
* **Problema a resolver:** Gatos y ratones
* **Archivos:**
  [gatos.rb](./HernandezIvan/gatos.rb),
  [documentoGatos.txt](./HernandezIvan/documentoGatos.txt),
* **Lenguaje:** Ruby
* **Calificación:** 5
* **Comentarios:**
    * Lo que envías es un acercamiento a cómo sincronizar a cien gatos
      para que sólo uno coma a la vez (y no el problema planteado)
    * Generas a los 100 gatos como hilos independientes... Pero _no se
      mantienen vivos_ como hilos
        * Cada instancia de `Gato` se limita a imprimir dos líneas de
          texto, y termina
        * No instancias ningún objeto de la clase `Platos`, y sólo uno
          de la clase `Raton`; tu `Raton` no llega siquiera a imprimir
          una línea en pantalla porque el hilo principal termina
          inmediatamente tras haberlo creado (recuerda que Ruby
          termina la ejecución al terminar la del hilo principal)
        * La documentación... Está escrita a las carreras, explica
          sólo la _intención_ de solución, pero no se refleja en el código

### Servando López
* **Problema a resolver:** El cruce del río
* **Archivos:**
  [desa.py](./LopezFernandezServandoMiguel/desa.py),
  [desa_version2.py](./LopezFernandezServandoMiguel/desa_version2.py)
* **Lenguaje:** Python
* **Calificación:** 7.5
* **Comentarios:**
  * Haces un buen trabajo de control de acciones basado en cómo van
    ocurriendo los eventos, cómo se van alternando los hilos. ¡Bien!
  * Sin embargo... Hay errores en tu lógica. Esto me pasó varias
    veces:

		Esperando tripulantes.....

		Cruzando!Nombre : Isaac Cruz  desarrollo en Windows
		Nombre : Ivan Hernandez  desarrollo en Windows
		Nombre : Julio Rodriguez  desarrollo en Linux

		Nombre : Ricardo Hernandez  desarrollo en Windows

		Arribo
		Bajo : Nombre : Eduardo Stevens  desarrollo en Windows   , Bajo : Nombre : Ivan Hernandez  desarrollo en Windows   , Bajo : Nombre : Ricardo Hernandez  desarrollo en Windows   , Bajo : Nombre : Isaac Cruz  desarrollo en Windows   , 
		Regreso

		Esperando tripulantes.....

		Arribo
		Nombre : Ricardo Hernandez  desarrollo en Windows
		Nombre : Jesus Pacheco  desarrollo en Windows
		Nombre : Alberto Negrete  desarrollo en Linux
		Nombre : Eduardo Stevens  desarrollo en Windows
		Bajo : Nombre : Ricardo Hernandez  desarrollo en Windows   , Bajo : Nombre : Alberto Negrete  desarrollo en Linux   , Bajo : Nombre : Jesus Pacheco  desarrollo en Windows   , Bajo : Nombre : Julio Rodriguez  desarrollo en Linux   , 

	¿Qué observamos acá? Que van subiendo en (¿aparente?)
    desorden... Pero... ¿Será que únicamente se "subieron" a las colas
    de balsas diferentes? ¿La realidad del cruce se ve únicamente en
    la línea donde dicen irse bajando? Me parece que sí.
      * _Creo_ que el error no es de lógica (revisé un par de decenas
        de ejecuciones, y la bajada está controlada correctamente),
        sino que de interfaz usuario.
  * La lógica está un poco confusa... Me costó algo de trabajo leer
    sobre todo la función `ingresan` — Pero _creo_ que es correcta.
      * ...Y parte del criterio de calificación de la tarea es una
        breve descripción / documentación de tu solución :-( ¡Es parte
        importante del desarrollo de un proyecto!
  * Me pides opinión acerca de cuál de las versiones me parece
    mejor.
      * Son muy parecidas, la diferencia es únicamente que en
        `desa.py` hay un par de llamadas a semáforo comentadas...
      * De entrada, veo que la versión `desa.py` no puede funcionar,
		pues cae en un bloqueo mutuo: En `Colas.encolar_en()`
		comentaste a `trabajando_con_cola.release()`, por lo que
		únicamente queda el `acquire()`. El primer hilo va a pasar,
		pero de ahí en más... Tenemos el semáforo permanentemente
		cerrado :-(

### Julio Rodríguez
* **Problema a resolver:** El profesor y los alumnos
* **Archivos:**
  [Tarea3-1.txt](./RodriguezJulio/Tarea3-1.txt) (documentación),
  [Tarea3.txt](./RodriguezJulio/Tarea3.txt) (código)
* **Lenguaje:** Ruby
* **Calificación:** 2.5
* **Comentarios:**
    * ¿Resolver un problema en un lenguaje que no conoces? ¡Dos
      problemas por el precio de uno!
        * Puedo asegurarte que el código no funcionó ni una vez: Copiaste
          el nombre del módulo `yaml` como `yam1`, eso no compila
            * ¿Y para qué requieres `yaml`? No tiene relación con el
              problema en cuestión
        * Las clases en Ruby _deben_ iniciar en mayúscula
        * Tienes algunos bloques `class` que no cerraste con `end`
    * Y aterrizando más a la resolución del problema, incluso si lo
      entiendo ver como pseudocódigo...
        * Los `Alumno`s no emplean ningún mecanismo de
          sincronización. Claramente, no está terminada su
          implementación (sólo saben "nacer" y tocar la puerta).
        * Veo que tienes idea _correcta_ de cómo manejar varios de los
          mecanismos que buscabas emplear... Pero no lo hiciste. ¿Te
          faltó tiempo? ¿Incluso con la extensión de dos días que te
          di? :-(
        * Nada de comentarios que me intenten explicar lo que
          intentaste aplicar
    * La documentación debe llevar un grado mínimo de
      cuidado... Documentar con faltas de ortografía, _dedazos_
      obvios, etc. desmerece al esfuerzo de crear la documentación.

## Entregas extemporáneas (21.03.2017 < _t_ ≤ 28.03.2017)

## Entregas _muy_ extemporáneas (28.03.2017 < _t_ ≤ 11.04.2017)

## Pasado el 11.04.2017 *no se recibe la tarea*
