"""
Ejercicio 4: Implementa un programa con un bucle for
que calcule la suma de los cuadrados de los números del 1 al 20. """

suma_c = 0

for i in range(1, 21):  # El rango va de 1 a 20 (inclusive)
    suma_c += i ** 2  # Suma el cuadrado de i 

print(f"La suma de los números del 1 al 20 elevados al cuadrado es: {suma_c}")