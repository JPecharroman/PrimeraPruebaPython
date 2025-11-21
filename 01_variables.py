# Variables, por conveccion en python los nombres de las variables
# se escriben en minusculas y si tienen varias palabras se separan con guion bajo (snake_case)

my_variable = "Hello, World!"
print(my_variable)

# Python es case-sensitive, lo que significa que 'myVariable' y 'myvariable' son variables diferentes
myVariable = 10
myvariable = 20
print(myVariable)  # Salida: 10
print(myvariable)  # Salida: 20

#definimos variables de diferentes tipos de datos
nombre = "Alice"          # cadena de texto (string)
apellidos = 'Smith'       # cadena de texto (string)
edad = 30                 # entero (int)
direccion = "123 Main St" # cadena de texto (string)
es_estudiante = True      # booleano (bool)

print("hola, tu nombre es", nombre, apellidos, ",", "tienes", edad, "años y vives en", direccion)

#conversion de tipos de datos
edad_como_cadena = str(edad)  # Convertir entero, edad, a cadena
print("Tu edad es " + edad_como_cadena + " años.")  # Concatenación de cadenas usando la conversión y el operador +

""" forma analoga de hacerlo, definimos una nueva variable  y le asignamos la concatenacion de cadenas
cadena = "Tu edad es " + edad_como_cadena + " años."  # Concatenación de cadenas
print(cadena)
"""

# Funciones precargadas del sistema
# probamos len() para obtener la longitud de una cadena, solo funciona con strings, listas, tuplas, diccionarios, etc. no con enteros o booleanos  
longitud_nombre = len(nombre)
print("La longitud de tu nombre es:", longitud_nombre)

# longitud_edad = len(edad) no funciona porque edad es un entero

