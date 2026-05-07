from flask import Flask, render_template, request
import json
import numpy as np
import os
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    return model

# Cargar himnos
with open("himnos_embeddings.json", "r", encoding="utf-8") as f:
    himnos = json.load(f)

HIMNARIOS_RESTRINGIDOS = [
    "Himnos de gracia",
    "Himnos de Gracia",
    "HIMNOS DE GRACIA",
    "Himnos De Gracia",
    "Integrity Music",
    "Magesty Music",
    "The Sing! Hymnal"
]

RESTRINGIDOS_NORMALIZADOS = {h.strip().lower() for h in HIMNARIOS_RESTRINGIDOS}

# Lista de himnarios
himnarios = sorted(list(set(h["himnario"] for h in himnos)))

@app.context_processor
def inject_restringidos():
    return {"restringidos": HIMNARIOS_RESTRINGIDOS}


def similitud(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Clasificación de relevancia
def clasificar_relevancia(score):
    if score >= 0.60:
        return "Alta"
    elif score >= 0.45:
        return "Media"
    else:
        return None

def es_himnario_restringido(nombre):
    return nombre and nombre.strip().lower() in RESTRINGIDOS_NORMALIZADOS


def buscar(query, himnario_filtro=None):
    query_embedding = get_model().encode(query)
    resultados = []

    for himno in himnos:
        if himnario_filtro and himnario_filtro != "Todos":
            if himno["himnario"] != himnario_filtro:
                continue

        score = similitud(query_embedding, himno["embedding"])
        nivel = clasificar_relevancia(score)

        if nivel:  # ignorar bajos
            himno_resultado = dict(himno)
            himno_resultado["es_restringido"] = es_himnario_restringido(himno["himnario"])
            resultados.append((score, nivel, himno_resultado))

    resultados.sort(key=lambda x: x[0], reverse=True)

    return resultados

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    query = ""
    himnario_seleccionado = "Todos"

    if request.method == "POST":
        query = request.form["query"]
        himnario_seleccionado = request.form["himnario"]
        resultados = buscar(query, himnario_seleccionado)

    return render_template(
        "index.html",
        resultados=resultados,
        query=query,
        himnarios=himnarios,
        seleccionado=himnario_seleccionado
    )

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))