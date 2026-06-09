# Ejercicio 7 - validaciones: evitar duplicados y datos vacíos

# En tu proyecto del restaurante es posible agregar dos platos
# con el mismo código. Eso genera errores. Este ejercicio practica
# cómo validar los datos ANTES de guardarlos.

listaEmpleados = []

# Crea la función codigo_existe(codigo):
#   - Recorre listaEmpleados
#   - Retorna True si ya hay un empleado con ese codigo
#   - Retorna False si no existe

# Crea la función agregar_empleado():
#   - Pide: codigo, nombre, cargo
#   - Valida que el codigo no esté vacío (""):
#       si está vacío -> "El código no puede estar vacío"
#       y no agrega nada
#   - Valida que el nombre no esté vacío:
#       si está vacío -> "El nombre no puede estar vacío"
#       y no agrega nada
#   - Usa codigo_existe() para validar duplicados:
#       si ya existe -> "Ya existe un empleado con ese código"
#       y no agrega nada
#   - Si todo está bien, agrega y confirma:
#       "Empleado Carlos agregado correctamente"

# Crea mostrar_empleados():
#   - Imprime cada empleado: [E01] Carlos - Mesero

# Prueba estas situaciones:
#   agregar_empleado()   <- ingresa código "E01", nombre "Carlos", cargo "Mesero"
#   agregar_empleado()   <- intenta agregar código "E01" de nuevo (duplicado)
#   agregar_empleado()   <- deja el nombre vacío
#   agregar_empleado()   <- ingresa código "E02", nombre "Ana", cargo "Chef"
#   mostrar_empleados()


