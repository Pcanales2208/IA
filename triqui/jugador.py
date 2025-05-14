"""
Jugador de Triqui
"""

import math

X = "X"
O = "O"
VACIO = None


def estado_inicial():
    """
    Retorna el estado inicial del tablero.
    """
    return [[VACIO, VACIO, VACIO],
            [VACIO, VACIO, VACIO],
            [VACIO, VACIO, VACIO]]


def jugador(tablero):
    """
    Retorna el jugador que tiene el siguiente turno en el tablero.
    """
    x_count = sum(row.count(X) for row in tablero)
    o_count = sum(row.count(O) for row in tablero)
    return X if x_count <= o_count else O


def acciones(tablero):
    """
    Retorna el conjunto de todas las acciones posibles (i, j) disponibles en el tablero.
    """
    return {(i, j) for i in range(3) for j in range(3) if tablero[i][j] == VACIO}


def resultado(tablero, accion):
    """
    Retorna el tablero que resulta de realizar el movimiento (i, j) en el tablero.
    """
    i, j = accion
    if tablero[i][j] is not VACIO:
        raise ValueError("La acción no es válida.")
    
    nuevo_tablero = [fila[:] for fila in tablero]
    nuevo_tablero[i][j] = jugador(tablero)
    return nuevo_tablero


def ganador(tablero):
    """
    Retorna el ganador del juego, si lo hay.
    """
    for i in range(3):
        # Verificar filas y columnas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] is not VACIO:
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] is not VACIO:
            return tablero[0][i]
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] is not VACIO:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] is not VACIO:
        return tablero[0][2]
    
    return None


def final(tablero):
    """
    Retorna True si el juego ha terminado, False en caso contrario.
    """
    return ganador(tablero) is not None or all(VACIO not in fila for fila in tablero)


def utilidad(tablero):
    """
    Retorna 1 si X ha ganado, -1 si O ha ganado, 0 en otro caso.
    """
    ganador_juego = ganador(tablero)
    if ganador_juego == X:
        return 1
    elif ganador_juego == O:
        return -1
    else:
        return 0


def minimax(tablero):
    """
    Retorna la acción óptima para el jugador actual en el tablero.
    """
    turno = jugador(tablero)

    def max_valor(tablero):
        if final(tablero):
            return utilidad(tablero)
        v = -math.inf
        for accion in acciones(tablero):
            v = max(v, min_valor(resultado(tablero, accion)))
        return v

    def min_valor(tablero):
        if final(tablero):
            return utilidad(tablero)
        v = math.inf
        for accion in acciones(tablero):
            v = min(v, max_valor(resultado(tablero, accion)))
        return v

    if turno == X:
        _, accion_optima = max((min_valor(resultado(tablero, accion)), accion) for accion in acciones(tablero))
    else:
        _, accion_optima = min((max_valor(resultado(tablero, accion)), accion) for accion in acciones(tablero))
    
    return accion_optima
