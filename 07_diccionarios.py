# Diccionarios en Python
# Los diccionarios son colecciones desordenadas de pares clave-valor. Son mutables y permiten acceder a los valores mediante sus claves.
print("Diccionarios en Python:")
print("Los diccionarios son colecciones desordenadas de pares clave-valor. Son mutables y permiten acceder a los valores mediante sus claves.")
# Crear un diccionario, se crean usando llaves {} con pares clave-valor separados por dos puntos.
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "casado": True
}
print("Diccionario creado:", mi_diccionario)
print("Tipo de dato:", type(mi_diccionario))
print()

# Otra forma de crear un diccionario es mediante el constructor dict(), la diferencia es que no se usan llaves {} 
# y los pares clave-valor llevan un igual en vez de dos puntos.
otro_diccionario = dict(
    nombre="Ana",
    edad=25,
    ciudad="Barcelona"
)
print("Otro diccionario, creado con el constructor dict():", otro_diccionario)
print("Tipo de dato:", type(otro_diccionario))
print()

# Podemos pasarle otras estructuras de datos, como sets, listas o tuplas a un diccionario
diccionario_con_estructuras = {
    "lista": [1, 2, 3],
    "tupla": (4, 5, 6),
    "set": {7, 8, 9}
}
print("Diccionario con estructuras de datos:", diccionario_con_estructuras)
print("Tipo de dato:", type(diccionario_con_estructuras))
print()

# Acceder a los valores de un diccionario, accedemos mediante el nombre del diccionario y la clave entre corchetes
name = mi_diccionario["nombre"]
print("Valor de nombre en el diccionario:", name)
print()

# Modificar un valor en el diccionario
print("Valor de edad en el diccionario:", mi_diccionario["edad"])
mi_diccionario["edad"] = 31
print("Valor de edad modificado en el diccionario:", mi_diccionario["edad"])
print()

# Añadir un nuevo par clave-valor al diccionario
mi_diccionario["profesion"] = " Ingeniero"
print("Valor de profesion en el diccionario:", mi_diccionario["profesion"])
print("Diccionario actualizado:", mi_diccionario)
print()

# Eliminar un par clave-valor del diccionario
print("Eliminamos la clave 'ciudad' del diccionario:", mi_diccionario)
mi_diccionario.pop("ciudad")
print("Diccionario actualizado:", mi_diccionario)
print()
# Podemos usar la palabra reservada del para eliminar una clave-valor
persona = dict(
    nombre="Juan",
    edad=30,
    ciudad="Madrid",
    profesion="Ingeniero",
    altura=1.80
)
print("Diccionario creado:", persona)
print("Tipo de dato:", type(persona))
# Eliminar un par clave-valor del diccionario
print("Eliminamos la clave 'ciudad' del diccionario usando la palabra reservada del:", persona)
del persona["ciudad"]
print("Diccionario actualizado:", persona)
print()

# Busquedas mediante la palabra reservada in en diccionarios
print("Buscamos la clave 'edad' en el diccionario:", "edad" in persona)
print("Buscamos la clave 'altura' en el diccionario:", "altura" in persona)
print() 

# Funciones y metodos que podemos usar con los diccionarios
# Funcion items() que nos devuelve una lista de tuplas con los pares clave-valor
print("Items del diccionario:", persona.items())
print()
# Funcion keys() que nos devuelve una lista de las claves del diccionario
print("Claves del diccionario:", persona.keys())
print()
# Funcion values() que nos devuelve una lista de los valores del diccionario
print("Valores del diccionario:", persona.values())
print()
# Funcion get() que nos devuelve el valor de una clave
print("Valor de la clave 'nombre':", persona.get("nombre"))
print()
# Funcion update() que nos permite actualizar los valores de un diccionario
print("Actualizamos el valor de la clave 'edad' en el diccionario:", persona)
persona.update({"edad": 31})
print("Diccionario actualizado:", persona)
print()
# Funcion copy() que nos permite crear una copia de un diccionario
print("Copia del diccionario:", persona)
copia = persona.copy()
print("Diccionario copiado:", copia)
print()
# Funcion fromkeys() que nos permite crear un diccionario con claves y valores
# En este caso creamos un diccionario con las claves "nombre", "edad", "ciudad" y les damos a las claves el valor "desconocido"
# fromkeys() nos devuelve un diccionario con las claves y valores que le pasamos, lo correcto seria crealo 
# a partir de la palabra reservada dict() y no de un diccionario determinado
print("Diccionario creado con fromkeys():", dict.fromkeys(["nombre", "edad", "ciudad"], "desconocido"))
print()
# El verdadero sentido de fromkeys() es crear un diccionario con claves a partir de un diccionario ya existente
persona2 = dict.fromkeys(persona)
print("Diccionario creado con fromkeys() a partir de un diccionario ya existente (persona):", persona2)
print()
# Si le pasamos un valor a fromkeys() nos devolvera un diccionario con las claves y el valor que le pasamos
persona3 = dict.fromkeys(persona, "desconocido")
print("Diccionario creado con fromkeys() a partir de un diccionario ya existente (persona) y con un valor por defecto (desconocido):", persona3)
print()

# Funcion clear() que nos permite eliminar todos los pares clave-valor de un diccionario
print("Eliminamos todos los pares clave-valor del diccionario:", persona)
persona.clear()
print("Diccionario actualizado:", persona)
print() 





