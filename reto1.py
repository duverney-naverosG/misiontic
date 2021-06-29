def empaquetador (porcentajeAjuste, largo1, largo2, largo3, largo4):
    piezasAprobadas = 0
    areaEmpaquetado = 0
    #area de todas la piezas 
    areaLado1 = largo1 * largo1
    areaLado2 = largo2 * largo2
    areaLado3 = largo3 * largo3
    areaLado4 = largo4 * largo4
    #area promedio 
    AreaPromedio = (areaLado1 + areaLado2 + areaLado3 + areaLado4) / 4
    #diferencia permitida 
    DiferenciaPermitida = porcentajeAjuste * AreaPromedio

    diferenciaArea1 = abs(AreaPromedio - areaLado1)
    if diferenciaArea1 <= DiferenciaPermitida:
        piezasAprobadas+=1
        areaEmpaquetado += areaLado1

    diferenciaArea2 = abs(AreaPromedio - areaLado2)
    if diferenciaArea2 <= DiferenciaPermitida:
        piezasAprobadas+=1
        areaEmpaquetado += areaLado2
    
    diferenciaArea3 = abs(AreaPromedio - areaLado3)
    if diferenciaArea3 <= DiferenciaPermitida:
        piezasAprobadas+=1
        areaEmpaquetado += areaLado3
    
    diferenciaArea4 = abs(AreaPromedio - areaLado4)
    if diferenciaArea4 <= DiferenciaPermitida:
        piezasAprobadas+=1
        areaEmpaquetado += areaLado4
    
    if piezasAprobadas >= 2:
        return f"Embalaje confirmado: piezas aprobadas = {piezasAprobadas}, superficie ocupada = {areaEmpaquetado}"
    else: 
        return f"Embalaje descartado {4 - piezasAprobadas} piezas no ajustan"

print(empaquetador(0.2, 30, 30, 30, 30))
print(empaquetador(0.5, 30, 10, 20, 25))
print(empaquetador(0.8, 30, 10, 20, 25))
print(empaquetador(0.8, 30, 10, 5, 30))