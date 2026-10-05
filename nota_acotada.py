# ==========================================
# PROGRAMA DE EVALUACIÓN DE NOTAS ACOTADAS
# ==========================================

nota = 8

# Filtro de seguridad: Acotación del rango (Entre 0 y 20)
if 0 <= nota <= 20:
    if nota >= 10:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Error: La nota ingresada no es válida. Debe estar entre 0 y 20.")
