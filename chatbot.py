def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."
    elif user_input == "what can you do":
        return "I can respond to basic messages."
    elif user_input == "thanks" or user_input == "thank you":
        return "You're welcome!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


print("================================")
print("       BASIC CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if user_input.lower().strip() == "bye":
        break