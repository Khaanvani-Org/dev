class Chatbot:
    def respond(self, user_input):
        if "hello" in user_input.lower():
            return "Hi there!"
        else:
            return "I don't understand."

# Example usage
chatbot = Chatbot()

user_input = input("You: ")
while user_input.lower() != "exit":
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    user_input = input("You: ")
