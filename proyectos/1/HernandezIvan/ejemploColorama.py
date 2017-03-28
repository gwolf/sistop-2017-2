from colorama import init, Fore, Back, Style

# Para restablecer colores después de cada impresión inicializar 
# el módulo con init(autoreset=True) en lugar de init().

init()
print(Fore.RED+"Texto color rojo")
print(Back.WHITE+"Texto color rojo sobre fondo blanco")
print(Back.WHITE+Style.BRIGHT+"Txt rojo brill.s/blanco"+Back.RESET)
print(Style.RESET_ALL + "Texto con valores por defecto")
print(Fore.WHITE+Back.BLUE+"Texto blanco sobre azul"+Back.RESET)
print("Texto blanco sobre fondo negro")

# Niveles de intensidad

print(Style.DIM + Fore.WHITE + "Intensidad baja")
print(Style.NORMAL + "Intensidad normal")
print(Style.BRIGHT + "Intensidad alta")