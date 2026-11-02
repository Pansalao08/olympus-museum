from flask import Flask, render_template, abort, request
from data.sports_db import SPORTS_DATABASE

app = Flask(__name__)

@app.route('/')
def home():
    winter = [s for s in SPORTS_DATABASE.values() if s["category"] == "Invierno"]
    summer = [s for s in SPORTS_DATABASE.values() if s["category"] == "Verano"]
    esports = [s for s in SPORTS_DATABASE.values() if s["category"] == "eSports"]
    return render_template('home.html', winter=winter, summer=summer, esports=esports)

@app.route('/sport/<sport_id>')
def sport_detail(sport_id):
    sport = SPORTS_DATABASE.get(sport_id)
    if not sport:
        abort(404)
    return render_template('sport_detail.html', sport=sport)

@app.route('/quiz')
def quiz():
    # Preguntas del desafío interactivo de Olympus
    questions = [
        {
            "id": 1,
            "question": "¿Quién es el máximo anotador histórico en la historia de la NHL (Hockey sobre Hielo)?",
            "options": ["Alexander Ovechkin", "Wayne Gretzky", "Sidney Crosby", "Mario Lemieux"],
            "answer": "Wayne Gretzky"
        },
        {
            "id": 2,
            "question": "¿Qué institución de eSports ostenta el récord de 4 Títulos Mundiales (Worlds) en League of Legends?",
            "options": ["Fnatic", "Gen.G", "T1 (SKT)", "Invictus Gaming"],
            "answer": "T1 (SKT)"
        },
        {
            "id": 3,
            "question": "¿Cuál es el atleta que ostenta el récord mundial absoluto de los 100 metros planos (9.58s)?",
            "options": ["Carl Lewis", "Eliud Kipchoge", "Usain Bolt", "Sydney McLaughlin"],
            "answer": "Usain Bolt"
        },
        {
            "id": 4,
            "question": "¿Qué club de fútbol europeo es el rey indiscutible con más títulos de la UEFA Champions League?",
            "options": ["AC Milan", "FC Barcelona", "Real Madrid", "Bayern Munich"],
            "answer": "Real Madrid"
        }
    ]
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True, port=5000)