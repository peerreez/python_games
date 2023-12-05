from random import randint

def generar_numeros_aleatorios():
    return randint(2, 10), randint(2, 10)

def main():
    # Generamos dos números aleatorios que serán los factores de la multiplicación.
    factor1, factor2 = generar_numeros_aleatorios()

    # Calculamos la multiplicación de los números generados.
    solucion = factor1 * factor2

    # Imprimimos la multiplicación y pedimos al usuario la solución.
    print(f"{factor1} x {factor2} = ", end="")
    solucion_de_usuario = int(input())

    # Verificamos si la solución dada por el usuario es correcta.
    if solucion_de_usuario == solucion:
        print("¡Respuesta correcta!")
    else:
        print("¡Respuesta incorrecta!")

if __name__ == "__main__":
    main()
