# FOR

# El bucle for se utiliza para iterar sobre una secuencia (lista, tupla, cadena, etc.)
# Por cada elemento de la secuencia se ejecuta el bloque de código

for i in range(10): # range(10) genera una secuencia de números del 0 al 9
    print(i)

print()

for i in range(1, 11): # range(1, 11), establecemos parametro de inicio y de fin, genera una secuencia de números del 1 al 10
    print(i)

print()

# range(1, 11, 2), establecemos parametro de inicio, de fin y de incremento, genera una secuencia de números del 1 al 10 
# con un incremento de 2
for i in range(1, 11, 2): 
    print(i)

print()

# range(1, 11, -1), establecemos parametro de inicio, de fin y de decremento, genera una secuencia de números del 1 al 10 
# con un decremento de 1
for i in range(11, 1, -1): 
    print(i)

print()

# Podemos usar una lista como rango de valores, listas van entre corchetes
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for i in meses:
    print(i)

print()

# Podemos usar una tupla como rango de valores, tuplas van entre parentesis
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
for i in dias:
    print(i)

print()

# Podemos usar un set como rango de valores, los sets van entre llaves
estaciones = {"Primavera", "Verano", "Otoño", "Invierno"}
for i in estaciones:
    print(i)

print()

# Podemos usar un string como rango de valores, los strings van entre comillas
palabra = "Python"
for i in palabra:
    print(i)

print()

# Podemos usar un diccionario como rango de valores, los diccionarios van entre llaves, en este caso usamos las claves 
# para iterar pero lo que mostrara seran los valores
persona = {"nombre": "Jorge", "apellido": "Garcia", "edad": 30}
for i in persona:
    print(i)

print()

# Podemos usar un diccionario como rango de valores, los diccionarios van entre llaves, en este caso usamos las claves 
# para iterar, esto es, hara el bucle 3 veces, una por cada clave. Pero lo que mostrara seran los items
persona = {"nombre": "Jorge", "apellido": "Garcia", "edad": 30}
for i in persona.items():
    print(i)

print()

# Si queremos sacar valores solo, o claves, modificamos el for con persona.values() o persona.keys()
# Valores
for i in persona.values():
    print(i)

print()

# Claves
for i in persona.keys():
    print(i)

print()

# Como en el caso del bucle while, podemos romper el bucle con break
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for i in meses:
    if i == "Julio":
        break
    print(i)

print()

# Rompemos el bucle en el mes Julio, por lo que solo se imprimen los meses hasta Julio

# Podemos añadir un else cuando el bucle llegue a su final
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
for i in dias:
    print(i)
else: # Una vez el for acaba de iterar la tupla, se ejecuta el else
    print("Fin del bucle")

print()

# continue es una palabra reservada que podemos usar para saltarnos iteraciones, por ejemplo si solo queremos imprimir los meses 
# impares del año podemos usar continue
j = 0
for i in meses:
    j += 1
    if j % 2 == 0: # Si el mes es par su modulo sera 0, por lo que no lo imprimimos
        continue # saltamos la presente iteracion y volvemos a analizar la condicion del for
    print(i)

# No es una buena practica usar continue en bucles for, evitarlo siempre que sea posible.