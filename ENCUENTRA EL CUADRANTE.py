# Identificar en que cuadrante se localiza el punto dados sus coordenadas (x, y).

while True:
    x = int(input("ingrese la coordenada x: "))
    y = int(input("ingrese la coordenada y: "))

    if x == 0 or y == 0:
        print("el origen de las coordenadas es cero, intentar nuevamente")
    else:
        break


if x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I")

elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II")

elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III")

else:
    print("El punto se encuentra en el cuadrante IV")