def agendamientoHornos(solicitudesHorneado):
    programacionTurnos = []
    turno = []
    duracionTurnoActual = 0
    
    for horno in solicitudesHorneado:
        if programacionTurnos == [] and duracionTurnoActual == 0 and turno == []:
            turno.append(horno)
            duracionTurnoActual += horno["tiempo"]
        else:
            if duracionTurnoActual+horno["tiempo"] <= 240 and turno[-1]["tf"] <= horno["t0"]:
                turno.append(horno)
                duracionTurnoActual += horno["tiempo"]
            else:
                programacionTurnos.append([turno,duracionTurnoActual])
                turno.append(horno)
                duracionTurnoActual = 0
                duracionTurnoActual += horno["tiempo"]

    if duracionTurnoActual != 0:
        programacionTurnos.append([turno, duracionTurnoActual])
        
    tiempo = 0
    for itinerario in programacionTurnos:
        tiempo += itinerario[-1]    
    ocupacionPromedio = round( tiempo/len(programacionTurnos) , 2 )

    return {'tiempoPromedioHornos':ocupacionPromedio, 'hornosUtilizados':len(programacionTurnos)}

print(agendamientoHornos([{'t0': 2, 'tf': 182, 'tiempo': 180, 'id': 'Tarea19'},
{'t0': 2, 'tf': 144, 'tiempo': 142, 'id': 'Tarea20'}, {'t0': 411, 'tf': 449,
'tiempo': 38, 'id': 'Tarea2'}, {'t0': 474, 'tf': 512, 'tiempo': 38, 'id':
'Tarea14'}, {'t0': 493, 'tf': 515, 'tiempo': 22, 'id': 'Tarea7'}, {'t0': 538,
'tf': 579, 'tiempo': 41, 'id': 'Tarea1'}, {'t0': 550, 'tf': 571, 'tiempo': 21,
'id': 'Tarea4'}, {'t0': 572, 'tf': 589, 'tiempo': 17, 'id': 'Tarea8'}, {'t0':
577, 'tf': 611, 'tiempo': 34, 'id': 'Tarea10'}, {'t0': 580, 'tf': 612, 'tiempo':
32, 'id': 'Tarea13'}, {'t0': 600, 'tf': 628, 'tiempo': 28, 'id': 'Tarea15'},
{'t0': 607, 'tf': 624, 'tiempo': 17, 'id': 'Tarea17'}, {'t0': 619, 'tf': 636,
'tiempo': 17, 'id': 'Tarea18'}, {'t0': 1091, 'tf': 1128, 'tiempo': 37, 'id':
'Tarea16'}, {'t0': 1120, 'tf': 1141, 'tiempo': 21, 'id': 'Tarea3'}, {'t0': 1136,
'tf': 1171, 'tiempo': 35, 'id': 'Tarea5'}, {'t0': 1140, 'tf': 1159, 'tiempo': 19,
'id': 'Tarea6'}, {'t0': 1166, 'tf': 1212, 'tiempo': 46, 'id': 'Tarea11'}, {'t0':
1172, 'tf': 1189, 'tiempo': 17, 'id': 'Tarea12'}, {'t0': 1265, 'tf': 1285,
'tiempo': 20, 'id': 'Tarea9'}]))