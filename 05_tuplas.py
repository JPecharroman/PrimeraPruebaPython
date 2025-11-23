# Tuplas en Python
# Una tupla es una colección ordenada e inmutable de elementos. A diferencia de las listas, las tuplas no pueden ser modificadas después de su creación.
# Se definen utilizando paréntesis (), o tuple(), y los elementos están separados por comas.
# tuple() es un constructor que convierte un iterable (como una lista o una cadena) en una tupla.
# Ejemplo de creación de una tupla 
mi_tupla = (1, 2, 3, 4, 5)
print("Tupla inicial, creada con ():", mi_tupla)
print("Tipo de dato:", type(mi_tupla))
print("Longitud de la tupla:", len(mi_tupla))
print()

# Usando el constructor tuple() para crear una tupla a partir de una lista
otra_tupla = tuple([ "a", "b", "c" ])  # Usamos una lista para crear la tupla
print("Tupla, creada con tuple():", otra_tupla)  
print("Tipo de dato:", type(otra_tupla))
print("Longitud de la tupla:", len(otra_tupla))
print()

# Modificación de tuplas
# Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
# Sin embargo, podemos crear una nueva tupla basada en una existente.
nueva_tupla = mi_tupla + (6, 7, 8)  # Concatenamos una nueva tupla
print("Tupla original:", mi_tupla)
print("Nueva tupla después de concatenar 6, 7 y 8:", nueva_tupla)    
print("Tipo de dato:", type(nueva_tupla))
print("Longitud de la nueva tupla:", len(nueva_tupla))
print()

# Como en el caso de strings y listas podemos accerder a los elementos de una tupla mediante índices positivos y negativos
print("Acceso a elementos de la tupla mediante indices, positivos y negativos:")
print("Tupla original:", mi_tupla)
print("Primer elemento de mi_tupla (índice 0):", mi_tupla[0])        # Primer elemento
print("Último elemento de mi_tupla (índice -1):", mi_tupla[-1])      # Último elemento
print("Elementos desde el índice 1 hasta el 3 (excluyendo el 4):", mi_tupla[1:4])  # Subtupla desde el índice 1 hasta el 3
print()

# funciones y metodos útiles para tuplas
print("Funciones y métodos útiles para tuplas:")
print("Tupla original:", mi_tupla)
print("Cantidad de veces que aparece el elemento 3 en mi_tupla, usamos la funcion count():", mi_tupla.count(3))  # Cuenta cuántas veces aparece el elemento 3
print("Índice del elemento 4 en mi_tupla, usamos la funcion index(), busca el elemento pasado por parametro y nos dice su posicion:", mi_tupla.index(4))          # Devuelve el índice del elemento 4
print()

# Desempaquetado de tuplas
# Podemos asignar los valores de una tupla a múltiples variables en una sola línea. el numero de variables debe coincidir con el número de elementos en la tupla.
print("Desempaquetado de tuplas:")
mi_tupla = (10, 20, 30, 40, 50)
print("Tupla para desempaquetar:", mi_tupla)
a, b, c, d, e = mi_tupla
print("Valores desempaquetados:")
print("a:", a)  
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print()

# Tuplas anidadas
# Las tuplas pueden contener otras tuplas como elementos.   
print("Tuplas anidadas:")
tupla_anidada = (1, 2, (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)  
print("Elemento en la posición 2 (tercer elemento):", tupla_anidada[2])  # Accede a la tupla (3, 4)
# Accediendo a elementos dentro de la tupla anidada, debemos usar índices adicionales
print("Elemento en la posición 2, primera tupla anidada, índice 1 (segundo elemento de la primera tupla anidada):", tupla_anidada[2][1])  # Accede al elemento 4 dentro de la tupla (3, 4)
print()

# ventajas de usar tuplas
# Las tuplas son más rápidas que las listas para ciertas operaciones debido a su inmutabilidad
# Son útiles para datos que no deben cambiar, como coordenadas o configuraciones
# Pueden ser utilizadas como claves en diccionarios debido a su inmutabilidad
print("Ventajas de usar tuplas:")
print("- Más rápidas que las listas para ciertas operaciones.")
print("- Útiles para datos que no deben cambiar.")
print("- Pueden ser utilizadas como claves en diccionarios.")

# Transformar una tupla en una lista
tupla_a_convertir = (1, 2, 3, 4, 5)
lista_convertida = list(tupla_a_convertir) 
print("\nTransformar una tupla en una lista:")
print("Tupla original:", tupla_a_convertir) 
print("Tipo de dato:", type(tupla_a_convertir))
print("Lista convertida:", lista_convertida)
print("Tipo de dato:", type(lista_convertida))
print()

# Añadir un valor a la lista convertida
print("Añadir un valor a la lista convertida:")
lista_convertida.append(8)
print("Lista después de añadir 8:", lista_convertida)
print("Tipo de dato:", type(lista_convertida))
print("Tupla original sigue igual:", tupla_a_convertir)
print("Tipo de dato:", type(tupla_a_convertir))
print()

# Transofrmamos la lista de nuevo en una tupla una vez modificada
tupla_modificada = tuple(lista_convertida)
print("Transformamos la lista modificada de nuevo en una tupla:")
print("Tupla modificada:", tupla_modificada)
print("Tipo de dato:", type(tupla_modificada))
print("Lista original sigue igual:", lista_convertida)
print("Tipo de dato:", type(lista_convertida))
print()

# Conclusión
print("Conclusión:")
print("Las tuplas son estructuras de datos inmutables y ordenadas en Python.")
print("Son útiles para almacenar datos que no deben cambiar y ofrecen ventajas en términos de rendimiento.")

# Fin del archivo 05_tuplas.py


