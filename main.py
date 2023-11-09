import openai

class GeneralChatbot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def respond(self, user_input):
        prompt = f"User: {user_input}\nChatbot:"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

# Replace "YOUR_API_KEY" with your actual OpenAI API key
api_key = "YOUR_API_KEY"
chatbot = GeneralChatbot(api_key)

# Conversation loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)
