def get_integer_input(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter an integer")

def get_float_input (message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter an float")