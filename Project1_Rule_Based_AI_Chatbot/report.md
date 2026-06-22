# Report: Rule-Based AI Chatbot

## Introduction
A rule-based chatbot is a basic AI system that uses predefined rules and responses to simulate human interaction.

## Objective
The objective is to create a chatbot that handles greetings, predefined questions, fallback responses, and exit commands.

## Methodology
1. User enters a message.
2. Input is cleaned using lowercase conversion and symbol removal.
3. The message is matched with predefined patterns from `intents.json`.
4. If a match is found, the chatbot returns a response.
5. If no match is found, a fallback response is shown.
6. The loop continues until the user enters an exit command.

## Requirements Covered
- Continuous loop
- Input sanitization
- 5+ intents
- Fallback response
- Exit command
- Rule-based decision making

## Conclusion
This project helped in understanding the foundation of AI logic using control flow and predefined rules.
