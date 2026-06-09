# Ejercicio 8 - dos listas relacionadas

# En tu proyecto del restaurante, un pedido guarda el código del plato
# pero no el precio. Para calcular el total habría que buscar el plato
# en listaPlatos. Ese es exactamente el patrón de este ejercicio.

# Lista de productos disponibles (NO se modifica)
listaProductos = [
    {"codigo": "P01", "nombre": "Arroz con pollo", "precio": 15000},
    {"codigo": "P02", "nombre": "Sopa",            "precio": 8000},
    {"codigo": "P03", "nombre": "Jugo",             "precio": 4000},
    {"codigo": "P04", "nombre": "Postre",           "precio": 6000},
]

# Lista de pedidos (aquí se guarda lo que pide cada mesa)
listaPedidos = []

# 1. Crea buscar_producto(codigo):
#    - Recorre listaProductos
#    - Retorna el diccionario completo del producto si lo encuentra
#    - Retorna None si no existe

# 2. Crea mostrar_productos():
#    - Imprime los productos disponibles así:
#        [P01] Arroz con pollo - $15000
#        [P02] Sopa - $8000
#        ...

# 3. Crea hacer_pedido():
#    - Pide el número de mesa
#    - Crea un pedido: {"mesa": ..., "items": [], "total": 0}
#    - En un while True:
#        - Muestra los productos disponibles
#        - Pide el código del producto
#        - Si el código es "fin", termina el bucle
#        - Si el producto existe, pide la cantidad y agrega a pedido["items"]:
#            {"nombre": ..., "cantidad": ..., "subtotal": precio * cantidad}
#          y suma el subtotal a pedido["total"]
#        - Si no existe: "Producto no encontrado, intenta de nuevo"
#    - Al terminar agrega el pedido a listaPedidos

# 4. Crea mostrar_pedidos():
#    - Por cada pedido imprime:
#        Mesa 3:
#          Arroz con pollo x2 = $30000
#          Jugo x1 = $4000
#        Total: $34000
#        ----------

# Prueba:
#   hacer_pedido()   <- mesa 3, pide P01 x2, P03 x1, luego "fin"
#   hacer_pedido()   <- mesa 1, pide P02 x3, luego "fin"
#   mostrar_pedidos()


