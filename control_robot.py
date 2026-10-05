# ==========================================
# MENÚ DE CONTROL INTERACTIVO DEL ROBOT
# ==========================================

print("=== MENÚ DE CONTROL DEL ROBOT ===")
print("A. Mover a la derecha")
print("B. Mover a la izquierda")
print("C. Mover hacia el frente")
print("D. Mover hacia atrás")
print("E. Apagar")
print("=================================")

while True:
    opcion = input("\nIngrese un código de comando (A, B, C, D o E): ").upper()
    
    match opcion:
        case "A":
            print("El robot se desplazó a la derecha")
        case "B":
            print("El robot se desplazó a la izquierda")
        case "C":
            print("El robot se desplazó hacia adelante")
        case "D":
            print("El robot se desplazó hacia atrás")
        case "E":
            print("Salir del programa")
            break
        case _:
            print("Comando no reconocido. Intente de nuevo.")
