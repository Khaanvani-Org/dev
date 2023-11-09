
import main  
class Chatbot:
    def respond(self, user_input):
        if "hello" in user_input.lower():
            return "Hi there!"
        else:
            return "I don't understand."

# Instantiate the chatbot
chatbot = Chatbot()

# Conversation loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)
