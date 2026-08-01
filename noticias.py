import requests
from bs4 import BeautifulSoup

URL_NOTICIAS = "https://bbs-api-os.hoyolab.com/community/post/wapi/getNewsList?gids=2&type=1&page_size=1"

# Aquí guardaremos el sistema de noticias de Teyvat News
def revisar_noticias():
    respuesta = requests.get(URL_NOTICIAS)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos["data"]["list"][0]["post"]["subject"]

    return "❌ No se pudo conectar con HoYoverse."
