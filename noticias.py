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

    if respuesta.status_code != 200:
        return None

    datos = respuesta.json()

    post = datos["data"]["list"][0]["post"]

    titulo = post["subject"]
    print(post.keys())

    post_id = post["post_id"]
    url = f"https://www.hoyolab.com/article/{post_id}"

    if post_id == ULTIMA_NOTICIA:
        return None

    imagen = post.get("cover")

    contenido = "No se pudo obtener el contenido completo."

    try:
        pagina = requests.get(url)

        if pagina.status_code == 200:
            sopa = BeautifulSoup(pagina.text, "html.parser")

            parrafos = sopa.find_all("p")

            texto = []

            for parrafo in parrafos:
                if parrafo.text.strip():
                    texto.append(parrafo.text.strip())

            if texto:
                contenido = "\n\n".join(texto)

    except Exception:
        pass

    ULTIMA_NOTICIA = post_id

    with open(ARCHIVO_MEMORIA, "w") as archivo:
        archivo.write(post_id)

    return {
        "titulo": titulo,
        "url": url,
        "imagen": imagen,
        "contenido": contenido
    }
