# Excepciones en Python
# Se define una excepcion a partir de la palabra reservada try
# Diagrama de excepciones

# Para no sobrecargar la ejecucion del programa iremos metiendo el codigo entre comillas una vez usado
# Si queremos probar algun codigo concreto quitar las """"
"""
try: 
    # Ejecuta este codigo
except:
    # Si hay un error, ejecuta este codigo
else:
    # Si no hay error, ejecuta este codigo
finally:
    # Siempre se ejecuta este codigo
"""

# No es necesario que aparezcan siempre todos los bloques
"""try:
    numero = int(input("Introduce un numero: "))
except ValueError:
    print("Has introducido un valor no valido")"""

# Podemos tener varias excepciones para rastrear varios errores.
"""
try:
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce otro numero: "))
    division = num1 / num2
except ValueError: # No es un numero
    print("Has introducido un valor no valido")
except ZeroDivisionError: # Division entre cero, debemos definir la division previamente, division = num1 / num2
    print("No se puede dividir entre cero")
except Exception as e: # Excepcion general
    print("Ha ocurrido un error: ", e)
else: # Los dos valores introducidos son numeros y el segundo no es 0
    print("La division es: ", division)
finally: # Siempre se ejecuta
    print("Fin del programa")
"""
# excepts mas comunes
# ValueError: Error de valor
# ZeroDivisionError: Division entre cero
# TypeError: Error de tipo
# IndexError: Error de indice
# KeyError: Error de clave
# FileNotFoundError: Error de archivo no encontrado
# EOFError: Error de fin de archivo

# No siempre es obligatorio que el except lleve el error
"""
try:
    numero = int(input("Introduce un numero: "))
except: # No lleva TypeError y le introducimos un string, error de tipo, es str y no int, y funciona, va implicito
    print("Has introducido un valor no valido")
"""

# Podemos capturar la informacion del error
try:
    numero = int(input("Introduce un numero: "))
except ValueError as captura_error: # Capturamos la informacion del error en una variable
    print("Has introducido un valor no valido")
    print(captura_error)
else: # Si no hay error
    print(f"Has introducido un valor valido: {numero}")
finally: # Siempre se ejecuta
    print("Fin del programa")



