import requests

def obtener_datos_clima(ciudad):
    url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": ciudad,
        "units": "metric",
        "APPID": "50ff42ffd87463e3fc038c0166616d7a"
    }

    try:
        # Realizamos la petición y manejamos errores
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()

        # Si la respuesta devuelve el código de estado 200, todo ha ido bien
        datos = respuesta.json()["main"]
        imprimir_datos_clima(datos)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos del clima: {e}")

def imprimir_datos_clima(datos):
    # Se obtienen los valores del diccionario y se imprimen
    print("La temperatura actual es: {} ºC".format(datos["temp"]))
    print("La sensación térmica es: {} ºC".format(datos["feels_like"]))
    print("La temperatura mínima es: {} ºC".format(datos["temp_min"]))
    print("La temperatura máxima es: {} ºC".format(datos["temp_max"]))
    print("La presión es: {} hPa".format(datos["pressure"]))
    print("La humedad es: {} %".format(datos["humidity"]))

if __name__ == "__main__":
    # Pedimos el nombre de la ciudad por teclado
    ciudad = input("Dime el nombre de una ciudad: ")
    obtener_datos_clima(ciudad)
