import platform
info = platform.processor()
file = open("procesador.txt","w")
file.write("Información de su procesador: {}".format(info))
file.close()
