import requests
from bs4 import BeautifulSoup

URL_NOTICIAS = "https://rsshub.app/hoyolab/news/es-mx/2/1"

# Aquí guardaremos el sistema de noticias de Teyvat News
def revisar_noticias():
    respuesta = requests.get(URL_NOTICIAS)

    if respuesta.status_code == 200:
        pagina = BeautifulSoup(respuesta.text, "html.parser")
        return pagina.title.text

    return "❌ No se pudo conectar con HoYoverse."
