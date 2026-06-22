"""
DecodeLabs AI Internship
Task 1: Rule-Based AI Chatbot
Author: Pradumn Patidar
"""

import json
import re
from pathlib import Path

EXIT_COMMANDS = {"bye", "exit", "quit", "stop"}

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def load_intents():
    return json.loads(Path("intents.json").read_text(encoding="utf-8"))

def get_response(user_input, intents):
    user_input = clean_text(user_input)
    for intent in intents.values():
        for pattern in intent["patterns"]:
            pattern = clean_text(pattern)
            if user_input == pattern or pattern in user_input:
                return intent["response"]
    return "Sorry, I could not understand that. Ask about AI, Python, internship, project, resume, or GitHub."

def main():
    intents = load_intents()
    print("=" * 55)
    print("Rule-Based AI Chatbot")
    print("=" * 55)
    print("Ask about: AI, Python, internship, project, resume, GitHub")
    print("Type bye / exit / quit to stop")
    print("-" * 55)
    while True:
        user_input = input("You: ")
        if clean_text(user_input) in EXIT_COMMANDS:
            print("Bot: Goodbye! All the best for your internship.")
            break
        print("Bot:", get_response(user_input, intents))

if __name__ == "__main__":
    main()
