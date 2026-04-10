from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

def chatbot(user_input):
    user_input = user_input.lower()

    if "bye" in user_input:
        return "Goodbye! Have a nice day."

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 What's your plan today?"

    elif "how are you" in user_input:
        return "I'm just code but I'm doing great!"

    elif "your name" in user_input:
        return "I'm your flight booking assistant ✈️"

    elif "help" in user_input:
        return "I can help you with flight booking. Try typing 'flight'"

    elif "flight" in user_input:
        return "Tell me destination (Goa, London, USA, Bangalore)"

    elif "goa" in user_input:
        return "Flights to Goa start from ₹3,000–₹6,000"

    elif "bangalore" in user_input:
        return "Flights to Bangalore start from ₹2,500"

    elif "london" in user_input:
        return "Flights to London start from ₹45,000"

    elif "usa" in user_input:
        return "Flights to USA start from ₹41,000"

    else:
        return "Sorry, I didn't understand. Try 'help'"


@app.route("/")
def home():
    return send_from_directory(".", "project.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")
    response = chatbot(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    print("Chatbot is running! Visit http://127.0.0.1:5000 in your browser.")
    print("Serving project.html file")
    app.run(debug=True)