tareas_usuario = []

while True:
    eleccion_usuario = int(input(
        "\nBienvenido, Por favor seleccione una opcion: \n \n1.Ver Tareas" \
        "\n2.Agregar Tarea \n3.Eliminar Tarea \n4.Salir\n \n"
    ))

    if eleccion_usuario == 1:
        if len(tareas_usuario) == 0:
            input("No hay tareas guardadas \nPresione Enter para volver al menu Principal")
        else:
            for indice, tarea in enumerate(tareas_usuario, start=1):
             print("\n", indice, tarea)
            input("\nPresione Enter para volver al menu Principal")

    elif eleccion_usuario == 2:
        tareas_usuario.append(input("\nAgregue su tarea:"))
    elif eleccion_usuario == 3:
        print()
    elif eleccion_usuario == 4:
        print()
        break
    else:
        print("\nPor favor seleccione una opcion correcta")