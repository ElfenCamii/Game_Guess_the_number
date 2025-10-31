### 
# Archivo principal donde se ejecutara el juego
###

# main.py
from game_logic import generar_numero, verificar_intento
from utils import es_numero_valido, mostrar_mensaje

def jugar():
    """
    Ejecuta una partida completa del juego.
    """
    mostrar_mensaje("bienvenida")
    numero = generar_numero()
    intentos = 0

    while True:
        entrada = input("👉 Ingresa un número entre 1 y 100: ").strip()
        if not es_numero_valido(entrada):
            mostrar_mensaje("error")
            continue

        intento = int(entrada)
        intentos += 1
        resultado = verificar_intento(numero, intento)

        if resultado == "mayor":
            mostrar_mensaje("mayor")
        elif resultado == "menor":
            mostrar_mensaje("menor")
        else:
            mostrar_mensaje("ganaste", intentos)
            break

if __name__ == "__main__":
    jugar()
