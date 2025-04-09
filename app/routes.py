from flask import Blueprint, render_template, request, jsonify
import os
import google.generativeai as genai

main = Blueprint("main", __name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        response = model.generate_content(user_input)
        reply = response.text
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})
