

class Chatbot:
    def respond(self, user_input):
        if "hello" in user_input.lower():
            return "Hi there!"
        else:
            return "I don't understand."

# Test cases for the Chatbot class
class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_hello_response(self):
        response = self.chatbot.respond("Hello")
        self.assertEqual(response, "Hi there!")

    def test_hello_response_case_insensitive(self):
        response = self.chatbot.respond("HeLLo")
        self.assertEqual(response, "Hi there!")

    def test_other_input_response(self):
        response = self.chatbot.respond("What's the weather like?")
        self.assertEqual(response, "I don't understand.")

    def test_exit_command(self):
        response = self.chatbot.respond("exit")
        self.assertNotEqual(response, "Chatbot: Goodbye!")  # Check that exit doesn't trigger goodbye

