import os
from flask import Flask, render_template, request, session, redirect, url_for
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
if not HF_TOKEN:
    raise ValueError("HUGGINGFACE_API_KEY not found in .env file!")

# Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for session

# OpenAI-compatible Hugging Face client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)

MODEL_NAME = "zai-org/GLM-4.6:novita"  # Chat-capable model

# Function to ask question with conversation memory
def ask_question(question):
    if "messages" not in session:
        session["messages"] = []

    # Add user question to messages
    session["messages"].append({"role": "user", "content": question})

    try:
        # Call the model
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=session["messages"]
        )
        # Get AI response
        answer = completion.choices[0].message.content

        # Add AI response to messages
        session["messages"].append({"role": "assistant", "content": answer})

        return answer
    except Exception as e:
        return f"Error: {e}"

# Routes
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    question = request.form.get("question")
    if not question:
        return redirect(url_for("index"))

    answer = ask_question(question)
    conversation = session.get("messages", [])
    return render_template("result.html", question=question, answer=answer, conversation=conversation)

@app.route("/reset", methods=["GET"])
def reset():
    session.pop("messages", None)  # Clear conversation
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
