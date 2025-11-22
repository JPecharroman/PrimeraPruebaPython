# Probamos algunos operadores en Python
# Los operadores son símbolos especiales que realizan operaciones con uno o más operandos, los operadores más comunes son:
# Aritméticos: +, -, *, /, %, //, **
# Comparación: ==, !=, >, <, >=, <=
# Lógicos: and, or, not
# Asignación: =, +=, -=, *=, /=, %=, //=, **=
# De pertenencia: in, not in
# De identidad: is, is not
# Bit a bit: &, |, ^, ~, <<, >>

#operadores aritméticos
print("Operadores Aritméticos, usamos 5 y 3 como operandos:")
print("Suma: ", 5 + 3)          # Suma
print("Resta: ", 5 - 3)         # Resta
print("Multiplicación: ", 5 * 3) # Multiplicación
print("División: ", 5 / 3)      # División
print("Módulo: ", 5 % 3)        # Módulo
print("División entera: ", 5 // 3) # División entera   
print("Exponente: ", 5 ** 3)    # Exponente
print()

# Uso de paréntesis para cambiar el orden de las operaciones
# El orden de las operaciones sigue las reglas matemáticas estándar, pero los paréntesis pueden usarse para alterar este orden.
# Sin parentesis, el orden de operaciones es: primero multiplicación y división, luego suma y resta. el exponente tiene la mayor prioridad.
print("Uso de paréntesis para cambiar el orden de las operaciones:")
print("Sin paréntesis: 5 + 3 * 2 ", 5 + 3 * 2)       # Sin paréntesis
print("Con paréntesis: (5 + 3) * 2 ", (5 + 3) * 2)   # Con paréntesis
print()

# Concatenación de cadenas de texto con operador +
print("Concatenación de cadenas de texto con operador +:")
cadena1 = "Hola, "
cadena2 = "mundo!" 
cadena = cadena1 + cadena2 # Concatenación de cadenas
print(cadena)  
print()

# Repetición de cadenas de texto con operador *
print("Repetición de cadenas de texto con operador *:") 
cadena_repetida = "Hola! " * 3 # Repetición de cadenas
print(cadena_repetida)
print()

# Operadores de comparación
print("Operadores de comparación, usamos 5 y 3 como operandos:")
print("Igual a (5 == 3): ", 5 == 3)          # Igual a
print("No igual a (5 != 3): ", 5 != 3)        # No igual a
print("Mayor que (5 > 3): ", 5 > 3)          # Mayor que
print("Menor que (5 < 3): ", 5 < 3)          # Menor que
print("Mayor o igual que (5 >= 3): ", 5 >= 3) # Mayor o igual que
print("Menor o igual que (5 <= 3): ", 5 <= 3)   # Menor o igual que
print()

# Comparacion de cadenas de texto
print("Comparación de cadenas de texto:")
print("'abc' == 'abc': ", 'abc' == 'abc')      # Igual a
print("'abc' != 'def': ", 'abc' != 'def')      # No igual a
print("'abc' > 'abd': ", 'abc' > 'abd')        # Mayor que
print("'abc' < 'abd': ", 'abc' < 'abd')        # Menor que
print()

# Recordar que las comparaciones son sensibles a mayúsculas y minúsculas, las mayusculas tienen un valor ASCII menor que las minúsculas por lo que las 
# minusculas son mayores que las mayusculas.
print("Comparaciones sensibles a mayúsculas y minúsculas:")
print("'abc' == 'ABC': ", 'abc' == 'ABC')      # Igual a
print("'abc' < 'ABC': ", 'abc' < 'ABC')        # Menor que
print()

# Si queremos compaarar la longitud de las cadenas en lugar de su valor lexicográfico, podemos usar la función len()
print("Comparación de la longitud de las cadenas usando la funcion len():")
print("len('abc') == len('ABC'): ", len('abc') == len('ABC'))  # Igual a
print("len('abc') > len('ABCD'): ", len('abc') > len('ABCD'))  # Mayor que
print()

# Operadores lógicos
print("Operadores lógicos:")
print("Operador and, solo es True si ambos operandos son True:")
print("True and True: ", True and True)     # True
print("True and False: ", True and False)   # False
print("False and False: ", False and False) # False
print()

print("Operador or, es True si al menos uno de los operandos es True:")
print("True or True: ", True or True)       # True
print("True or False: ", True or False)     # True
print("False or False: ", False or False)   # False
print()

print("Operador not, invierte el valor lógico del operando:")
print("not True: ", not True)   # False
print("not False: ", not False) # True
print()
