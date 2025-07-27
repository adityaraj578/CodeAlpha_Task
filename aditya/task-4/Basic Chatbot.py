# Step 1: Define chatbot responses
def get_bot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm just a bot, but I'm doing great! 😊"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day! 👋"
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple rule-based chatbot created in Python!"
    else:
        return "Sorry, I didn't understand that. 🤖 Try saying 'hello', 'how are you', or 'bye'."

# Step 2: Chat loop
print("💬 Welcome to the Basic Chatbot!")
print("Type 'bye' to end the conversation.\n")

while True:
    user_message = input("You: ")
    response = get_bot_response(user_message)
    print("Bot:", response)
    
    if user_message.lower() in ["bye", "goodbye"]:
        break
