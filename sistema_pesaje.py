# Sistema de pesaje automático de piezas de metal
pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]

# Contador de piezas válidas
piezas_validas = 0

# Bucle para recorrer la lista de pesos
for peso in pesos_piezas:
    if peso <= 0:
        print(f"Peso {peso}: Error de lectura: Flujo negativo descartado.")
    elif 1 <= peso <= 13:
        print(f"Peso {peso}: Pieza Ligera aprobada.")
        piezas_validas += 1
    elif peso > 13:
        print(f"Peso {peso}: Pieza Pesada aprobada.")
        piezas_validas += 1

# Mostrar el total al final del programa
print("-" * 40)
print(f"Total de piezas válidas aprobadas: {piezas_validas}")
