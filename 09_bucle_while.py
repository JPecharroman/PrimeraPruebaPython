# Bucles
# Los bucles son estructuras que nos permiten repetir un bloque de código varias veces en funcion de una condicion

# Empezamos por el bucle while

# while condicion:
#     codigo a repetir

# Ejemplo  

contador = 1
while contador <= 10:
    print(contador)
    contador += 1 # += incrementa la condicion en el numero entero pasado a la derecha

print()

# Debemos de tener especial cuidado con crear bucles infinitos, la condicion debe cumplirse un numero finito de veces
# en algun momento la condicion debe pasar a false para salir del bucle
# En el caso anterior el bucle se ejecuta 10 veces porque la condicion es contador <= 10 y vamos incrementando el contador en 1
# cada vez para acabar pasando la concidion a false.

# Podemos ponerle else al while para que se ejecute una vez que la condicion sea false

contador = 1
while contador <= 10:
    print(contador)
    contador += 2 # += incrementa la condicion en el numero entero pasado a la derecha
else:
    print("Fin del bucle al ser contador mayor que 10")

# Podemos romper el bucle si se cumple una condicion concreta, lo haremos mediante break
contador = 1
while contador <= 10:
    if contador == 5:
        break # Rompemos el bucle mediante la palabra reservada break cuando se cumple una condicion, que contador sea igual a5
    print(contador)
    contador += 1
else: #Este else es de while, no de if
    print("Fin del bucle al ser contador mayor que 10") # No se ejecuta porque se rompe el bucle con break

print("Rompemos el bucle con break, solo imprimimos hasta el 4")


