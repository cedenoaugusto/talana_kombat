# Talana Kombat JRPG

# Inicializacion
NOMBRE_J1 = "Tonyn"
NOMBRE_J2 = "Arnaldor"

golpe_movimiento = ""
energia_jugador_1 = energia_jugador_2 = 6
ataques_list = []
total_golpes_movimientos_j1 = 0
total_golpes_movimientos_j2 = 0
total_golpes_j1 = 0
total_golpes_j2 = 0
total_movimientos_j1 = 0
total_movimientos_j2 = 0

def obtener_movimientos_combate(elemento=0)->dict:
    if elemento == 0:
        movimientos_combate = {
            "player1": {
                "golpes": [
                    "K",
                    "P",
                    "",
                    "K",
                    "P"
                ],
                "movimientos": [
                    "D",
                    "DSD",
                    "S",
                    "DSD",
                    "SD"
                ]
            },
            "player2": {
                "golpes": [
                    "K",
                    "",
                    "K",
                    "P",
                    "P"
                ],
                "movimientos": [
                    "SA",
                    "SA",
                    "SA",
                    "ASA",
                    "SA"
                ]
            }
        }

    elif elemento == 1:
        movimientos_combate = {
            "player1": {
                "golpes": [
                    "K",
                    "P",
                    "K",
                    "P"
                ],
                "movimientos": [
                    "SDD",
                    "DSD",
                    "SA",
                    "DSD"
                ]
            },
            "player2": {
                "golpes": [
                    "P",
                    "K",
                    "K",
                    "K",
                    "P",
                    "k"
                ],
                "movimientos": [
                    "DSD",
                    "WSAW",
                    "ASA",
                    "",
                    "ASA",
                    "SA"
                ]
            }
        }
    elif elemento == 2:
        movimientos_combate = {
            "player1": {
                "golpes": [
                    "P",
                    ""
                ],
                "movimientos": [
                    "DSD",
                    "S"
                ]
            },
            "player2": {
                "golpes": [
                    "P",
                    "",
                    "P",
                    "K",
                    "K",
                    "K"
                ],
                "movimientos": [
                    "",
                    "ASA",
                    "DA",
                    "AAA",
                    "",
                    "SA"
                ]
            }
        }

    return movimientos_combate


def vizualizacion_preliminar():
    print('\n**************** Talana Kombat JRPG ****************')
    vista_inicio = f"""
    O/       \\O
    |\\       /|
    |         |
    |\\       /|

    {NOMBRE_J1} vs {NOMBRE_J2}
    """
    print(vista_inicio)


def contador_golpes(jugador):
    global total_golpes_j1
    global total_golpes_j2

    if jugador == 'player1':
        total_golpes_j1 += 1
    elif jugador == 'player2':
        total_golpes_j2 += 1

def contador_movimientos(jugador):
    global total_movimientos_j1
    global total_movimientos_j2

    if jugador == 'player1':
        total_movimientos_j1 += 1
    elif jugador == 'player2':
        total_movimientos_j2 += 1


def obtener_valor_ataque(jugador:str, movimiento:str, golpe:str) -> int:
    global total_golpes_movimientos_j1
    global total_golpes_movimientos_j2

    puntaje_anotado = 0
    golpe_movimiento = movimiento.upper() + golpe.upper()

    if jugador == 'player1':
        descripcion_ataque = NOMBRE_J1
        if golpe_movimiento == 'DSDP' or 'DSDP' in golpe_movimiento: # Taladoken
            puntaje_anotado = 3
            descripcion_ataque += ' conecta un Taladoken'
            total_golpes_movimientos_j1 += 1

        elif golpe_movimiento == 'SDK' or 'SDK' in golpe_movimiento: # Remuyuken
            puntaje_anotado = 2
            descripcion_ataque += ' conecta un Remuyuken'
            total_golpes_movimientos_j1 += 1

    else:
        descripcion_ataque = NOMBRE_J2
        if golpe_movimiento == 'SAK' or 'SAK' in golpe_movimiento: # Remuyuken
            puntaje_anotado = 3
            descripcion_ataque += ' conecta un Remuyuken'
            total_golpes_movimientos_j2 += 1

        elif golpe_movimiento == 'ASAP' or 'ASAP' in golpe_movimiento: # Taladoken
            puntaje_anotado = 2
            descripcion_ataque += ' conecta un Taladoken'
            total_golpes_movimientos_j2 += 1

    if puntaje_anotado == 0:
        if 'P' in golpe_movimiento: # Puño
            puntaje_anotado = 1
            descripcion_ataque += ' conecta un puñetazo' # le da un puñetazo al pobre
            # contador_golpes(jugador)

        elif 'K' in golpe_movimiento: # Patada
            puntaje_anotado = 1
            descripcion_ataque += ' conecta una Patada'
            # contador_golpes(jugador)

        else:
            puntaje_anotado = 0
            if golpe_movimiento != '':
                descripcion_ataque += ' se mueve'
                # contador_movimientos(jugador)

            else:
                descripcion_ataque += ' realiza un movimiento no reconocido'
                # contador_movimientos(jugador)

        if 'P' in golpe_movimiento or 'K' in golpe_movimiento:
            contador_golpes(jugador)
        else:
            if golpe != '':
                contador_movimientos(jugador)


    return (golpe_movimiento, puntaje_anotado, descripcion_ataque)


