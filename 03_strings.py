# Strings, cadenas de texto en Python
# Definición de una cadena de texto
mi_cadena = "Hola, Mundo!"
# Podemos usar comillas simples o dobles
otra_cadena = 'Python es genial'
print(mi_cadena)  # Imprime la cadena completa
print(otra_cadena)  # Imprime la otra cadena

# Hallar la longitud de una cadena
longitud = len(mi_cadena)
print("Longitud de mi_cadena:", longitud, "caracteres")

# Concatenación de cadenas
saludo = mi_cadena + " " + otra_cadena
print(saludo)  # Imprime la cadena concatenada
print()

# Caracteres especiales
# Uso de secuencias de escape para incluir caracteres especiales
# Nueva línea con \n y tabulación con \t
cadena_con_especiales = "Primera línea\nSegunda línea\tcon tabulación"
print(cadena_con_especiales)
print()

# Dar formato a las cadenas, tener valores de varios tipos en la cadena (con f-strings)
nombre = "Ana"
apellido = "Pérez"
edad = 28

# Usando f-strings, inferencio de datos, para formatear la cadena
presentacion = f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años."
print(presentacion)  # Imprime la presentación formateada
print()
# Usando % y .format() para formatear cadenas
# %s para cadenas, %d para enteros, el % antes del paréntesis final indica que es una tupla de dos cadenas de caracteres y un entero
presentacion_percent = "Hola, mi nombre es %s %s y tengo %d años." % (nombre, apellido, edad)
print(presentacion_percent)  # Imprime la presentación formateada con %
# En vez de usar %s y %d, usamos llaves {} como marcadores de posición y la función .format() con las variables correspondientes
presentacion_format = "Hola, mi nombre es {} {} y tengo {} años.".format(nombre, apellido, edad)
print(presentacion_format)  # Imprime la presentación formateada con .format()
print()

# Interpolación de cadenas
# Combinar cadenas usando f-strings
ciudad = "Madrid"
pais = "España"
ubicacion = f"{nombre} vive en {ciudad}, {pais}."
print(ubicacion)  # Imprime la ubicación formateada
print()

#combinar enteros usando f-strings
a = 5
b = 10
suma = f"La suma de {a} y {b} es {a + b}."
print(suma)  # Imprime la suma formateada
print()

# Desempaquetado de cadenas
# Asignar caracteres individuales de una cadena a variables
palabra = "Python"
# Desempaquetado de cada carácter en variables separadas, como Python tiene 6 letras, se crean 6 variables
a, b, c, d, e, f = palabra
print(a)  # Imprime 'P'
print(b)  # Imprime 'y'
print(c)  # Imprime 't'
print(d)  # Imprime 'h'
print(e)  # Imprime 'o'
print(f)  # Imprime 'n'
print()

# Division de cadenas
# Conseguir una parte de la cadena usando slicing (rebanado)
texto = "Aprendiendo Python"
slice_cadena = texto[1:11]  # Obtiene los caracteres desde el índice 1 hasta el 10, el primero no lo obtiene ya que empieza en el indice 0, el 11 no lo obtiene porque es exclusivo
print(slice_cadena)  # Imprime 'prendiendo'
print()
#Slice solo con el inicio
slice_inicio = texto[11:]  # Obtiene los caracteres desde el índice 11 hasta el final
print(slice_inicio)  # Imprime 'Python'
print()
#Slice solo con el final
slice_final = texto[:11]  # Obtiene los caracteres desde el inicio hasta el índice 10
print(slice_final)  # Imprime 'Aprendiendo'
print()
#Slice con paso (especificar cada cuantos caracteres se toma uno)
slice_paso = texto[0:15:2]  # Obtiene los caracteres desde el índice 0 hasta el 14, tomando cada 2 caracteres
print(slice_paso)  # Imprime 'ArninoPt' 
print()
# Slice con índices negativos
slice_negativo = texto[-6:]  # Obtiene los últimos 6 caracteres de la cadena ya que empezamos desde -1 que es la última letra
print(slice_negativo)  # Imprime 'Python'
# Dar la vuelta a la cadena usando slicing con paso negativo
cadena_invertida = texto[::-1]  # Invierte la cadena completa
print(cadena_invertida)  # Imprime 'nohtyP odneidnarpA'
print()


# Dividir una cadena en una lista de subcadenas usando un separador
frase = "Aprender Python es divertido"
palabras = frase.split(" ")  # Divide la frase en palabras usando el espacio como separador
print(palabras)  # Imprime la lista de palabras ['Aprender', 'Python', 'es', 'divertido']
print()




