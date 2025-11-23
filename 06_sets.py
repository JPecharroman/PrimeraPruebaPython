# Sets en Python
# Los sets son colecciones desordenadas de elementos únicos. No permiten elementos duplicados y son mutables.
print("Sets en Python:")
print("Los sets son colecciones desordenadas de elementos únicos. No permiten elementos duplicados y son mutables.")
# Crear un set
# Los sets se crean usando llaves {} o el constructor set().
mi_set = {1, 2, 3, 4, 5}
otro_set = set([4, 5, 6, 7, 8])  # Usando el constructor set()
print("Set creado con llaves:", mi_set)
print("Tipo de dato:", type(mi_set))
print("Set creado con el constructor set():", otro_set)
print("Tipo de dato:", type(otro_set))
print()

# Diferencia entre set y lista
# Un set no mantiene el orden de los elementos y no permite duplicados, mientras que una lista sí.
# Al crear un set a partir de una lista con elementos duplicados, los duplicados se eliminan automáticamente.
print("Diferencia entre set y lista:")
mi_lista = [1, 2, 2, 3, 4, 4, 5]
print("Lista con elementos duplicados:", mi_lista)
mi_set_desde_lista = set(mi_lista)
print("Set creado desde la lista (elementos duplicados eliminados):", mi_set_desde_lista)
print()

# Operaciones con sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Operaciones con sets:")
print("Set A:", set_a)
print("Set B:", set_b) 
# Unión
union = set_a.union(set_b)
print("Unión de A y B:", union)
print("Al unir A y B, los elementos duplicados se eliminan automáticamente. En este caso, el elemento 3 está en ambos sets, pero aparece solo una vez en la unión.")
print("Tambien se puede usar el operador | para la unión:", set_a | set_b)
print()

# Intersección
interseccion = set_a.intersection(set_b)
print("Operaciones con sets:")
print("Set A:", set_a)
print("Set B:", set_b) 
print("Intersección de A y B:", interseccion)
print("La intersección devuelve los elementos que están en ambos sets. En este caso, solo el elemento 3 está en ambos sets.")
print("Tambien se puede usar el operador & para la intersección:", set_a & set_b)
print()

# Diferencia
diferencia = set_a.difference(set_b)
print("Operaciones con sets:")
print("Set A:", set_a)  
print("Set B:", set_b)
print("Diferencia de A y B (elementos en A pero no en B):", diferencia)
print("La diferencia devuelve los elementos que están en el primer set pero no en el segundo. En este caso, los elementos 1 y 2 están en A pero no en B.")
print("Tambien se puede usar el operador - para la diferencia:", set_a - set_b)
print()

# Agregar y eliminar elementos a un set
mi_set = {1, 2, 3}  
print("Agregar y eliminar elementos a un set:")
print("Set inicial:", mi_set)
mi_set.add(4)  # Agregar un elemento
print("Set después de agregar 4:", mi_set)
mi_set.remove(2)  # Eliminar un elemento
print("Set después de eliminar 2:", mi_set)
print()
# Funcion discard para eliminar un elemento sin generar error si no existe
print("Usando discard para eliminar un elemento sin generar error si no existe:")
mi_set.discard(5)  # No genera error si el elemento no existe
print("Set después de intentar eliminar 5 (no existe):", mi_set)
print()

# Comprobar si un elemento está en un set mediante el operador in
print("Comprobar si un elemento está en un set mediante el operador in:")
mi_set = {1, 2, 3, 4, 5}
print("Set:", mi_set)
print("¿El 3 está en el set?", 3 in mi_set)  # Devuelve True
print("¿El 6 está en el set?", 6 in mi_set)  # Devuelve False
print()

# Funciones útiles para sets
mi_set = {1, 2, 3, 4, 5}
print("Funciones útiles para sets:")
print("Set:", mi_set)
print("Longitud del set:", len(mi_set))  # Devuelve el número de elementos en el set
print("Elemento máximo del set:", max(mi_set))  # Devuelve el elemento máximo
print("Elemento mínimo del set:", min(mi_set))  # Devuelve el elemento mínimo
print("Suma de los elementos del set:", sum(mi_set))  # Devuelve la suma de los elementos
print("clear() para eliminar todos los elementos del set:")
mi_set.clear()
print("Set después de clear():", mi_set)
print()
# update() para agregar múltiples elementos a un set
print("Usando update() para agregar múltiples elementos a un set:")
mi_set = {1, 2, 3, 4, 5}
print("Set antes de update():", mi_set)
mi_set.update([6, 7, 8])
print("Set después de update():", mi_set)
print()

# Resumen de sets
print("Resumen de sets:")
print("Los sets son colecciones desordenadas de elementos únicos que no permiten duplicados.")

# Acceder a un elelmento de un set mediante un indice no es posible, ya que los sets son desordenados.
print("Acceder a un elemento de un set mediante un índice no es posible, ya que los sets son desordenados.")

# Los sets son estructuras desordenadas de elementos únicos que permiten realizar operaciones matemáticas como unión, intersección y diferencia de manera eficiente.
print("Los sets son estructuras desordenadas de elementos únicos que permiten realizar operaciones matemáticas como unión, intersección y diferencia de manera eficiente.")

# Los sets son útiles cuando se necesita almacenar una colección de elementos sin duplicados y realizar operaciones de conjuntos.
print("Los sets son útiles cuando se necesita almacenar una colección de elementos sin duplicados y realizar operaciones de conjuntos.")

# Fin del archivo 06_sets.py




