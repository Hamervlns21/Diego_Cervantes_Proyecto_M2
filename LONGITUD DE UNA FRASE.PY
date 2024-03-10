# Identificar_la_longitud_de_una_palabra_ingresada

palabra = input("ingrese una palabra: ")
longitud = len(palabra)

if 4 <= longitud <= 8:
    print("la palabra es correcta")

elif longitud < 4:
    print("hacen falta letras. solo tiene {} letras " .format(longitud))

else:
    print("sobran letras. tiene {} letras. " .format(longitud))