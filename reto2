def pronosticoATP(jugador):
    "Desarrollar aqui el pronóstico para los jugadores"
    
    if jugador["Olimpicos"] == "No Participante":
        olimpicos=False
    else: 
        olimpicos=True
    
    nombre = jugador["nombre"]
    sexo = jugador["sexo"]
    PG = jugador["PG"]
    PP = jugador["PP"]
    Ranking_ATP = jugador["Ranking ATP"]
    Dobles_faltas = jugador["Dobles faltas"]
    Torneos_jugados = jugador["Torneos jugados"]
    Saques_perfectos = jugador["Saques perfectos"]

    if sexo=="mujer":
        if PG > PP or Ranking_ATP > 2400:
            if not(Dobles_faltas > 4 and Torneos_jugados > 19):
                if olimpicos:
                    return f"La jugadora {nombre} tiene 0.8 de probabilidad de quedar primera en el ranking ATP"
                else:
                    return f"La jugadora {nombre} tiene 0.65 de probabilidad de quedar primera en el ranking ATP"
            else:
                return f"La jugadora {nombre} tiene 0.5 de probabilidad de quedar primera en el ranking ATP"
        else:
            if Torneos_jugados <= 18 and Dobles_faltas > 5:
                return f"La jugadora {nombre} tiene 0.5 de probabilidad de quedar primera en el ranking ATP"
            else:
                return f"La jugadora {nombre} tiene 0.6 de probabilidad de quedar primera en el ranking ATP"
    else:
        if olimpicos:
            if PG > PP and Torneos_jugados > 17:
                if Dobles_faltas < 4 or Saques_perfectos > 7:
                    return f"El jugador {nombre} tiene 0.8 de probabilidad de quedar primero en el ranking ATP"
                else: 
                    return f"El jugador {nombre} tiene 0.7 de probabilidad de quedar primero en el ranking ATP"
            else:
                if Ranking_ATP > 2400:
                    return f"El jugador {nombre} tiene 0.65 de probabilidad de quedar primero en el ranking ATP"
                else:
                    return f"El jugador {nombre} tiene 0.55 de probabilidad de quedar primero en el ranking ATP"
        else:
            if Ranking_ATP > 2200 or Torneos_jugados > 18:
                if Dobles_faltas < 4 and PG > PP:
                    return f"El jugador {nombre} tiene 0.55 de probabilidad de quedar primero en el ranking ATP"
                else:
                    return f"El jugador {nombre} tiene 0.45 de probabilidad de quedar primero en el ranking ATP"
            else:
                 return f"El jugador {nombre} tiene 0.35 de probabilidad de quedar primero en el ranking ATP"   


jugador1={"nombre":"Serena Williams", "sexo": "mujer","PG" : 5,"PP":2, "Olimpicos": "Oro", "Ranking ATP": 3000, "Dobles faltas" : 3, "Torneos jugados": 23, "Saques perfectos": 10}
jugador2={"nombre":"Roger Federer", "sexo": "hombre","PG" : 5,"PP": 3,"Olimpicos": "Plata", "Ranking ATP": 2200, "Dobles faltas" : 5, "Torneos jugados": 18, "Saques perfectos": 6}
jugador3={"nombre":"Simona Halep", "sexo": "mujer","PG" : 2,"PP": 3,"Olimpicos": "Plata", "Ranking ATP": 2200, "Dobles faltas" : 6, "Torneos jugados": 18, "Saques perfectos": 10}
jugador4={"nombre": "Yannick Hanfmann", "sexo": "hombre","PG" :1,"PP": 7, "Olimpicos": "No Participante", "Ranking ATP": 819, "Dobles faltas" :7, "Torneos jugados": 10, "Saques perfectos": 2}

print(pronosticoATP(jugador1))
print(pronosticoATP(jugador2))
print(pronosticoATP(jugador3))
print(pronosticoATP(jugador4))
