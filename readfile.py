import os
from pathlib import Path
import music_tag 
from yt_descarga import descarga, busquedad

ruta_inicial = Path("C:/Users/luise/OneDrive/Documents/Musica")

audios_malos = []

def pasar(ruta):
    contenido_ruta = os.listdir(ruta)
    for data in contenido_ruta:
        if os.path.isdir(Path.joinpath(ruta,data)):
            pasar(Path.joinpath(ruta,data))      
        else:
            procesando(ruta,data)
        
def procesando(ruta, audio):
    try:
        f = music_tag.load_file(Path.joinpath(ruta,audio))
    except:
        n_audio = audio.replace(".mp3","")
        audios_malos.append(n_audio)
        print("Ruta",ruta,"/", n_audio)

        
"""pasar(ruta_inicial)
print(len(audios_malos))"""

list_link = busquedad(["https://youtu.be/Br9gprofzaU?si=7DpXETfLiMnCIpv3"])
print(len(list_link))

for link in list_link:
    descarga(link)
