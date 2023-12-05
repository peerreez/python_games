def solicitar_palabra(tipo_palabra):
    return input(f"Ingrese un(a) {tipo_palabra}: ")

def mad_libs():
    sustantivo = solicitar_palabra("sustantivo")
    verbo = solicitar_palabra("verbo")
    adjetivo = solicitar_palabra("adjetivo")

    historia = f"Un {adjetivo} {sustantivo} empezó a {verbo} en el parque. Todos se sorprendieron al ver a este {adjetivo} {sustantivo} {verbo} tan inusual."

    print("\n¡La historia resultante es!\n")
    print(historia)

# Llamar a la función principal
mad_libs()
