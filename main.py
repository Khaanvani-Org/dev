
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
    try:
        user_input = input("You: ")
        # Do something with user input
        # ...
    except EOFError:
        print("Input error: please enter some text.")
        continue
    else:
        break


    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)
