#import random

class Chatbot:
    def respond(self, user_input):
        user_input_lower = user_input.lower()

        if "hello" in user_input_lower:
            return "Hi there!"
        elif "how are you" in user_input_lower:
            return "I'm doing well, thank you. How about you?"
        elif "goodbye" in user_input_lower:
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
    #user_input = input("You: ")

   # if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

 
