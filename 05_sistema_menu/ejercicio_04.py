# Ejercicio 4 - mini proyecto: sistema de veterinaria

# Combina todo lo que practicaste:
#   - Listas de diccionarios
#   - Funciones separadas por responsabilidad
#   - Menú while True + match-case
#   - Iteración con .items()

# Cada mascota tiene: id, nombre, especie, dueño, peso

listaMascotas = []

# Implementa estas funciones:

# registrar_mascota()
#   - Pide todos los datos con input
#   - El id se genera automático: "M" + str(len(listaMascotas) + 1)
#     (M1, M2, M3... sin necesidad de que el usuario lo ingrese)
#   - Agrega la mascota a listaMascotas

# mostrar_mascotas()
#   - Recorre la lista con for
#   - Por cada mascota imprime TODAS sus claves y valores usando .items():
#       id: M1
#       nombre: Firulais
#       especie: Perro
#       dueño: Carlos
#       peso: 8.5
#       ----------
#   - Si no hay mascotas: "No hay mascotas registradas"

# buscar_por_dueño(nombre_dueño)
#   - Recorre la lista y muestra todas las mascotas de ese dueño
#   - Si no tiene ninguna: "No se encontraron mascotas para ese dueño"

# mascota_mas_pesada()
#   - Encuentra e imprime la mascota con mayor peso
#   - Muestra su nombre y peso

# menu()
#   ===== VETERINARIA =====
#   1. Registrar mascota
#   2. Ver todas las mascotas
#   3. Buscar mascotas por dueño
#   4. Ver mascota más pesada
#   0. Salir

# Al final llama: menu()


