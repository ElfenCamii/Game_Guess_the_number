### 
# Funciones de apoyo: validaciones y mensajes reutilizables.
###

# utils.py

def es_numero_valido(entrada):
    """
    Verifica si la entrada del usuario es un número entero válido.
    Devuelve True si es válido, False si no.
    """
    return entrada.isdigit()


def mostrar_mensaje(tipo, intentos=None):
    """
    Muestra mensajes comunes según el tipo.
    """
    mensajes = {
        "bienvenida": "🎯 ¡Bienvenido al juego de Adivina el Número!",
        "mayor": "🔼 El número secreto es mayor.",
        "menor": "🔽 El número secreto es menor.",
        "error": "❌ Por favor, ingresa un número válido.",
        "ganaste": f"🎉 ¡Correcto! Lo adivinaste en {intentos} intentos."
    }
    # Si el mensaje necesita mostrar intentos, lo genera dinámicamente
    if tipo == "ganaste" and intentos is not None:
        print(f"🎉 ¡Correcto! Lo adivinaste en {intentos} intentos.")
    else:
        print(mensajes.get(tipo, ""))
