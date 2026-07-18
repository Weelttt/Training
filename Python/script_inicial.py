

Valor_dolar = 1

Pesos_valor =  924.5
Soles_valor =  3.39 
Reales_valor =  5.11 

condicion = 1, 2, 3

while condicion :

    Eleccion_Usuario = int(input('Hola, Que tipo de moneda desea convertir? \n1.Pesos Chilenos \n2.Soles Peruanos \n3.Reales Brasileños\n4.Cerrar Programa \nSeleccione una opción:'))

    if Eleccion_Usuario == 1:
        PesosUsuario = int(input('Cuanto tienes en pesos? \n'))
        Conversion_pesos = PesosUsuario / Pesos_valor * Valor_dolar
        print("Tus dolares actuales son:", f"{Conversion_pesos:.2f}", "USD \n")
    
    elif Eleccion_Usuario == 2:
        SolesUsuario = int(input('Cuanto tienes en soles? \n'))
        Conversion_soles = SolesUsuario / Soles_valor * Valor_dolar
        print("Tus dolares actuales son:", f"{Conversion_soles:.2f}","USD \n")

    elif Eleccion_Usuario ==3:
        RealesUsuario = int(input('cuanto tienes en reales? \n'))
        Conversion_reales = RealesUsuario / Reales_valor * Valor_dolar
        print("Tus dolares actuales son:", f"{Conversion_reales:.2f}","USD \n")
    
    elif Eleccion_Usuario == 4:
        print("Gracias Por usar.")
        break


    else:
        print("Por favor elija una opcion valida")

         






