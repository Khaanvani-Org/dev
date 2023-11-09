import random

class Chatbot:
    def __init__(self):
        self.goodbye_commands = ["exit", "bye", "quit"]

    def respond(self, user_input):
        user_input_lower = user_input.lower()

        if "hello" in user_input_lower:
            return "Hi there!"
        elif "how are you" in user_input_lower:
            return "I'm doing well, thank you. How about you?"
        elif any(command in user_input_lower for command in self.goodbye_commands):
            return "Goodbye! Have a great day!"
        elif "joke" in user_input_lower:
            return self.tell_joke()
        else:
            return "I don't understand. Can you ask me something else?"

    def tell_joke(self):
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call fake spaghetti? An impasta!",
            "Why don't scientists trust atoms? Because they make up everything!"
        ]
        return random.choice(jokes)

# Instantiate the chatbot
chatbot = Chatbot()

# Conversation loop
while True:
  

    # Check if the user wants to exit
    if any(command in user_input.lower() for command in chatbot.goodbye_commands):
        print("Chatbot: Goodbye!")
        break

    # Get the chatbot's response
    response = chatbot.respond(user_input)
    
    # Print the chatbot's response
    print("Chatbot:", response)

    # Handle jokes separately for more interactive conversations
    if "joke" in user_input.lower():
        response = chatbot.tell_joke()
        print("Chatbot:", response)

    # Add more specific response handling based on user input if needed
    # ...

    # Continue the conversation loop
