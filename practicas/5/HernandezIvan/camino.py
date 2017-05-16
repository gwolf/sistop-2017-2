from os import walk
from colorama import init, Fore, Back, Style
init()


for (path, directorio, archivos) in walk("."):
	#Lo primero es leer el path, ver donde se esta"""
    print(Fore.RED + Style.BRIGHT + "PATH")
    print(Style.RESET_ALL)
    print (Fore.RED)
    print path 
    print(Style.RESET_ALL)
    """Leer los directorios o directorio"""
    print(Fore.GREEN + Style.BRIGHT + "directorio")
    print(Style.RESET_ALL)
    print (Fore.GREEN)
    print directorio
    print ("\n")
    print(Style.RESET_ALL)
    """Ver los archivos dentro de los directorios"""
    print(Fore.BLUE + Style.BRIGHT + "ARCHIVOS")
    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print archivos
    print ("\n")


# Referencias http://www.alvarohurtado.es/leer-carpetas-y-archivos-con-python/