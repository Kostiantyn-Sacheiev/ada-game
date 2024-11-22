import turtle

from utils.utils import get_integer_input
from Classes.TurtleArtist import TurtleArtist


class TurtleController:
    def __init__(self):
        self.artist = TurtleArtist(name="Leonardo")

    def start_turtle(self):
        commands = {
            1: ("Move forward 100px", self.artist.move_forward),
            2: ("Move up 100px", self.artist.move_up),
            3: ("Move down 100px", self.artist.move_down),
            4: ("Move left 100px", self.artist.move_left),
            5: ("Move right 100px", self.artist.move_right),
            6: ("Draw 'ADA'", self.artist.draw_ada),
            7: ("Draw a square", self.artist.draw_square),
            8: ("Exit Turtle Mode", lambda: print("Exiting Turtle Mode..."))
        }

        while True:
            print("\nTurtle Drawing Options:")
            for key in sorted(commands.keys()):
                description, _ = commands[key]
                print(f"{key}: {description}")
            action = get_integer_input("Choose an option: ")
            if action in commands:
                description, func = commands[action]
                func()
                if description == "Exit Turtle Mode":
                    break
            else:
                print("Invalid choice. Please try again.")
        turtle.done()
