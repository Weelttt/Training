
Eleccion_Usuario = int(input('Hola, Que tipo de moneda desea convertir? \n1.Pesos Chilenos \n2.Soles Peruanos \n3.Reales Brasileños\n Seleccione una opción:'))

Valor_dolar = 1

Pesos_valor =  924.5
Soles_valor =  3.39 
Reales_valor =  5.11 


if Eleccion_Usuario == 1:
    PesosUsuario = int(input('Cuanto tienes en pesos?'))
    Conversion_pesos = PesosUsuario / Pesos_valor * Valor_dolar
    print("Tus dolares actuales son:", f"{Conversion_pesos:.2f}", "USD")
    
elif Eleccion_Usuario == 2:
    SolesUsuario = int(input('Cuanto tienes en soles?'))
    Conversion_soles = SolesUsuario / Soles_valor * Valor_dolar
    print("Tus dolares actuales son:", f"{Conversion_soles:.2f}","USD")

elif Eleccion_Usuario ==3:
    RealesUsuario = int(input('cuanto tienes en reales?'))
    Conversion_reales = RealesUsuario / Reales_valor * Valor_dolar
    print("Tus dolares actuales son:", f"{Conversion_reales:.2f}","USD")






