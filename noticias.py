import requests
from bs4 import BeautifulSoup

URL_NOTICIAS = "https://bbs-api-os.hoyolab.com/community/post/wapi/getNewsList?gids=2&type=1&page_size=1"
ULTIMA_NOTICIA = None
ARCHIVO_MEMORIA = "ultima_noticia.txt"

def revisar_noticias():
    global ULTIMA_NOTICIA

    try:
        with open(ARCHIVO_MEMORIA, "r") as archivo:
            ULTIMA_NOTICIA = archivo.read()
    except FileNotFoundError:
        pass

    respuesta = requests.get(URL_NOTICIAS)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        titulo = datos["data"]["list"][0]["post"]["subject"]
        post_id = datos["data"]["list"][0]["post"]["post_id"]
        url = f"https://www.hoyolab.com/article/{post_id}"

        imagen = datos["data"]["list"][0]["post"]["cover"]

        if not imagen:
            imagenes = datos["data"]["list"][0]["post"]["images"]

            if imagenes:
                imagen = imagenes[0]

        if post_id == ULTIMA_NOTICIA:
            return None

        ULTIMA_NOTICIA = post_id

        with open(ARCHIVO_MEMORIA, "w") as archivo:
            archivo.write(post_id)

        return {
            "titulo": titulo,
            "url": url,
            "imagen": imagen
        }

    return None
