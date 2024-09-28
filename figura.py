while True:
    num = int(input(" ingrese el tamano del que desea que sea su triangulo: "))
    for i in range(num):
        print("  " * (num- i - 1) + "**" * (2 * i + 1))


    continuar = input("¿Desea continuar s/n?")
    if continuar.lower() != "s":
        break 







