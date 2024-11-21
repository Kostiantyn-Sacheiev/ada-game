import random
import webbrowser
import time
import threading

def get_integer_input (message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter an integer")


def print_random_number_between_one_and_six():
    print("Your number is: " + str(random.randint(1, 6)))

def generate_fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        print(a)
        a, b = b, a + b

def play_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 6

    print("Guess the number between 1 and 100. You have 6 attempts.")

    for i in range(attempts):
        guess = int(input(f"Attempt {i + 1}/{attempts}: Your guess: "))
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Game over! The number was: {secret_number}")

def search_in_browser():
    input_message = input("Enter your search query: ")
    webbrowser.open(f"https://www.google.com/search?q={input_message}")

def get_user_input():
    global user_answer
    user_answer = input("Your answer: ").strip()

def handle_question(question, correct_answer, timeout=30) -> str:
    global user_answer
    user_answer = None
    print(f"\nQuestion: {question}")
    print("You have 30 seconds to answer.")
    input_thread = threading.Thread(target=get_user_input)
    input_thread.start()
    input_thread.join(timeout=timeout)
    if user_answer is None:
        print("\nTime's up! You didn't answer in time.")
        return "skipped"
    elif user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return "correct"
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return "incorrect"

def ask_questions():
    questions = {
        "What is the capital of Germany?": "Berlin",
        "What is 5 + 7?": "12",
        "What is the square root of 16?": "4",
        "What is the color of the sky on a clear day?": "blue",
        "What is the largest planet in the solar system?": "Jupiter",
        "What language is used to write Python programs?": "Python",
        "What is the chemical symbol for water?": "H2O",
        "What is 9 * 9?": "81",
        "What is the first letter of the English alphabet?": "A",
        "What is the opposite of hot?": "cold"
    }
    correct = 0
    incorrect = 0
    skipped = []
    for question, correct_answer in questions.items():
        result = handle_question(question, correct_answer)
        if result == "correct":
            correct += 1
        elif result == "incorrect":
            incorrect += 1
        elif result == "skipped":
            skipped.append((question, correct_answer))
    print("\n--- Quiz Results ---")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")
    if skipped:
        print("\nQuestions you didn't answer in time:")
        for question, answer in skipped:
            print(f"{question} (Correct answer: {answer})")

def chatting_with_ada():
    print("Hello! I'm Ada, your virtual girlfriend.")
    name = input("What's your name? ")
    print(f"The name is stupid, but ok, {name}!")

    age = get_integer_input(f"{name}, how old are you? ")
    if age < 18:
        print(f"You're still a baby, {name}")
    elif age < 25:
        print(f"A good age to spend time with friends. Get up from your computer, {name}")
    elif age < 40:
        print(f"Why are you not at the work, {name}?")
    elif age < 60:
        print(f"Don't forget to visit the doctor, {name}")
    else:
        print(f"Can you turn on the computer? It's success, {name}!!!")

    commands = {
        1 : ("Roll", print_random_number_between_one_and_six),
        2 : ("Guess", play_guessing_game),
        3 : ("Fibonacci", lambda: generate_fibonacci(100000)),
        4 : ("Open the Google Page", search_in_browser),
        5 : ("Get 10 questions", ask_questions),
        6 : ("Exit", lambda: print("Goodbye!"))
    }

    while True:
        print(f"\nWhat would you like to do next, {name}?")
        for key, (description) in commands.items():
            print(f"{key}: {description}")
        action = get_integer_input("Write the number for the option: ")
        if action in commands:
            description, func = commands[action]
            func()
            if description == "Exit":
                break
        else:
            print("Invalid choice. Please try again.")

chatting_with_ada()
