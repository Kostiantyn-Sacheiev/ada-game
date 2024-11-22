import turtle

class TurtleArtist:
    def __init__(self, name, color="green", background_color="black"):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        screen = turtle.Screen()
        screen.bgcolor(background_color)
        self.turtle.speed('normal')
        self.name = name

    def move_forward(self, distance=100):
        self.turtle.forward(distance)

    def move_up(self, distance=100):
        self.turtle.setheading(90)  
        self.turtle.forward(distance)

    def move_down(self, distance=100):
        self.turtle.setheading(270) 
        self.turtle.forward(distance)

    def move_left(self, distance=100):
        self.turtle.setheading(180)  
        self.turtle.forward(distance)

    def move_right(self, distance=100):
        self.turtle.setheading(0)  
        self.turtle.forward(distance)

    def draw_ada(self):
        self.turtle.penup()
        self.turtle.goto(-200, 0)
        self.turtle.setheading(0)
        self.turtle.pendown()

        self.turtle.left(75)
        self.turtle.forward(100)
        self.turtle.right(150)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.right(105)
        self.turtle.forward(30)

        self.turtle.penup()
        self.turtle.goto(-80, 0)
        self.turtle.setheading(0)
        self.turtle.pendown()

        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.circle(-50, 180)

        self.turtle.penup()
        self.turtle.goto(80, 0)
        self.turtle.setheading(0)
        self.turtle.pendown()

        self.turtle.left(75)
        self.turtle.forward(100)
        self.turtle.right(150)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.right(105)
        self.turtle.forward(30)

    def draw_square(self, size=100):
        for _ in range(4):
            self.turtle.forward(size)
            self.turtle.right(90)
