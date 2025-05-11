from flask import Flask, render_template, request, jsonify
import openai
import os
import math
from dotenv import load_dotenv

app = Flask(__name__)

# Configuración de OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Constantes
G = 9.81          # gravedad (m/s²)
RHO_DEFAULT = 1000  # densidad de referencia (kg/m³)

# Rutas principales
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simulaciones")
def simulaciones():
    return render_template("simulaciones.html")

@app.route("/conceptos")
def conceptos():
    return render_template("conceptos/conceptos.html")

@app.route("/ejercicios")
def ejercicios():
    return render_template("ejercicios/ejercicios.html")

@app.route("/chat-page")
def chat_page():
    return render_template("chat_page.html")

# Endpoint de chat
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente útil para estudiantes de mecánica de fluidos."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=150
        )
        reply = resp.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---- CALCULADORAS ----

@app.route("/calcular/densidad", methods=["POST"])
def calcular_densidad():
    masa = float(request.form["masa"])
    volumen = float(request.form["volumen"])
    densidad = masa / volumen
    return render_template("ejercicios/ejercicios.html",
                           resultado_densidad=f"{densidad:.4g} kg/m³")

@app.route("/convertir/unidades", methods=["POST"])
def convertir_unidades():
    valor = float(request.form["valor"])
    magnitud = request.form["magnitud"]
    origen = request.form["unidad_origen"]
    destino = request.form["unidad_destino"]
    convertido = valor
    if magnitud == "presion":
        if origen == "Pa" and destino == "atm":
            convertido = valor / 101325
        elif origen == "atm" and destino == "Pa":
            convertido = valor * 101325
    # más conversiones pueden añadirse aquí…
    return render_template("ejercicios/ejercicios.html",
                           resultado_conversion=f"{convertido:.0f} {destino}")

@app.route("/calcular/viscosidad", methods=["POST"])
def calcular_viscosidad():
    νn = float(request.form["viscosidad_newtoniana"])
    νnn = float(request.form["viscosidad_nonewtoniana"])
    diff = νnn - νn
    return render_template("ejercicios/ejercicios.html",
                           resultado_viscosidad=f"{diff:.0f} Pa·s")

@app.route("/calcular/presion", methods=["POST"])
def calcular_presion():
    profundidad = float(request.form["profundidad"])
    densidad = float(request.form["densidad"])
    presion = densidad * G * profundidad
    return render_template("ejercicios/ejercicios.html",
                           resultado_presion=f"{presion:.0f} Pa")

@app.route("/calcular/fuerza", methods=["POST"])
def calcular_fuerza():
    area = float(request.form["area"])
    h_media = float(request.form["profundidad_media"])
    densidad = float(request.form["densidad_f"])
    presion = densidad * G * h_media
    fuerza = presion * area
    return render_template("ejercicios/ejercicios.html",
                           resultado_fuerza=f"{fuerza:.0f} N")

@app.route("/calcular/bernoulli", methods=["POST"])
def calcular_bernoulli():
    p1 = float(request.form["p1"])
    v1 = float(request.form["v1"])
    p2 = float(request.form["p2"])
    v2 = math.sqrt(v1**2 + 2 * (p1 - p2) / RHO_DEFAULT)
    return render_template("ejercicios/ejercicios.html",
                           resultado_bernoulli=f"v₂ = {v2:.0f} m/s")

if __name__ == "__main__":
    app.run(debug=True)
