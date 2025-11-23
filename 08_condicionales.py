# Condicionales, if, elif, else en Python  
# Los condicionales nos permiten ejecutar cierto código si se cumple una condición

import random # Importamos el modulo random, para hallar numeros aleatorios

# Usamos la palabra reservada if para crear una condición 
mi_condicion = True
if mi_condicion:
    print("Se cumple la condición")
    print("Se sigue cumpliendo la condición")
else:
    print("No se cumple la condición") # Salimos del bucle if dando dos veces al intro

mi_condicion = False
print("\nCambiamos el valor de la condición a False")
print()
if mi_condicion:
    print("Se cumple la condición")
else:
    print("No se cumple la condición")
    print("No se sigue cumpliendo la condición")

# Anidamiento de condiciones usando elif
numero = 10 * 3
# Evaluamos el valor de numero, si es mayor que 20 entramos en la primera condicion
# Si es igual a 20 entramos en la segunda condicion
# Si es menor que 20 entramos en la tercera condicion
print("El numero a analizar es:", numero)
if numero > 20:
    print(f"El número {numero} es mayor que 20") # Damos formato a la cadena de texto
elif numero == 20:
    print(f"El número {numero} es igual a 20") # Damos formato a la cadena de texto
else: # Si no se cumple ninguna de las condiciones anteriores, es decir no es ni mayor ni igual a 20
    print(f"El número {numero} es menor que 20") # Damos formato a la cadena de texto

# Anidar condiciones en el if mediante los operadores logicos and, or y not
# Generamos un numero random entre 0 y 100 (previamente importamos el modulo random para generar numeros aleatorios)
numero = random.randint(0, 100)
print("\nEl numero a analizar es:", numero) # Vemos el numero que nos ha generado random
if numero > 20 and numero < 50: # Si el numero es mayor que 20 y menor que 50
    print("El numero esta entre 20 y 50")
elif numero >= 50 or numero <= 20: # Si el numero es mayor o igual a 50 o menor o igual a 20
    print("El numero es mayor o igual a 50 o menor o igual a 20")
elif not numero == 50: # Si el numero no es 50
    print("El numero no es 50") # Si no se cumple ninguna de las condiciones anteriores 

#Condicional con cadenas de texto
cadena_vacia = "" 
# Al comprobar esta variable mediante un if, se evalua como False, esto es, una cadena de texto vacia es false
if cadena_vacia:
    print("La cadena no está vacía")
else: # Entrara por aqui ya que la cadena esta vacia
    print("La cadena está vacía")

nombre = "Jorge"
if nombre: # Entrara por aqui ya que la cadena de texto no esta vacia
    print(f"La variable no esta vacia y su valor es {nombre}")
else: # No entrara por aqui ya que la cadena no esta vacia
    print("La variable esta vacía")

# Resumen de if, elif y else
# if: Si se cumple la condición
# elif: Si no se cumple la condición anterior y se cumple la condición actual
# else: Si no se cumple ninguna de las condiciones anteriores
