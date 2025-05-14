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
    raise NotImplementedError


def acciones(tablero):
    """
    Retorna el conjunto de todas las acciones posibles (i, j) disponibles en el tablero.
    """
    raise NotImplementedError


def resultado(tablero, accion):
    """
    Retorna el tablero que resulta de realizar el movimiento (i, j) en el tablero.
    """
    raise NotImplementedError


def ganador(tablero):
    """
    Retorna el ganador del juego, si lo hay.
    """
    raise NotImplementedError


def final(tablero):
    """
    Retorna True si el juego ha terminado, False en caso contrario.
    """
    raise NotImplementedError


def utilidad(tablero):
    """
    Retorna 1 si X ha ganado, -1 si O ha ganado, 0 en otro caso.
    """
    raise NotImplementedError


def minimax(tablero):
    """
    Retorna la acción óptima para el jugador actual en el tablero.
    """
    raise NotImplementedError
