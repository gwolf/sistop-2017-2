# Práctica 3: Ramas paralelas de desarrollo

    Práctica creada el 23.02.2017
	Entrega en tiempo: Jueves 02.03.2017

Como era de esperarse, ya ha ocurrido con varios de ustedes que envían
un *pull request* incluyen una práctica y una tarea, y si no nos
cuidamos, pronto enviarán incluso su proyecto de desarrollo o
exposición en distintos estados de desarrollo.

Una de las ventajas que da Git al desarrollo es que nos permite abrir
*ramas temáticas* (en inglés normalmente se les llama *feature
branches*), atendiendo a problemáticas específicas.

Vamos a partir de los siguientes supuestos:

- Un *pull request* debe ir únicamente sobre un problema o sugerencia
  específico.
- Pueden desarrollar dos líneas de pensamiento distintas de forma
  simultánea, pero separada empleando *ramas*
- Una característica fundamental de Git es la preservación de la
  *historia*; si hay algún archivo que subieron al repositorio y le
  dieron `git rm`, sólo se borrará de las versiones nuevas, pero seguirá
  siempre como parte de la historia; (la historia de *commits* se
  mantiene entera.

¿Cómo procedemos entonces?

Supongamos que tienen que entregar, en la misma semana, la práctica
3-A y la práctica 3-B. El contenido de cada una de estas prácticas es
trivial, basta que generen un archivo con su nombre para cada uno de
ellos. El contenido que decidan darle no es muy relevante para esta
práctica.

## Creación de dos ramas

1. Para crear nuestras ramas vamos a usar el comando `git branch`. La
   rama sobre la cual trabajamos por omisión se llama `master`. Vamos a
   crear una rama llamado `practica3a`, y otra llamada
   `practica3b`. Desde el directorio base de nuestro repositorio:


        $ git branch practica3a
        $ git branch practica3b

2. En este momento, `master`, `practica3a` y `practica3b` apuntan al
   mismo *objeto*, al mismo punto en la historia de nuestro
   proyecto. Y, a pesar de haber creado las dos ramas, la rama activa
   sigue siendo `master`. Vamos a seleccionar, con `checkout`, la
   práctica 3A, y crear un archivo dentro de ésta. Por ejemplo, para
   obtener la fecha del sistema y guardarla en un archivo:

		$ git checkout practica3a
		$ date > practicas/3/GunnarWolf/A/hora_actual.txt

   El comando `git checkout` tiene por efecto que el _punto actual de
   trabajo_ en el repositorio sea el que le indicamos; podemos
   especificar para el `checkout` el nombre de una rama o el
   identificador de un `commit` cualquiera — Volveremos a esto más
   adelante.

3. Como ya sabemos, agrego el archivo y hago mi *commit*:

		$ git add practicas/3/GunnarWolf/A/hora_actual.txt
		$ git commit -m 'Agrego el archivo de Gunnar Wolf para la práctica 3A'

4. Ahora, vamos a la rama de la práctica 3B:

		$ git checkout practica3b

	Puedes verificar que tu archivo en el directorio de 3A no
    existe. ¡No te preocupes, no se ha perdido!

		$ ls practicas/3/GunnarWolf/A/hora_actual.txt
		ls: cannot access practicas/3/GunnarWolf/A/hora_actual.txt: No such file or directory

	Ahora, generemos un archivo ejemplo. Puede ser cualquier cosa, en
	este caso (desde un sistema Linux) puede ser la información de tu
	CPU, según la presenta el sistema operativo (claro, el archivo
	`/proc/cpuinfo` sólo existe en Linux; ponle cualquier contenido
	que elijas en caso de estar usando otro sistema):

	    $ cp /proc/cpuinfo practicas/3/GunnarWolf/B/cpuinfo.txt
		$ git add practicas/3/GunnarWolf/B/cpuinfo.txt
		$ git commit -m 'Agrego el archivo de Gunnar Wolf para la práctica 3B'

5. Enviamos los cambios a GitHub. Dado que éstos no están en la rama
   `master`, hay que indicar expresamente sobre qué rama trabajamos:

		$ git push origin practica3a
		$ git push origin practica3b

    Ya con eso, y dado que son dos ideas distintas e independientes,
    abrimos *dos pull requests*, uno desde cada una de estas ramas.

	¡Recuerda volver a tu rama `master` para seguir trabajando
    normalmente!

		$ git checkout master

6. Posteriormente, puedes incorporar estos cambios a tu rama `master`:

		$ git merge practica3a
		$ git merge practica3b

	Podríamos también *no* incorporarlos; en realidad depende de la
    naturaleza del proyecto en que estemos trabajando. Para nuestras
    prácticas, te sugiero que sí hagas el merge.

	Ojo, si estás desarrollando un trabajo mayor (digamos, el proyecto
    de unidad o la exposición) y tu rama `master` ha avanzado
    sensiblemente, puedes querer sincronizar *al revés*: Sincronizar
    tu rama con `master`, para que no crezca demasiado la
    distancia. Esto es,

		$ git checkout proyecto
		$ git merge master

	Claro está, una vez que tu proyecto esté listo para ser entregado,
    sincroniza master, envía al servidor:

		$ git checkout master
		$ git merge proyecto
		$ git push

    Y no olvides notifícarme por medio de un *pull request*.
