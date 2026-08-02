import requests

URL_NOTICIAS = "https://bbs-api-os.hoyolab.com/community/post/wapi/getNewsList?gids=2&type=1&page_size=1"
URL_POST = "https://bbs-api-os.hoyolab.com/community/post/wapi/getPostFull"

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
    post_id = post["post_id"]
    url = f"https://www.hoyolab.com/article/{post_id}"

    if post_id == ULTIMA_NOTICIA:
        return None

    imagen = post.get("cover")

    contenido = "No se pudo obtener el contenido completo."

    try:
        detalle = requests.get(
            URL_POST,
            params={"post_id": post_id}
        )

        if detalle.status_code == 200:
            datos_post = detalle.json()

            contenido = datos_post["data"]["post"]["content"]

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
