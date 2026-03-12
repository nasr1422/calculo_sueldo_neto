# ----------------------------------------
# Programa para calcular sueldo neto
# Basado en porcentajes de RD
# ----------------------------------------

# Constantes (porcentajes)
TSS = 0.0591        # Seguridad Social 5.91%
ISR = 0.15          # Impuesto Sobre la Renta 15%
BONIFICACION = 0.10 # Bonificación 10%

# Solicitar datos al usuario
sueldo_bruto = float(input("Ingrese el sueldo bruto del empleado: "))
otros_descuentos = float(input("Ingrese otros descuentos: "))

# Validación
if sueldo_bruto <= 0:
    print("Error: El sueldo bruto debe ser mayor que 0.")
else:

    # Cálculo de seguridad social
    descuento_tss = sueldo_bruto * TSS

    # Cálculo de ISR
    descuento_isr = sueldo_bruto * ISR

    # Cálculo de bonificación
    bonificacion = sueldo_bruto * BONIFICACION

    # Total de descuentos
    total_descuentos = descuento_tss + descuento_isr + otros_descuentos

    # Sueldo neto
    sueldo_neto = sueldo_bruto - total_descuentos + bonificacion

    # Mostrar resultados
    print("\n----- RESULTADOS -----")
    print("Sueldo Bruto: ", sueldo_bruto)
    print("Descuento Seguridad Social:", descuento_tss)
    print("Retención ISR:", descuento_isr)
    print("Otros Descuentos:", otros_descuentos)
    print("Bonificación:", bonificacion)
    print("Sueldo Neto:", sueldo_neto)