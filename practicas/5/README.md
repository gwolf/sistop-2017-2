# Recorriendo un sistema de archivos

## Contexto

Vimos en clase las principales operaciones que se pueden realizar con
un _archivo_ — Abrir, cerrar, leer, escribir, reposicionar (`open(),
close(), read(), write(), seek()`), todas ellas _relativas_ a un
descriptor de archivo (_file descriptor_).

Discutimos que el manejo de archivos es, a fin de cuentas, equiparable
con _programación orientado a objetos_, porque es manipulación de
_tipos de datos abstractos_ (un _archivo_ no existe propiamente, es
una convención que se usa para aprovechar el espacio que ofrece un
dispositivo _orientado a bloques_).

Revisamos también, al hablar de _organización de archivos_, el
concepto de _directorios jerárquicos_. Para hablar de directorios,
empleamos otra serie de operaciones similares a las de los archivos —
Abrir, cerrar, leer, renombrar, eliminar, reposicionar (`opendir(),
readdir(), closedir(), rename(), remove(), rewinddir()`). Les mostré
un pequeño ejemplo de un programa que muestra el contenido de un
directorio
([página 246-247 del libro](http://sistop.org/pdf/sistemas_operativos.pdf#page=246)).

## Tu misión

Quiero que hagan un programa que _recorra_ un árbol de directorios, a
tres niveles de profundidad. Pueden basarse en el código
referido.

¿Cuál es el reto?

Sobre el código que les presenté, van a tener que identificar el
_tipo_ de cada uno de los archivos. La función `opendir()` únicamente
funciona con directorios, no puede abrir archivos. ¿Cómo pueden
averiguar cuáles son archivos y cuáles no? ¿Qué otros tipos de archivo
pueden encontrar? ¿Tienen idea cómo podrían manejarlos?

Como _tip_ directo para resolver esto, revisen la función `stat()`;
pueden encontrarlo referido en
[su página de manual](http://man7.org/linux/man-pages/man2/stat.2.html#DESCRIPTION)
(`man 2 stat`), y más específicamente, en
[sus ejemplos](http://man7.org/linux/man-pages/man2/stat.2.html#EXAMPLE).

## Entregas

Tienen una semana para desarrollar este ejercicio. La calificación
será de 10 si cumple con el planteamiento y está desarrollado en C, de
8 si cumple con el planteamiento y está desarrollado en otro lenguaje
más _fácil_, y de 6 si no lograron cumplir el planteamiento, pero
hicieron un avance, llamémosle... _interesante_ ;-)

La fecha de entrega _en tiempo_ es el 16 de mayo; una semana pasada
ésta, se califica sobre 8. Después del 23 de mayo, se califica
sobre 5. **El 25 de mayo se cierra toda entrega** (fin de semestre).
