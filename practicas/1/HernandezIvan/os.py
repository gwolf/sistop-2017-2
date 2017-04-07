import os   
sistemaop = os.name 

file= open("so.txt","w")
file.write("El sistema operativo de esta computadora es : {}".format(sistemaop))
file.close()

###fuente https://www.cambiadeso.es/entradas/python-tipcomo-saber-el-sistema-operativo-usando-python/###