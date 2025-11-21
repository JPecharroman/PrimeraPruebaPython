# Por claridad crearemos varios archivos de variables
# Probamos la funcion input() para solicitar datos al usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")
edad_usuario = input("Por favor, ingresa tu edad: ") # Estos valores son del tipo cadena (string), si queremos usarlos como numeros debemos convertirlos
edad_usuario = int(edad_usuario)  # Convertimos la edad a entero

# Imprimos los datos ingresados por el usuario
print("¡Hola,", nombre_usuario + "! Tienes", edad_usuario, "años.")

# Frozar el tipo de dato de una variable no es posible en Python, pero podemos usar anotaciones de tipo para indicar el tipo esperado
altura: float = 1.75  # Anotación de tipo indicando que altura es un float
print("Tu altura es de", altura, "metros.")
# Sin embargo, Python no impide que cambiemos el tipo de dato
altura = "un metro y setenta y cinco centimetros"  # Ahora altura es una cadena
print("Ahora tu altura es:", altura)  # Imprime la nueva cadena
