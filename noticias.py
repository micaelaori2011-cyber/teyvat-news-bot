import requests
URL_NOTICIAS = "https://www.hoyolab.com/circles/2/27/official"
# Aquí guardaremos el sistema de noticias de Teyvat News
def revisar_noticias():
    respuesta = requests.get(URL_NOTICIAS)
    if respuesta.status_code == 200:
        return respuesta.text[:500]
    else:
        return "❌ No se pudo conectar con HoYoverse."
