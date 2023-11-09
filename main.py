import random
import statistics

def generate_random_numbers(num_elements):
    return [random.randint(1, 100) for _ in range(num_elements)]

def calculate_stats(numbers):
    try:
        sorted_numbers = sorted(numbers)
        mean = statistics.mean(sorted_numbers)
        std_dev = statistics.stdev(sorted_numbers)
        return mean, std_dev
    except statistics.StatisticsError as e:
        print(f"Error calculating statistics: {e}")
        return None, None

def main():
    num_elements = 10
    random_numbers = generate_random_numbers(num_elements)

    print(f"Generated Random Numbers: {random_numbers}")

    mean, std_dev = calculate_stats(random_numbers)

    if mean is not None and std_dev is not None:
        print(f"Mean: {mean}")
        print(f"Standard Deviation: {std_dev}")

if __name__ == "__main__":
    main()
