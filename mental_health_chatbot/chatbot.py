import random

def detect_mood(user_input):
    responses = {
        "sad": [
            "I'm really sorry you're feeling that way. You're not alone 🤍",
            "It's okay to feel sad sometimes. I'm here with you 💙",
            "Sending you a big virtual hug 🤗"
        ],
        "happy": [
            "That's wonderful to hear! 😊",
            "Yay! I'm glad you're feeling good 🌈",
            "Keep shining bright! 🌟"
        ],
        "stressed": [
            "It’s okay to feel stressed. Take a deep breath 🌿",
            "You’ve got this, one step at a time 🧘",
            "Try to take a small break — you deserve it ☕"
        ],
        "anxious": [
            "You're strong for pushing through anxiety. You're not alone 🤝",
            "Try focusing on your breath. You're doing great 🫶",
            "I'm here with you. One moment at a time 💛"
        ],
        "angry": [
            "It’s okay to feel anger. I'm here if you want to talk about it 🔥",
            "Let it out — it's healthy to express it 💢",
            "I'm here to listen, no judgment 🧡"
        ],
        "help": [
            "You're doing great for reaching out. Would talking to someone help? ❤️",
            "I'm proud of you for asking. Let’s take it slow together 💬",
            "Asking for help is a brave first step 🌼"
        ]
    }

    # Define keyword groups
    keyword_groups = {
        "sad": ["sad", "down", "depressed", "unhappy"],
        "happy": ["happy", "good", "joyful", "excited", "content"],
        "stressed": ["stressed", "overwhelmed", "pressured", "tense"],
        "anxious": ["anxious", "nervous", "worried", "panicking"],
        "angry": ["angry", "mad", "frustrated", "furious"],
        "help": ["help", "support", "assist", "guidance"]
    }

    # Search for any keyword in user input
    for mood, keywords in keyword_groups.items():
        for keyword in keywords:
            if keyword in user_input.lower():
                return random.choice(responses[mood])
    
    return None


# Chat Loop
print("👋 Hello! I'm your Mental Health Chatbot.")
print("You can talk to me about how you're feeling.")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Take care! I'm here whenever you need to talk. 💙")
        break

    mood_response = detect_mood(user_input)
    if mood_response:
        print("Bot:", mood_response)
    else:
        print("Bot: I may not understand everything, but I'm here to listen 🫶")
