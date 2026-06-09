# Ejercicio 5 - buscar y modificar un registro

# En tu proyecto del restaurante puedes agregar platos pero no modificarlos.
# Este ejercicio practica exactamente eso: encontrar un elemento
# en la lista y cambiar uno de sus valores.

listaProductos = [
    {"codigo": "P01", "nombre": "Cuaderno",  "precio": 3500,  "stock": 10},
    {"codigo": "P02", "nombre": "Lapicero",  "precio": 1200,  "stock": 50},
    {"codigo": "P03", "nombre": "Mochila",   "precio": 45000, "stock": 5},
]

# 1. Crea la función actualizar_precio(codigo, nuevo_precio):
#    - Recorre listaProductos buscando el codigo
#    - Si lo encuentra, cambia el precio y muestra:
#        "Precio de Cuaderno actualizado a $4000"
#    - Si no existe: "Producto no encontrado"

# 2. Crea la función agregar_stock(codigo, cantidad):
#    - Busca el producto por codigo
#    - Suma la cantidad al stock actual
#    - Muestra: "Stock de Lapicero actualizado: 50 -> 65"

# 3. Prueba las funciones:
#    actualizar_precio("P01", 4000)
#    actualizar_precio("P99", 1000)   <- este no existe
#    agregar_stock("P02", 15)
#    agregar_stock("P03", 0)          <- suma 0, sigue funcionando

# 4. Imprime toda la lista al final para confirmar los cambios.


