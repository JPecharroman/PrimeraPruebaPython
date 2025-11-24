# Funciones en Python
# Una funcion es un bloque de codigo que se ejecuta cuando se llama

# Definir una funcion mediante la palabra reservada def nombre_funcion()
# Python no usa llaves, todo lo que este tabulado sera parte de la funcion
def saludar():
    print("Hola, bienvenido a mi programa")

# Llamar a la funcion
saludar()

# Una funcion puede recibir parametros y devolver valores, veamos ejemplos
# Recibir parametros
def sumar(parametro1, parametro2):
    suma = parametro1 + parametro2
    return suma # Devolver valor, en este caso la suma de los parametros pasados como parametros

print(sumar(10, 20))

# Funciones con cadenas de caracteres
nombre = "Jorge"
apellido = "Rios"
def imprime_nombre(nombre, apellido):
    print(f"Hola {nombre} {apellido}, bienvenido a mi programa en Python") # Damos formato a la cadena de caracteres con f

imprime_nombre(nombre, apellido)
imprime_nombre(apellido="Perez", nombre="Juan") # Podemos cambiar el orden de los parametros especificando el nombre del parametro

# Valores por defecto
nombre = "Jorge"
apellido = "Rios"
edad = 30
def imprime_datos(nombre, apellido, edad = 0):
    print(f"Hola {nombre} {apellido}, tienes {edad} años")

imprime_datos(nombre, apellido, edad)
imprime_datos(nombre, apellido) # Al no poner edad coge el valor por defecto definido en la funcion, 0.

# Pasar un numero indefinido de parametros
def imprime_texto(*texto):
    print(f"{texto}")

imprime_texto("Hola", "bienvenido", "a", "mi", "programa")
imprime_texto("Hola", "bienvenido", "a", "mi", "programa", "en", "Python")