def ataque_jugador_1(ataques_list, i):
    # Info jugador 1
    # print(ataques_list[0][i])
    print(f'{ataques_list[0][i][2]} ({ataques_list[0][i][0]}) (energia actual: {energia_jugador_1})')
    global energia_jugador_2
    energia_jugador_2 -= ataques_list[0][i][1]
    # print("Energia actual del jugador 2:", energia_jugador_2)

    if energia_jugador_2 <= 0:
        detener_combate = True
        ganador = NOMBRE_J1
        energia_ganador = energia_jugador_1
    else:
        detener_combate = False
        ganador = ""
        energia_ganador = None

    return detener_combate, ganador, energia_ganador

def ataque_jugador_2(ataques_list, i):
    # Info jugador 2
    global energia_jugador_1
    
    # print(ataques_list[1][i])
    print(f'{ataques_list[1][i][2]} ({ataques_list[1][i][0]}) (energia actual: {energia_jugador_2})')
    
    energia_jugador_1 -= ataques_list[1][i][1]

    # print("Energia actual del jugador 1:", energia_jugador_1)
    if energia_jugador_1 <= 0:
        detener_combate = True
        ganador = NOMBRE_J2
        energia_ganador = energia_jugador_2
    else:
        detener_combate = False
        ganador = ""
        energia_ganador = None

    return detener_combate, ganador, energia_ganador


def compensar_batalla(ataques_list:list):
    # Antes de iniciar la batalla agrego movimientos vacios para que se pueda realizar la batalla
    rondas_j1 = len(ataques_list[0])
    rondas_j2 = len(ataques_list[1])
    default_tupla_j1 = ('', 0, NOMBRE_J1 + ' parece un vegetal y no se mueve', None, None, None)
    default_tupla_j2 = ('', 0, NOMBRE_J2 + ' parece estar congelado y no se mueve', None, None, None)
    
    if rondas_j1 > rondas_j2:
        dif = rondas_j1 - rondas_j2
        for _ in range(dif):
            ataques_list[1].append(default_tupla_j2)
        
    elif rondas_j1 < rondas_j2:
        dif = rondas_j2 - rondas_j1
        for _ in range(dif):
            ataques_list[0].append(default_tupla_j1)


def iniciar_combate(movimientos_combate):
    vizualizacion_preliminar()

    for jugador in movimientos_combate:
        if len(movimientos_combate[jugador]["golpes"]) == len(movimientos_combate[jugador]["movimientos"]):
            at_list = []
            i=0
            for golpe in movimientos_combate[jugador]["golpes"]:
                golpe_movimiento = obtener_valor_ataque(jugador, movimientos_combate[jugador]["movimientos"][i], golpe)
                at_list.append(golpe_movimiento)
                i+=1
                
            ataques_list.append(at_list)

        else:
            raise Exception("El JSON dado no esta correcto. (La cantidad de golpes debe ser igual a la cantidad de movimientos)")

    compensar_batalla(ataques_list)

    if total_golpes_movimientos_j2 < total_golpes_movimientos_j1:
        inicia_combate = NOMBRE_J2
    elif total_golpes_movimientos_j1 < total_golpes_movimientos_j2:
        inicia_combate = NOMBRE_J1
    else:
        if total_golpes_j2 < total_golpes_j1:
            inicia_combate = NOMBRE_J2
        elif total_golpes_j1 < total_golpes_j2:
            inicia_combate = NOMBRE_J1
        else:
            if total_movimientos_j2 < total_movimientos_j1:
                inicia_combate = NOMBRE_J2
            elif total_movimientos_j1 < total_movimientos_j2:
                inicia_combate = NOMBRE_J1
            else:
                inicia_combate = NOMBRE_J1

    print('Inicia el combate: ', inicia_combate, '\n')


    for i in range(len(ataques_list[0])):
        print("==========================  ", i + 1, "  ==========================", sep="")

        if inicia_combate == NOMBRE_J1:
            detener_combate, ganador, energia = ataque_jugador_1(ataques_list, i)
            if detener_combate:
                break

            detener_combate, ganador, energia = ataque_jugador_2(ataques_list, i)
            if detener_combate:
                break

        else:
            detener_combate, ganador, energia = ataque_jugador_2(ataques_list, i)
            if detener_combate:
                break
            
            detener_combate, ganador, energia = ataque_jugador_1(ataques_list, i)
            if detener_combate:
                break

    # print(ataques_list[0])
    print('=========================================================\n')
    print(f'{ganador} gana la pelea y aun le queda {energia} de energía.\n')




# Obtiene los datos de combate
movimientos_combate = obtener_movimientos_combate()

# Inicia la pelea
iniciar_combate(movimientos_combate)

