import cha

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "how are you": ["I'm good, thanks!", "I'm doing well, how about you?"],
            "goodbye": ["Goodbye!", "See you later!", "Bye!"],
            "default": ["I'm not sure how to respond to that.", "Can you ask me something else?"]
        }

    def respond(self, user_input):
        # Convert input to lowercase for case-insensitive matching
        user_input = user_input.lower()

        # Check if the input matches any known patterns
        for pattern, responses in self.responses.items():
            if pattern in user_input:
                return random.choice(responses)

        # If no specific pattern matches, use a default response
        return random.choice(self.responses["default"])

# Instantiate the chatbot
chatbot = SimpleChatbot()

# Example usage
#user_input = input("You: ")
while user_input.lower() != "exit":
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    user_input = input("You: ")
