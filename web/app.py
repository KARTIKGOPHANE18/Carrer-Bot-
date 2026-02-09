from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    # Temporary mock response (until quota resets)
    bot_reply = f"🤖 CareerBot: I received your message -> '{user_msg}'. API will be connected soon 🚀"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

