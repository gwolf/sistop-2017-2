Tarea 3: Ejercicios de sincronización
===================

**Realizada por:**
Isaac Cruz Santos
Afferny Ramirez Canales

Descripción
-------------
Elegimos el problema del cruce del rió entre Serfs y Hackers, para la resolución del problema realizamos un script en Python.

> **Primitivas de sincronizan usadas:**

> - **Mutex:** Usamos dos mutex para proteger las zonas criticas del código como variables que necesitaban ser leídas y modificadas. Para esto usamos dos semaforos inicializados en uno: **mutex** y **mutexBalsa**.
> - **Barrera**: Usamos una barrera a modo de fila que nos sirvió para contener a los hilos,creando filas de 3 hilos hasta que el cuarto llegara y abordara.

>**Modulos de Python usados:**
>>-   **Threading:** de Threading importamos *Semaphore* para hacer uso de los semáforos y usarlos como mutex y barrera y *Thread* para trabajar con hilos.
>- **Time:** de time importamos *sleep* para hacer un pequeño retraso en la ejecución del programa cuando la balsa avanzara.



Referencias:
>*Gunnar Wolf*, Fundamentos de Sistemas Operativos
>*Allan B. Downey*, The Little Book Of Semaphores

