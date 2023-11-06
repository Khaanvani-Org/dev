class Chatbot:
    def respond(self, user_input):
        if "hello" in user_input.lower():
            return "Hi there!"
        else:
            return "I don't understand."
