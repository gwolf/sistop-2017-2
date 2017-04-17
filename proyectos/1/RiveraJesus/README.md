## Monitor Sistema Operativo

Primer proyecto de Sistemas Operativos. Se desarrollo un monitor de recurso del sistema operativo, con la ayuda de la biblioteca psutil 5.2.2, tkinter para la ventana, utilizando python3.6 en windows y python3.5 en linux.
También fue de apoyo el ejemplo 11 incluido en esta [web.](http://www.programcreek.com/python/example/53869/psutil.process_iter)

## Installación / Ejecución

Para su correcta ejecución es necesario tener instaladas las bibliotecas psutil 5.2.2 y tkinter.
La instalacón de psutil para python 3 se puede hacer a través del siguiente comando en el terminal de linux o windows:
```{r, engine='bash', count_lines}
python3 -m pip install psutil
```
Para la instalación de tkinter en linux: 
```{r, engine='bash', count_lines}
sudo apt-get install python3-tk
```
En windows se intala por defevto al realizar nuestra instalación de python.

La ejecución en linux es por medio del directorio del proyeto en terminal y escribimos:
```{r, engine='bash', count_lines}
python3 monitor.py
```
La ejecución en windows es por medio del directorio del proyeto en terminal y escribimos:
```{r, engine='bash', count_lines}
python monitor.py
```

## Bugs

A falta de conocimiento se actualiza el treeview limpiando por completo el mismo, esto hace un poco molesto el ordenamiento.
