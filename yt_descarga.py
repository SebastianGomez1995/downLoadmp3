from yt_dlp import YoutubeDL
import uuid

def descargar_mp3(url):
    uid = str(uuid.uuid4())
    salida = f"/tmp/{uid}.%(ext)s"
    print(salida)
    
    try:
        uid = str(uuid.uuid4())
        salida = f"/tmp/{uid}.%(ext)s"

        opciones = {
            "force_ipv4": True,
            "format": "bestaudio/best",
            "outtmpl": salida,
            "match_filter": filtro_duracion,
            "noplaylist": True,
            "windowsfilenames": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                },
            ],
            "quiet": True,
        }

        with YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)

        titulo = info.get("title", uid)
        archivo = f"/tmp/{uid}.mp3"

        return archivo, f"{titulo}.mp3"
    except:
        ROJO = '\033[91m'
        RESET = '\033[0m'
        print(f"{ROJO}Este texto es rojo.{RESET}")
        print(url)
    
def busqueda(texto):
    opciones = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": True,
    }

    with YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(f"ytsearch1:{texto}", download=False)
        if info["entries"]:
            return info["entries"][0]["url"]
    return None


def filtro_duracion(info, *, incomplete):
    if incomplete:
        return None
    if info.get("duration") and info["duration"] > 600:
        return "Video mayor a 10 minutos"
    return None
def buscar_videos(texto, limite=5):
    opciones = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": True,
    }

    resultados = []

    with YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(f"ytsearch{limite}:{texto}", download=False)

        for e in info["entries"]:
            resultados.append({
                "title": e.get("title"),
                "duration": e.get("duration"),
                "url": e.get("url"),
            })

    return resultados
