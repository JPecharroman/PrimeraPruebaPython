# Clases en Python
# Una clase es un modelo o plantilla para crear objetos
# Una clase tiene atributos y metodos
# Un objeto es una instancia de una clase, es decir, un objeto es un ejemplo de una clase

# Definir una clase, la calse tiene atributos y metodos, por convencion se usa mayuscula al inicio de la clase
# En vez de usar snake case usamos camel case, es decir, la primera letra de la clase se pone en mayuscula
# y si tiene mas de una palabra, iran juntas y la siguiente palabra se pone en mayuscula
class PersonaMayor:
    # Atributos
    nombre = "Jorge"
    apellido = "Rios"
    edad = 30
    # Metodos
    # self es una referencia a la instancia actual de la clase
    # self es obligatorio en los metodos
    def saludar(self):
        print(f"Hola {self.nombre} {self.apellido}, bienvenido a mi programa en Python")

# Crear un objeto de la clase PersonaMayor
persona = PersonaMayor()
# Llamamos al metodo saludar del objeto persona de la clase PersonaMayor
persona.saludar()

# Palabra reservada pass
# pass es una palabra reservada que se usa para indicar que no se va a usar
# En este caso, no se va a usar el metodo saludar
class Pajaro:
    # __init__ es un metodo constructor, sirve para inicializar los atributos de la clase
    # self es una referencia a la instancia actual de la clase
    # self es obligatorio en los metodos
    # nombre y especie son atributos de la clase
    # nombre y especie son parametros que se pasan al metodo constructor

    def __init__(self, nombre, envergadura, especie, familia):
        self.nombre = nombre # el atributo interno de la clase, definido por self, toma el valor que le pasamos al parametro nombre
        self.envergadura = envergadura # el atributo interno de la clase, definido por self, toma el valor que le pasamos al parametro envergadura
        self.especie = especie # el atributo interno de la clase, definido por self, toma el valor que le pasamos al parametro especie
        self.familia = familia # el atributo interno de la clase, definido por self, toma el valor que le pasamos al parametro familia

    def volar(self):
        print(f"El pajaro {self.nombre} tiene una envergadura de {self.envergadura} metros")
        print(f"El pajaro {self.nombre} es de la especie {self.especie} y la familia {self.familia}")


# Crear un objeto de la clase Pajaro
pajaro = Pajaro("Piollo", 1.2, "Piollo", "Pajarraco")
pajaro.volar() 

# Creamos nuestras propios atributos propios de la clase
class Personaje:
    def __init__(self, nombre, apellido, vida, ataque):
        self.nombre = nombre
        self.apellido = apellido
        self.vida = vida
        self.ataque = ataque
        self.acronimo = nombre[0] + apellido[0] # Creamos un atributo propio de la clase a partir de los parametros que le pasamos al constructor

    def mostrar(self):
        print(f"El personaje {self.nombre} {self.apellido}, {self.acronimo}, tiene {self.vida} de vida y {self.ataque} de ataque")

personaje = Personaje("Jorge", "Rios", 100, 50)
personaje.mostrar()


# Podemos definir una clase vacia, que podriamos rellenar mas adelante, mediante la palabra reservada pass

class Vacia:
    pass

# Gracias a pass el programa no da error, aunque esta clase no hace nada

vacia = Vacia()

# Podriamos redefinir la clase mas adelante cuando la necesitemos
class Vacia:
    def __init__(self):
        pass # pass es una palabra reservada que se usa para indicar que no se va a usar, o se definira mas adelante
    def volar(self):
        print("El pajaro puede volar")

vacia = Vacia()
vacia.volar()

# Damos algun valor al constructor de la clase Vacia
class Vacia:
    def __init__(self, nombre):
        self.nombre = nombre
    def volar(self):
        print(f"El pajaro {self.nombre} puede volar")

vacia = Vacia("Piollo")
vacia.volar()

# En las clases podemos definir atributos propios o derivados de otros que pasamos como parametros
class anio:
    def __init__(self, anio, mes, dia):
        self.anio = f"{dia} / {mes} / {anio}" # Creamos un atributo propio de la clase a partir de los parametros que le pasamos al constructor
    
    def mostrar(self):
        print(self.anio)

anio = anio(2025, 11, 25)
anio.mostrar()

# Definimos una clase con atributos privados
class Privado:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad # Atributo privado, lo definimos con dos guiones bajos, __
        
    def mostrar(self):
        print(f"El nombre es {self.nombre} {self.apellido}, tiene {self.__edad} años")

privado = Privado("Jorge", "Rios", 30)
privado.mostrar()

# Podemos acceder a los atributos privados mediante el nombre de la clase
print(privado.nombre)
print(privado.apellido)
# print(privado.__edad) # No se puede acceder a los atributos privados por lo el programa da error

# Para acceder a los atributos privados, debemos usar el nombre de la clase y el atributo privado
print(privado._Privado__edad) # Guion bajo delante de la clase y el atributo privado con los dos guiones con los que lo definimos

# Otra forma es crear una funcion que nos devuelva el atributo privado
class Privado1:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad # Atributo privado, lo definimos con dos guiones bajos, __
        
    def mostrar(self):
        print(f"El nombre es {self.nombre} {self.apellido}, tiene {self.__edad} años")
    
    def mostrar_edad(self):
        return self.__edad

privado1 = Privado1("Jorge", "Rios", 30)
privado1.mostrar()
print(privado1.mostrar_edad()) # Mostramos el atributo privado, pero no podemos modificarlo



