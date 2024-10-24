"""
Pagina para comprar peluches
Que tenga un mensaje que diga “BIENVENIDOS A DULCE VANIDAD”
Que el usuario pueda decidir entre 3 peluches (oso pardo, oso panda y un Stitch) están en 2
presentaciones que son grande y pequeño. El usuario puede pedir que se lo arreglen con
decoraciones y por eso se le agrega un valor adicional de 50000
Los precios son
Oso pardo pequeño =100000
Oso pardo grande= 200000
oso panda pequeño= 150000
oso panda grande= 300000
Stitch pequeño= 200000
Stitch grande= 400000 
Dependiendo de lo que el usuario decida se le muestra la factura. Y un mensaje que diga"""


print("----BIENVENIDOS A DULCE VANIDAD----")
print("peluches disponibles")
print("1. oso pardo ")
print("2. oso panda ")
print("3. Stitch ")
peluche= int (input("INGRESE EL NUMERO DEL PELUCHE QUE DESA COMPRAR: "))

if peluche == 1:
    print("En que tamano desea el peluche")
    print("1.pequeno")
    print("2.grande")
    tamano= int (input("ingrese el # del tamano que desea que sea el peluche"))

    if tamano ==1:
        Opardo_P =100000
        print (F"el valor a pagar es {Opardo_P}")
        print("Desea que le decoren el peluche : 1.si o 2.no")
        obc= int(input("ingrese el numero de la obcion que desea realizar"))
        if obc == 1:
            print(F"se a decorado el peluche, el total a pagar es {Opardo_P + 50000}")
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA")
        elif obc == 2:
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA HASTA PRONTO")

    elif tamano ==2:
        Opardo_G = 200000
        print (F"el valor a pagar es {Opardo_G}")
        print("Desea que le decoren el peluche : 1.si o 2.no")
        obc= int(input("ingrese el numero de la obcion que desea realizar"))
        if obc == 1:
            print(F"se a decorado el peluche, el total a pagar es {Opardo_G + 50000}")
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
        elif obc == 2:
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")

elif peluche == 2:
    print("En que tamano desea el peluche")
    print("1.pequeno")
    print("2.grande")
    tamano= int (input("ingrese el # del tamano que desea que sea el peluche"))
    if tamano ==1:
        Opanda_P =150000
        print (F"el valor a pagar es {Opanda_P}")
        print("Desea que le decoren el peluche : 1.si o 2.no")
        obc= int(input("ingrese el numero de la obcion que desea realizar"))
        if obc == 1:
            print(F"se a decorado el peluche, el total a pagar es {Opanda_P+ 50000}")
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
        elif obc == 2:
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
    elif tamano ==2:
        Opanda_G = 300000
        print (F"el valor a pagar es {Opanda_G}")
        print("Desea que le decoren el peluche : 1.si o 2.no")
        obc= int(input("ingrese el numero de la obcion que desea realizar"))
        if obc == 1:
            print(F"se a decorado el peluche, el total a pagar es {Opanda_G+ 50000}")
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
        elif obc == 2:
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
elif peluche == 3:
    print("En que tamano desea el peluche")
    print("1.pequeno")
    print("2.grande")
    tamano= int (input("ingrese el # del tamano que desea que sea el peluche"))
    if tamano ==1:
        Stitch_P =200000
        print (F"el valor a pagar es {Stitch_P}")
        print("Desea que le decoren el peluche : 1.si o 2.no")
        obc= int(input("ingrese el numero de la obcion que desea realizar"))
        if obc == 1:
            print(F"se a decorado el peluche, el total a pagar es {Stitch_P+ 50000}")
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
        elif obc == 2:
            print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
    elif tamano ==2:
        Stitch_G = 400000
        print (F"el valor a pagar es {Stitch_G}")
    print("Desea que le decoren el peluche : 1.si o 2.no")
    obc= int(input("ingrese el numero de la obcion que desea realizar"))
    if obc == 1:
        print(F"se a decorado el peluche, el total a pagar es {Stitch_G+ 50000}")
        print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")
    elif obc == 2:
        print(F"MUCHAS GRACIAS POR REALIZAR LA COMPRA, HASTA PRONTO")




        

        


