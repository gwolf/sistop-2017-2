# Calificación de la tarea 3 (ejercicios de concurrencia)

## Entregas en tiempo (_t_ ≤ 21.03.2017)

### Isaac Cruz y Afferny Ramírez
* **Archivos:**
  []()
* **Calificación:**
* **Comentarios:**

### Iván Hernández
* **Archivos:**
  []()
* **Calificación:**
* **Comentarios:**

### Servando López
* **Archivos:**
  [desa.py](./LopezFernandezServandoMiguel/desa.py)
  [desa_version2.py](./LopezFernandezServandoMiguel/desa_version2.py)
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
* **Archivos:**
  []()
* **Calificación:**
* **Comentarios:**

## Entregas extemporáneas (21.03.2017 < _t_ ≤ 28.03.2017)

## Entregas _muy_ extemporáneas (28.03.2017 < _t_ ≤ 11.04.2017)

## Pasado el 11.04.2017 *no se recibe la tarea*
