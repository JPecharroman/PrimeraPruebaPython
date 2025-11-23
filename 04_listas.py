# Listas en Python, tambien conocidas como arrays en otros lenguajes de programación.
# Una lista es una colección ordenada y mutable de elementos. Una estructura de datos muy utilizada en Python.
# Se definen utilizando corchetes [] y los elementos están separados por comas.
# Ejemplo de creación de una lista
mi_lista = [1, 2, 3, 4, 5]
print("Lista inicial:", mi_lista)
print("Tipo de dato:", type(mi_lista))
print("Longitud de la lista:", len(mi_lista))
print()

# Funcion list() para crear una lista a partir de un iterable (como una cadena o una tupla)
otra_lista = list(("a", "b", "c"))  # Usamos un constructor de tupla para crear la lista
print("Lista creada con list():", otra_lista)
print("Tipo de dato:", type(otra_lista))
print("Longitud de la lista:", len(otra_lista))
print()

# En una lista podemos usar datos de diferentes tipos
persona = ["Juan", 30, True, 1.75] # type: ignore # Nombre, edad, casado, altura
print("Lista con diferentes tipos de datos:", persona) # type: ignore
print("Tipo de dato:", type(persona)) # type: ignore
print("Longitud de la lista:", len(persona)) # type: ignore
print()

# Acceso a elementos de una lista mediante índices, como en el caso de los strings y tuplas empezamos a contar desde 0
print("Primer elemento de mi_lista tiene el indice 0:", persona[0])   
print("Segundo elemento de mi_lista tiene el indice 1:", persona[1])   
print("Podemos acceder al ultimo elemento de mi_lista con el indice -1:", persona[-1])
# podemos acceder a la lissta en ordenes inversas con indices negativos
print("Penultimo elemento de mi_lista con el indice -2:", persona[-2])
print()

# Podemos sacar los elementos de una lista a variables individuales
# Para desempaquetar una lista, el numero de variables debe coincidir con el numero de elementos en la lista
# Los desempaquetados no son buenas practicas, si no se conoce la estructura de la lista. Se desaconseja su uso.
nombre, edad, casado, altura = persona  # type: ignore
print("Nombre:", nombre)
print("Edad:", edad)
print("Casado:", casado)
print("Altura:", altura)
print()
# Para asignar un elemento a una variable lo haremos accediendo mediante su indice
nombre2 = persona[0]  # type: ignore
print("Nombre2:", nombre2)
print()

# Concatenación de listas con el operador +
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista concatenada:", lista_concatenada)
print()

# Repetición de listas con el operador *
lista_repetida = lista1 * 3
print("Lista 1 repetida 3 veces:", lista_repetida)
print()



# Funciones y métodos comunes para listas
# Contar elementos count(), cuenta las veces que aparece un elemento en la lista
numeros = [1, 2, 2, 3, 4, 2, 5]
print("Lista de numeros:", numeros)
print("El numero 2 aparece", numeros.count(2), "veces en la lista numeros.")
print()

# Añadir elementos append(), añade un elemento al final de la lista
print("Lista de numeros antes de añadir un elemento al final de la lista, append(6):", numeros)
numeros.append(6)
print("Lista de numeros despues de añadir un elemento al final de la lista, append(6):", numeros)
print()
# Insertar elementos insert(), inserta un elemento en una posición específica
print("Lista de numeros antes de insertar un elemento, el entero 10, en la posicion 2, recordar que empezamos en el indice 0, insert(2, 10):", numeros)
numeros.insert(2, 10)
print("Lista de numeros despues de insertar un elemento, el entero 10, en la posicion 2, recordar que empezamos en el indice 0, insert(2, 10):", numeros)
print()
# Eliminar elementos remove(), elimina la primera aparición del elemento específicado como argumento, en este caso buscamos el primer 2
print("Lista de numeros antes de eliminar el primer 2 que encuentra, remove(2):", numeros)
numeros.remove(2) 
print("Lista de numeros despues de eliminar el primer 2 que encuentra, remove(2):", numeros)
print()

