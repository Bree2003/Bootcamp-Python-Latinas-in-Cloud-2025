#  None
# Representa ausencia de valor
variable = None
if variable is None:
    print("La variable no tiene valor")

# Funciones utiles para tipos de datos
# ---------------------------------
type(variable)  # Retorna el tipo de dato
id(variable)    # Retorna el identificador unico del objeto en memoria
isinstance(1, int)  # Verifica si un objeto es de un tipo dado
str(123)  # Convierte a cadena de texto "123"
int("456")  # Convierte a entero 456
float("3.14")  # Convierte a decimal 3.14
list("hola")  # Convierte a lista, ['h', 'o', 'l', 'a']
tuple([1, 2, 3])  # Convierte a tupla, (1, 2, 3)
set([1, 2, 2, 3])  # Convierte a conjunto, {1, 2, 3}
dict([("a", 1), ("b", 2)])  # Convierte a diccionario, {'a': 1, 'b': 2}
