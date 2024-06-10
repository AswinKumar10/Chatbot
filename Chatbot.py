import random
from nltk.chat.util import Chat, reflections
# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"what is your name?",
        ["You can call me ChatGPT. How can I assist you?",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm fine, thanks for asking.",]
    ],
    [
        r"(.*) (hungry|sleepy)",
        ["I'm just a computer program, so I don't feel hunger or sleepiness.",]
    ],
    [
        r"(.*) age?",
        ["I'm just a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want?",
        ["I'm here to assist you. How can I help you today?",]
    ],
    [
        r"(.*) created you?",
        ["I was created by OpenAI using their GPT-3.5 architecture.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I exist in the digital realm. I don't have a physical location.",]
    ],
    [
        r"how can I (.*) help you?",
        ["You can ask me questions or tell me what you need assistance with.",]
    ],
    [
        r"quit",
        ["Thank you for chatting with me. Have a great day!", "Goodbye!"]
    ],
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)
# Start the conversation
print("Hi! I'm your chatbot assistant. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.respond(user_input)
    print("ChatGPT:", response)