# Operaciones propias de colas, LIFO en este caso, que usaremos con listas
# pop(): elimina y devuelve el último elemento de la lista, si no se especifica un índice
# Sin indice
temperaturas = [20, 22, 21, 19, 23]
print("Lista de temperaturas antes de usar pop():", temperaturas)
ultima_temperatura = temperaturas.pop()
print("Lista de temperaturas despues de usar pop():", temperaturas)
print("Ultima temperatura eliminada con pop():", ultima_temperatura)
print()
# Con indice, recordar que el indice empieza en 0, buscamos la segunda temperatura
print("Lista de temperaturas antes de usar pop(1), recordar que el indice empieza en 0, buscamos la segunda temperatura:", temperaturas)
segunda_temperatura = temperaturas.pop(1)
print("Lista de temperaturas despues de usar pop(1), recordar que el indice empieza en 0, buscamos la segunda temperatur :", temperaturas)
print("Segunda temperatura eliminada con pop(1), recordar que el indice empieza en 0, buscamos la segunda temperatura:", segunda_temperatura)
print()
# Para añadir elementos al final de la lista usamos append() como hemos visto antes

# Operaciones propias de pilas, FIFO en este caso, que usaremos con listas
# Para añadir elementos al principio de la lista usamos insert(0, elemento)
edades = [25, 30, 35, 40]
print("Lista de edades antes de usar insert(0, 18) para añadir un elemento al principio de la lista:", edades)
edades.insert(0, 18)
print("Lista de edades despues de usar insert(0, 18) para añadir un elemento al principio de la lista:", edades)
print()
print("Al ser una lista FIFO vamos empujando los elementos hacia la derecha, de tal manera que el primero en entrar sea el primero en salir gracias a pop().")
print("Lista de edades antes de usar pop(), al ser una lista FIFO el elemento que sacaremos sera el situado mas a la derecha, 40:", edades)
ultimo_elemento_fifo = edades.pop()
print("Lista de edades despues de usar pop(), al ser una lista FIFO hemos eliminado el 40 de la lista:", edades)
print("Ultimo elemento eliminado con pop() en una lista FIFO:", ultimo_elemento_fifo)
print()

# Ordenar listas sort(), ordena los elementos de la lista en orden ascendente
numeros_desordenados = [5, 2, 9, 1, 7, 6]
print("Lista de numeros desordenados antes de usar sort():", numeros_desordenados)  
numeros_ordenados = numeros_desordenados.copy()  # Hacemos una copia para no modificar la original 
numeros_ordenados.sort() # Ordena la lista en orden ascendente
print("Lista de numeros ordenados despues de usar sort():", numeros_ordenados)
print()
# Ordenar listas sort() con el argumento reverse=True, ordena los elementos de la lista en orden descendente
numeros_desordenados_desc = [5, 2, 9, 1, 7, 6]
print("Lista de numeros desordenados antes de usar sort(reverse=True):", numeros_desordenados_desc)  
numeros_ordenados_desc = numeros_desordenados_desc.copy()  # Hacemos una copia para no modificar la original 
numeros_ordenados_desc.sort(reverse=True) # Ordena la lista en orden descendente
print("Lista de numeros ordenados en orden descendente despues de usar sort(reverse=True):", numeros_ordenados_desc)
print()

# Invertir el orden de los elementos reverse(), invierte el orden de los elementos en la lista
letras = ['a', 'b', 'c', 'd', 'e']
print("Lista de letras antes de usar reverse():", letras)
letras.reverse()
print("Lista de letras despues de usar reverse():", letras)
print()

# Limpiar una lista clear(), elimina todos los elementos de la lista
colores = ['rojo', 'verde', 'azul']
print("Lista de colores antes de usar clear():", colores)
colores.clear()
print("Lista de colores despues de usar clear():", colores)
print()

# Copiar una lista copy(), crea una copia superficial de la lista
frutas = ['manzana', 'banana', 'cereza']
print("Lista de frutas original:", frutas)
frutas_copiadas = frutas.copy()
print("Copia de la lista de frutas usando copy():", frutas_copiadas)
print()
# Podemos modificar la copia sin afectar a la lista original
frutas_copiadas.append('naranja')
print("Lista de frutas original despues de modificar la copia:", frutas)
print("Copia de la lista de frutas despues de añadir 'naranja':", frutas_copiadas)
print()







