import random


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
