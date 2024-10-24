"""
Ejercicio: 
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
La función retorna el número de veces que se ha impreso el número en lugar de los textos."""
#le agrege un bucle while para que se repita y tambien lo puse para que el usuario decida que texto quiere poner
while True: 

    def ejer(dato1: str, dato2: str):
    
        cont4=0 
        for i in range(1,101):
            if  i % 3 == 0 and i % 5 == 0: 
                print (i, dato1 , dato2)
            
            elif i % 3 == 0:

                print (i, dato1)
            
            elif i % 5 == 0:
                print (i, dato2)
                
            else:
                print(i)
                cont4 +=1  

    
    
        print (f"se imprimio el numero sin texto {cont4} veces")
    # le puse esto paara que fuera mas interativo con el usuario 
    palabra1 = input("ingrese la primera palabra: ")
    palabra2 = input("ingrese la segunda palabra: ")

    ejer(palabra1, palabra2)

    cont= input("Desea continuar s/n")
    if cont.lower() != "s":
        break


