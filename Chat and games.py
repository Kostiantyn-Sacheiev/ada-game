import random

def get_random_number_between_one_and_six():
    return random.randint(1, 6)

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

def chatting_with_ada():
    print("Hello! I'm Ada, your virtual girlfriend.")
    name = input("What's your name? ")
    print(f"The name is stupid, but ok, {name}!")

    age = int(input(f"{name}, how old are you? "))
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

    while True:
        action = input(f"\nWhat would you like to do next, {name}? \n1.roll; \n2.guess; \n3.fibonacci; \n4.exit.\nWrite please the number for the option: ")
        if action == "1":
            print(f"You rolled a {get_random_number_between_one_and_six()}!")
        elif action == "2":
            play_guessing_game()
        elif action == "3":
            generate_fibonacci(100000)
            print("\n")
        elif action == "4":
            print(f"Goodbye, {name}! See you soon! (Hope no)")
            break

chatting_with_ada()
