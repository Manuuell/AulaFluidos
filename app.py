from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Configuración de OpenAI API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ruta para la página de inicio
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/simulaciones")
def simulaciones():
    return render_template("simulaciones.html")
@app.route("/conceptos")
def conceptos():
    return render_template("conceptos/conceptos.html")


# Ruta para la página de chat
@app.route("/chat-page")
def chat_page():
    return render_template("chat_page.html")

# Ruta para manejar las peticiones del chat
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        # Llamada a la API de OpenAI para generar la respuesta
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Cambia a "gpt-4" si tienes acceso a GPT-4
            messages=[
                {"role": "system", "content": "Eres un asistente útil para estudiantes de mecánica de fluidos."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=150
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Inicializa la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
