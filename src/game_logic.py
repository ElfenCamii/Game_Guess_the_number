### 
# Aquí vive la lógica central del juego: generación del número y comparación del intento.
###

import random

def generar_numero(minimo=1, maximo=100):
    """
    Genera un número aleatorio entre los valores dados.
    """
    return random.randint(minimo, maximo)


def verificar_intento(numero_secreto, intento):
    """
    Compara el número ingresado con el número secreto.
    Devuelve:
        - "mayor" si el número secreto es mayor
        - "menor" si el número secreto es menor
        - "correcto" si el usuario adivinó
    """
    if intento < numero_secreto:
        return "mayor"
    elif intento > numero_secreto:
        return "menor"
    else:
        return "correcto"
