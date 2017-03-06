#Script que genera archivo indicando el numero de procesadores en la computadora

import multiprocessing 

noCpus=multiprocessing.cpu_count()
file= open("infoCpu.txt","w")
file.write("El numero de procesadores en esta computadora es de: {}".format(noCpus))
file.close()
