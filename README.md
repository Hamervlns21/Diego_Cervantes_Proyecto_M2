# Diego_Cervantes_Proyecto_M2
En este proyecto se estan realizando dos codigos, en el primero se estar realizando un programa donde podamos identificar la longitud de una palabra ingresada donde debe indicar que esta dentro de un rango de 4 a 8 letras. El segundo programa se genero para identificar en que cuadrante se encuentran las coordenadas y ninguna sea 0.


# Identificar_la_longitud_de_una_palabra_ingresada


palabra = input("ingrese una palabra: ")                                                           Se estan asignando las variables "palabra" y "longitud",
longitud = len(palabra)

if 4 <= longitud <= 8:                                                                             Se agrega la condición if, para validar si se cumple con la longitud
    print("la palabra es correcta")

elif longitud < 4:                                                                                 Se agrega la condición elif si es que no se cumple con la sentencia anterior
    print("hacen falta letras. solo tiene {} letras " .format(longitud))

else:                                                                                              Se agrega la condición else para demostrar que no se cumplio con ninguna de las condiciones anteriores
    print("sobran letras. tiene {} letras. " .format(longitud))




    # Identificar en que cuadrante se localiza el punto dados sus coordenadas (x, y).

while True:                                                                                Se agrega la sentencia while.True para que cumpla con la condición
    x = int(input("ingrese la coordenada x: "))                                            Se asignan las variables de los ejes pertenecientes
    y = int(input("ingrese la coordenada y: "))

    if x == 0 or y == 0:                                                                  Se agrega la sentencia if para validar que las variables cumplan con la condición
        print("el origen de las coordenadas es cero, intentar nuevamente")
    else:                                                                                 Se agrega la sentencia else para demostrar que no se cumplio con la condición anterior
        break                                                                             Se agrega el break para romper el bucle del if


if x > 0 and y > 0:                                                                       Se agrega la sentencia if para demostrar que se cumple con la condición
    print("El punto se encuentra en el cuadrante I")

elif x < 0 and y > 0:                                                                     Se agrega la sentencia elif para demostrar que no se cumple con la primera condición
    print("El punto se encuentra en el cuadrante II")

elif x < 0 and y < 0:                                                                     Se agrega otra sentencia elif para demostrar que no se cumple con la primera ni segunda condición
    print("El punto se encuentra en el cuadrante III")

else:                                                                                     Se agrega la sentencia else para demostrar que no se cumplió con la primera, segunda y tercera condición
    print("El punto se encuentra en el cuadrante IV")



                                                                      La reflexión que me ha dejado la segunda parte de este bootcamp, es como aprender a utilizar una mejor estructura, tener una mejor 
                                                                      logica pero sobre todo a tener mayor conocimiento sobre las listas.
