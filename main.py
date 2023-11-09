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

def calculate_square(number):
    result = number * number
    thread_name = threading.current_thread().name
    print(f"Square of {number} is {result} (Thread: {thread_name})")
    time.sleep(2)

def main():
    numbers = [1, 2, 3, 4, 5]

    threads = []

    for number in numbers:
        thread = threading.Thread(target=calculate_square, args=(number,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads have finished.")
