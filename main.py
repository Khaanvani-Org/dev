class SimpleChatbot:
    def respond(self, user_input):
        if "hello" in user_input.lower():
            return "Hi there! How can I help you?"
        else:
            return "I'm a simple chatbot. I may not understand everything. Ask me anything!"

