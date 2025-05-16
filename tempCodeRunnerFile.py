@app.route("/speak", methods=["POST"])
# def speak_route():
#     user_input = request.form.get("user_input", "").strip()
#     if not user_input:
#         return "No input received", 400

#     bot_response = get_chatbot_response(user_input)

#     # Call the speak function to say bot_response aloud on server
#     speak(bot_response)

#     chat_history.append({"sender": "user", "text": user_input})
#     chat_history.append({"sender": "bot", "text": bot_response})

#     # Return the updated page or JSON
#     return render_template("index.html", messages=chat_history)