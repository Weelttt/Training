while True:
    Eleccion_usuario = int(input("Que desea hacer? \n1.Convertir Fahrenheit a Celcius \n2.Convertir Celcius a Fahrenheit \n3.Cerrar programa\n"))

    if Eleccion_usuario == 1:
        Grados_F = float(input("Cuantos grados Fahrenheit desea convertir?\n"))
        Grados_C = (Grados_F - 32) * 5 / 9
        print("Sus Grados Fahrenheit son:", f"{Grados_C:.1f}\n", "° Grados celcius.")

    elif Eleccion_usuario == 2:
        Grados_C = float(input("Cuantos grados Celcius desea convertir?\n"))
        Grados_F = (Grados_C /5 *9) + 32 
        print("Sus Grados Celcius son:", f"{Grados_F:.1f}\n", "° Grados Fahrenheit.")

    elif Eleccion_usuario == 3:
        print("Gracias por usar.\n")
        break
    else:
        print("Por favor elija una de las opciones indicadas.\n")
