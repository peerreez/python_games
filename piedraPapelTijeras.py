import random

def jugar_ppt(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijeras") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijeras" and jugador2 == "papel"):
        return "Gana Jugador 1"
    else:
        return "Gana Jugador 2"

opciones = ["piedra", "papel", "tijeras"]
jugador1 = random.choice(opciones)
jugador2 = random.choice(opciones)

resultado = jugar_ppt(jugador1, jugador2)

print(f"Jugador 1 eligió: {jugador1}")
print(f"Jugador 2 eligió: {jugador2}")
print(f"Resultado: {resultado}")
