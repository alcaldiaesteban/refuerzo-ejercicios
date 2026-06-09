# Ejercicio 6 - eliminar registros de una lista

# Para eliminar un elemento de una lista de diccionarios hay que:
# 1. Encontrar el índice del elemento (su posición en la lista)
# 2. Usar lista.pop(indice) para quitarlo
#
# Ejemplo:
#   frutas = ["manzana", "pera", "uva"]
#   frutas.pop(1)   -> elimina "pera", queda ["manzana", "uva"]

listaTareas = []

# 1. Crea agregar_tarea():
#    - El id se genera automático: len(listaTareas) + 1
#    - Pide la descripción con input
#    - El estado empieza siempre en "pendiente"
#    - Agrega a listaTareas

# 2. Crea mostrar_tareas():
#    - Si no hay tareas: "No hay tareas"
#    - Si hay, imprime cada una así:
#        [1] Estudiar Python - pendiente
#        [2] Hacer ejercicio - completada

# 3. Crea eliminar_tarea(id_tarea):
#    - Recorre la lista buscando la tarea con ese id
#    - Si la encuentra, usa .pop() para eliminarla y confirma:
#        "Tarea eliminada: Estudiar Python"
#    - Si no existe: "Tarea no encontrada"

# 4. Crea completar_tarea(id_tarea):
#    - Busca la tarea por id
#    - Cambia su estado a "completada"
#    - Confirma: "Tarea marcada como completada"

# 5. Prueba el flujo completo:
#    - Agrega 3 tareas
#    - Muéstralas
#    - Completa la tarea con id 2
#    - Elimina la tarea con id 1
#    - Muestra la lista final


