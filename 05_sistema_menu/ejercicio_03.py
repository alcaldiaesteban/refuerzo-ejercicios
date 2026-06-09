# Ejercicio 3 - menú con while True y match-case

# En tu proyecto el menú principal funciona así:
#   while True:
#       mostrar opciones
#       opc = input(...)
#       match opc:
#           case "1": funcion1()
#           case "0": break
#
# Este ejercicio practica ese patrón con una agenda de contactos.

listaContactos = []

# Crea estas funciones de soporte:

# agregar_contacto()  -> pide nombre y telefono, guarda en listaContactos

# mostrar_contactos() -> imprime todos los contactos
#                        si está vacía: "No hay contactos"

# buscar_contacto()   -> pide un nombre, busca en la lista, muestra el teléfono

# Luego crea menu() con este menú:
#
#   ===== AGENDA =====
#   1. Agregar contacto
#   2. Ver todos los contactos
#   3. Buscar contacto
#   0. Salir
#   Elige una opción:
#
# Usa while True + match-case para manejar las opciones.
# Al elegir 0, imprime "Hasta luego!" y termina.
# Si elige una opción inválida, imprime "Opción no válida".

# Al final llama: menu()


