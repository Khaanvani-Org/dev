import random
import unittest

def generate_random_numbers(size):
    return [random.randint(1, 100) for _ in range(size)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def classify_numbers(numbers, average):
    return ["above average" if num > average else "below average" for num in numbers]

class TestRandomCode(unittest.TestCase):
    def test_generate_random_numbers(self):
        result = generate_random_numbers(5)
        self.assertEqual(len(result), 5)

    def test_calculate_average(self):
        average = calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(average, 3)

    def test_classify_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        average = calculate_average(numbers)
        classification = classify_numbers(numbers, average)
        self.assertEqual(classification, ["below average", "below average", "average", "above average", "above average"])

if __name__ == "__main__":
    # Let's run the tests
    unittest.main()
