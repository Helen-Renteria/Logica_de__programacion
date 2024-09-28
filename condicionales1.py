
while True: 

    rango_v= range(0, 101)


    print("-------BIENVENIDO-------")
    puntaje = int(input("Ingrese su calificacion para saber si aprobo: "))

    if puntaje in rango_v:
        print(f"El número {puntaje} es válido.")
        if puntaje >= 90: 
            print("Su calificacion es excelente.")
            print("APROBADO")

        elif puntaje >=75:
            print("Su calificacion es buena")
            print("APROBADO")
        elif puntaje >=50:
            print("Su calificacion es regular")
            print("APROBADO")
        else:
            print("A REPROBADO :(")

    else:
        print("El número no es válido. Debe estar entre 0 y 100.")


    continuar = input("desea continuar")
    if continuar.lower() != "s":
        break 

# que el usuario no puede escribir mas de 100

