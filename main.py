import json

from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

all_messages = []


def print_message(msg):
    print(f"[{msg['sender']}] {msg['time']}: {msg['text']}")


def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S"),
    }
    all_messages.append(new_message)
    save_messages()


# for message in all_messages:
#     print_message(message)

@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/chat")
def display_chat():
    return render_template("form.html")


@app.route("/")
def main_page():
    return "Hello!"


@app.route("/send_message")
def sent_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    return "OK"


DB_FILE = "data/db.json"


def load_messages():
    json_file = open(DB_FILE, "r")
    json.load(json_file)


def save_messages():
    data = {
        "messages": all_messages
    }
    json_file = open(DB_FILE, "w")
    json.dump(data, json_file)
    return


app.run(host="0.0.0.0", port=80)
