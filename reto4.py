from casosGeneradosP45 import *

def recaudoModelosDefectuosos(caso):
    """Desarrollar aquí el requerimiento. Se recomienda el uso de las funciones, map, filter, 
       reduce y opcionalmente zip, para realizarlo con mayor facilidad."""
    numero=0  
    #1) El número de consignaciones en los cajeros que están fallando (Fuera de Servicio yCerrados).        
    for llave in caso:
        if caso[llave]['estado']=='Fuera de Servicio' or caso[llave]['estado']== 'Cerrado':
            for i in range(len((caso[llave]['transacciones']))):
               if caso[llave]['transacciones'][i]['tipoMovimiento'] == "consignacion":
                numero+=1
    
    #2) Recaudo total de las consignaciones realizadas en los cajeros del numeral (1), con el fin de realizar 
    # una proyección del dinero que podría dejar de recaudarse al tener estos equipos sin operar
    recaudo=0
    for llave in caso:
        if caso[llave]['estado']=='Fuera de Servicio' or caso[llave]['estado']== 'Cerrado':
            for i in range(len((caso[llave]['transacciones']))):
               if caso[llave]['transacciones'][i]['tipoMovimiento'] == "consignacion":
                recaudo+=caso[llave]['transacciones'][i]['monto']
    #3) Listado de modelos (sin repeticiones y en orden ascendente) de los equipos que no están operando
    modelos=set()
    for llave in caso:
        if caso[llave]['estado']=='Fuera de Servicio' or caso[llave]['estado']== 'Cerrado':
            modelos.add(caso[llave]['modeloCajero'])
    modelos=list(modelos)
    modelos.sort()
    
    return {'numeroConsignaciones': numero,'totalRecaudado': recaudo,'listadoModelosFallando': modelos}
print(recaudoModelosDefectuosos(caso1))
print(recaudoModelosDefectuosos(caso2))
print(recaudoModelosDefectuosos(caso3))