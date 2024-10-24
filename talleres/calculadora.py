"""
Hacer un algoritmo en python que permita realizar dos procesos uno es elevar al cuadrado todos 
los números menores al número que ingreso y que nos muestre la tabla de multiplicar de este mismo.
El usuario puede decidir si hacer 1 o los 2 procesos. (el numero tiene que ser entre 1 y 10 con
estos incluidos) ."""
while True:
    num= int(input("Ingrese el numero con el que desea realizar la operacion (entre 1 y 10): "))

    if num >= 1 and num <=12:
        print("que operacion desea realizar")
        print("1. tabla de multiplicar")
        print("2. numeros elevados ")
        print("3.ambos")
        opc = int(input("ingrese el numero de la opcion: "))
        if opc == 1:
            print("TABLA DE MULTIPLICAR")
            for c in range(1,11):
                print(num, "x", c , "=", (num*c))
        
        elif opc == 2: 
            print("TABLA DE MULTIPLICAR")
            for c in range (num ):
                elevado= c**2
                print(c, "^", "2","=", elevado)
                
        elif opc ==3:
            print("TABLA DE MULTIPLICAR")
            for c in range(1,11):
                print(num, "x", c , "=", (num*c))

            print("NUMEROS ELEVADOS AL CUADRADO")
            for c in range (num):
                elevado= c**2
                print(c, "^", "2" , elevado)


    
    
    else:
        print("EL dato que ingrso no es valido. ")

    continuar= input("desea continuar s/n ")
    if continuar.lower() != "s":
        break

 