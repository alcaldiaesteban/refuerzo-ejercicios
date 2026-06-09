# Ejercicio 2 - iterar sobre diccionarios

# Hay tres formas de recorrer un diccionario con for:
#
#   for clave in diccionario:            -> recorre las claves
#   for clave in diccionario.keys():     -> igual al anterior, más explícito
#   for valor in diccionario.values():   -> recorre solo los valores
#   for clave, valor in diccionario.items(): -> recorre clave Y valor juntos

# Trabaja con este diccionario de precios:
precios = {
    "manzana": 1200,
    "leche": 3500,
    "pan": 2000,
    "huevos": 8000,
    "arroz": 4500
}

# 1. Imprime solo los nombres de los productos (las claves).

# 2. Imprime solo los precios (los valores).

# 3. Imprime cada producto con su precio así:
#    manzana -> $1200

# 4. Calcula el precio total si se compra uno de cada producto.

# 5. Encuentra el producto más caro. (sin usar max())


