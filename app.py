from flask import Flask, render_template, request, jsonify
from chatbot_agent import get_chatbot_response
from speakllm import speak
app = Flask(__name__)
chat_history = []
@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    if request.method == "POST":
        user_input = request.form["user_input"]  
        bot_response = get_chatbot_response(user_input)
        chat_history.append({"sender": "user", "text": user_input})
        chat_history.append({"sender": "bot", "text": bot_response})
    return render_template("index.html", messages=chat_history)

@app.route("/speak", methods=["POST"])
def speak_route():
    user_input = request.form.get("user_input", "").strip()
    if not user_input:
        return "No input received", 400

    bot_response = get_chatbot_response(user_input)


    speak(bot_response)

    chat_history.append({"sender": "user", "text": user_input})
    chat_history.append({"sender": "bot", "text": bot_response})

    
    return render_template("index.html", messages=chat_history)



if __name__ == "__main__":
    app.run(debug=True)

