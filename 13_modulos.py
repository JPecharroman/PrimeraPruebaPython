# Modulos en Python
# Un modulo es un archivo con extension .py que contiene definiciones y sentencias
# Es analogo a una libreria

# Para importar un modulo se usa la palabra reservada import
import math # Importa todo el modulo, este modulo es un modulo matematico que provee funciones matematicas

raiz_cuadrada = math.sqrt(16)
print(f"La raiz cuadrada de 16 es: {raiz_cuadrada}")

# Importar una funcion especifica de un modulo, con from modulo import funcion
from math import sqrt
# No importamos el modulo entero, solo la funcion sqrt, esto es util para ahorrar memoria
raiz_cuadrada = sqrt(9) # Hemos importado la funcion sqrt, no necesitamos añadir el modulo math
print(f"La raiz cuadrada de 9 es: {raiz_cuadrada}")
# Para importar mas de una funcion lo hacemos mediante comas
from math import sqrt, pow
raiz_cuadrada = sqrt(25)
potencia = pow(2, 3)
print(f"La raiz cuadrada de 25 es: {raiz_cuadrada}")
print(f"La potencia al cubo de 2 es: {potencia}")   

# Para definir un fichero creado como modulo se usa la palabra reservada def, creamos un modulo en el archivo 13_modulo_creado.py
# Para importar un modulo creado por nosotros se usa la palabra reservada import
import modulo_creado

# Para poder operar con las funciones creadas en el modulo creado debemos usar el nombre del modulo y el nombre de la funcion
# modulo.funcion(parametros)
suma = modulo_creado.suma(10, 20)
resta = modulo_creado.resta(10, 20)
multiplicacion = modulo_creado.multiplicacion(10, 20)
division = modulo_creado.division(10, 20)

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")
print(f"La division es: {division}")    

   
