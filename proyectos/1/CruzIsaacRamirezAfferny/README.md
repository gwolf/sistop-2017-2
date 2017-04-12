Proyecto 1: Monitor de Procesos
===================

**Realizada por:**
Isaac Cruz Santos
Afferny Ramirez Canales

Descripción
-------------
El primer proyecto consistía en la programación de un monitor de procesos. Escribimos un Script que monitorea el estado de uso de la CPU y la memoria,ademas de mostrarnos información útil sobre los últimos procesos corriendo. Usamos las primitivas de sincronizacion para mantener una actualización uniforme de los datos y la interfaz.

**Lenguaje:** Python 2.7
**Sistema Operativo:** Linux Ubuntu 16.04

> **Primitivas de sincronizan usadas:**

> - **Mutex:** Usamos un mutex para proteger una variable que actuaba como contador para implementar una barrera en la sincronización de los hilos.
> - **Barrera**: Usamos una barrera a modo sincronización entre los varios hilos generados, de tal manera que todos tuvieran una actualización en la interfaz mas o menos uniforme.

>**Modulos de Python usados:**
>-   **Threading:** de Threading importamos *Semaphore* para hacer uso de los semáforos y usarlos como mutex y barrera y *Thread* para trabajar con hilos.
>- **Psutil:** Usamos psutil para obtener datos del procesador, memoria y procesos.
>- **Curses:** Usado para generar la interfaz gráfica.
>- **Platform:** Usado para obtener algunos datos como el SO y la arquitectura utilizada.

Idea Original:
![Idea Original](https://raw.githubusercontent.com/Scr3amind/sistop-2017-2/master/proyectos/1/CruzIsaacRamirezAfferny/Idea.jpg)
Proyecto terminado:
![

> enter image description here

](http://i.imgur.com/JgbrI2E.png)
Referencias:
>*Gunnar Wolf*, Fundamentos de Sistemas Operativos
>*http://pythonhosted.org/psutil/

Repositorio donde trabajamos:
>https://github.com/Scr3amind/Proyecto-1-Sistop
>PD: La laptop de Afferny murio por lo cual no hay pull requests.