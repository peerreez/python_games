import random

def adivina_el_numero():
    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número del 1 al 100")

    # Generar un número aleatorio
    numero_secreto = random.randint(1, 100)

    intentos = 0
    while True:
        # Pedir al usuario que adivine el número
        intento = int(input("Tu adivinanza: "))

        # Incrementar el contador de intentos
        intentos += 1

        # Verificar si el intento es correcto
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número es mayor. ¡Inténtalo de nuevo!")
        else:
            print("El número es menor. ¡Inténtalo de nuevo!")

# Llamar a la función principal
adivina_el_numero()
