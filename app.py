from flask import Flask, request, send_file, render_template, jsonify
from yt_descarga import busqueda, descargar_mp3, buscar_videos
import os

app = Flask(__name__)

# ---------- RUTAS ----------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    texto = request.form.get("query")

    if not texto:
        return "Entrada vacía", 400

    resultados = buscar_videos(texto)
    return render_template("results.html", resultados=resultados)


@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    if not url:
        return "URL inválida", 400

    try:
        mp3, nombre = descargar_mp3(url)
        return send_file(
            mp3,
            as_attachment=True,
            download_name=nombre,
            mimetype="audio/mpeg"
        )
    except Exception as e:
        return f"Error: {e}", 500


app.run(debug=True)