"""
Helen Farina Renteria. 
Crear un programa que calcule el precio total de una compra de camisas. El precio
de cada camisa es de $35,000. Si el número de camisas compradas es de 12
unidades, se aplicará un descuento del 10%, y aumenta un 2% por cada camisa
adicional, a partir de la docena, con un límite máximo de 50% de descuento.
"""
#Precio Final=Precio Original−(Precio Original×Porcentaje de Descuento)
# el while permite que el programa se repita 
while True:  # la condicion siempre sera verdadera por lo que siempre se va a repetir hasta que se rompa el ciclo 

    PRECIO_C= 35000
    descuento= 0
    total= 0 
    print("  ") 
    print("-----------------------------------------")
    Numero_C = int(input("BIENVENID@ CUANTAS CAMISAS DESEA COMPRAR: "))

    if Numero_C < 12: 
        total = PRECIO_C * Numero_C
        print(F"el total a pagar es {total}")
        print("MUCHAS GRACIAS POR LA COMPRA ESPERO QUE VUELVAS")
        print("  ")
    elif Numero_C == 12:
        sindescuento= PRECIO_C *Numero_C
        total = sindescuento - (sindescuento * 0.10)
        print(F"el total sin descuento es {sindescuento}")
        print(F"el total a pagar con descuento es {total}")
        print("MUCHAS GRACIAS POR LA COMPRA ESPERO QUE VUELVAS")
        print("  ")
    elif Numero_C > 12:
        # multiplicamos el #camisas adicis * el 0.02 para saber el total del descuento adicional 
        descuento_adicional = (Numero_C -12) * 0.02 
        descuento = 0.10+descuento_adicional 
        
        # para que el descuento no esceda el 50% 
        if descuento > 0.50:
        
            descuento = 0.50
            

    
        sindescuento= PRECIO_C *Numero_C 
        total = sindescuento - (sindescuento * descuento)

        print(F"el total a pagar es {total}")
        print("MUCHAS GRACIAS POR LA COMPRA ESPERO QUE VUELVAS")
        print("  ")
    #condicion para romper el while 
    continuar= input("Desea comprar mas camisas? (ingrese s/n)")
    if continuar.lower()!= "s": 
        break 



