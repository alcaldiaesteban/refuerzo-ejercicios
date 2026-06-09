# Ejercicio 9 - sistema completo con CRUD y reportes

# CRUD = Create (agregar), Read (ver), Update (modificar), Delete (eliminar)
# Este es el ejercicio integrador. Combina todo lo anterior.

# Contexto: sistema de gestión de una tienda de ropa.
# Cada prenda tiene: codigo, nombre, talla, precio, stock

listaPrendas = []

# ── CRUD ──────────────────────────────────────────────────────

# agregar_prenda()
#   - Genera el codigo automático: "PR" + str(len(listaPrendas) + 1)
#   - Valida que no se ingresen nombre ni talla vacíos
#   - Si todo está bien, agrega a listaPrendas

# mostrar_prendas()
#   - Si está vacía: "No hay prendas registradas"
#   - Si no: imprime cada prenda en una línea con todos sus datos

# buscar_prenda(codigo)
#   - Retorna el diccionario de la prenda o None

# modificar_precio(codigo, nuevo_precio)
#   - Busca la prenda y actualiza su precio
#   - Confirma el cambio o muestra "No encontrada"

# eliminar_prenda(codigo)
#   - Busca y elimina la prenda de la lista
#   - Confirma: "Prenda eliminada: [nombre]"
#   - Si no existe: "No encontrada"

# ── REPORTES ──────────────────────────────────────────────────

# reporte()
#   Imprime:
#   - Total de prendas registradas
#   - Prenda más cara y su precio
#   - Prenda con menos stock y su cantidad
#   - Valor total del inventario (precio * stock de cada prenda sumados)

# ── MENÚ ──────────────────────────────────────────────────────

# menu()
#   ===== TIENDA DE ROPA =====
#   1. Agregar prenda
#   2. Ver todas las prendas
#   3. Buscar prenda por código
#   4. Modificar precio
#   5. Eliminar prenda
#   6. Ver reporte
#   0. Salir

# Al final llama: menu()


