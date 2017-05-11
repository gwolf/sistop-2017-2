Después de releer varias veces el artículo, encuentro varias maneras de abordar
el tema, pero dos ellas me parecen más interesantes por lo contrarias que pueden
ser.

Primero, el punto de vista del autor, que no existe tal cosa como un procesador
de propósito general, porque ningún procesador puede ser bueno ejecutando todos
los algoritmos habidos y por haber. Y creer existe tal cosa es dañino por que
lleva al diseño de pequeñas piezas de silicon que terminan siendo malas para más
cosas que aquellas para las que son buenas; por que creer que existe tal cosa
como un procesador de propósito general lleva a hacer asumpciones sobre los
algoritmos que ejecuta que ya no son ciertos en la actualidad, y esto termina
limitando los algoritmos que se ejecutan sobre ellos.

Por otro lado también podemos plantear el caso contrario.

¿Es realmente culpa del procesador no ser bueno con los algoritmos más modenos?
La forma de programar a cambiado bastante en los ultimos años (para bien o para
mal). Ahora la gran mayoría de los lenguajes de programación actual son
interpretados (algunos de una forma elegante, otros de una forma tradicional) y
añaden varias abstracciones (o complejidad escondida) a la solución de problemas.

Tomemos el ejemplo del autor, una suma en un lenguaje de programación actual.
Esta suma en un lenguaje de alto nivel moderno, requerirá determinar el tipo de
dato de ambos operandos, determinar si es un tipo de valor de esos raros como
_undefined_ o _null_ o _infinito_, suponiendo que no lo son, abrá de buscar
por la rutina correcta para la suma de esos tipos de datos, verificar que con
valores actuales es posible la suma, si es seguro sumar, tenemos derecho de
sumar esas variables, etc. finalmente ejecutar la operacion, posiblemente
crear objeto, variable o lo que sea para guardar el resultado, etc. Si añadimos
a esto todas las llamadas que al sistema que esto requerirá, resulta que para
ejecutar esa operación, al menos abrán sido necesarias muchas bifurcaciones en
el fujo del procesador, este nivel de abstracción es completamente desconocido
para el procesador, y no le podemos exigir que prediga correctamente a nuestro
programa.

La forma de programar ha cambiado, sin embargo, las bases de la computación no
paracen cambiar demasiado, nuestras computadoras siguen entendiendo unicamente
unos y ceros. Y la programación actual ha olvidado eso. Se ha incorporado capa
tras capa de abstracción a la computación para hacer más fácil la vida al que
programa, pero se ha hecho un infierno la vida del que diseña el procesador.

Y siendo sinceros, ¿es necesario ese nivel de abstraccion? ¿necesitamos
realmente que cada entero de nuestro programa sea un objeto? ¿estos niveles de
abstracción nos permiten resolver problemas más rápido o son muestra de nuestra
incomprensión de los problemas? ¿hasta qué punto son sanas estas abstracciones?
¿por qué hago tantas preguntas?

En estos tiempos es fácil aprender a programar, pero no sé de muchas personas
que hayan aprendido de diseño digital por su propia cuenta, hayan diseñado un
procesador y se hayan vuelto ricos. Por que es más fácil crear una nueva capa de
abstracciónsobre algo que ya existe, a crear el circuito que tranforme esa capa
de abtraccion en algo tangible.

No existe tal cosa como un procesador de propósito general, por que ningún
procesador tiene la capacidad de entender los niveles de abstracciones (o
complejidad innecesaria!) que se le exiguen actualmente, y la creeencia de que
existe tal es dañina por que eso ha hecho que añadamos más y más capas de
abstracciones a cosas que prodríamos hacer de forma más simple (como sumar...
declarando previamente los tipos), creyendo firmemente que el procesador sabrá
resolverlas.
