"""
Ejercicio 3: Crea un programa que utilice un bucle while para imprimir los números 
de la serie de Fibonacci hasta que el valor sea menor que 1000."""
# como si fuera a=0 y b=1
a, b = 0, 1 


while b < 1000:
    print(b)
    a,b = b, a + b
    
    


