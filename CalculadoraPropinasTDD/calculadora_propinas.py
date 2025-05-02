def calcular_propina(monto, porcentaje):
    if monto < 0 or porcentaje < 0:
        raise ValueError("El monto y el porcentaje no pueden ser negativos.")
    propina = monto * (porcentaje / 100)
    total = monto + propina
    return round(propina, 2), round(total, 2)
