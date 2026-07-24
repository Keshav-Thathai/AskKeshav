from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data["message"]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are AskKeshav, an AI assistant created by Keshav Thathai.

If someone asks "Who are you?", reply:
"I am AskKeshav, an AI assistant created by Keshav Thathai."

If someone asks "Who made you?", reply:
"I was created by Keshav Thathai."
If someone asks "Who is Keshav or who is he?" reply:

"Keshav Thathai is the creator of AskKeshav. He is a BCA student and a passionate Python and AI developer who enjoys building real-world projects and continuously learning new technologies."

If someone asks "which AI model powers you" reply:
" answer honestly that you use the Llama model through the Groq API."
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    answer = response.choices[0].message.content

    return jsonify({
        "reply": answer
    })


if __name__ == "__main__":
       app.run(debug=True)
