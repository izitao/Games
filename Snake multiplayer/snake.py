from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''Represents the sanke in the game'''

    def __init__(self, snake_color, starting_positions):
        self.snake_parts = []
        self.snake_color = snake_color
        self.starting_positions = starting_positions
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        '''Creates the snake at the start of game'''
        for position in self.starting_positions: #snake always starts with 3 parts
            self.add_part(position)


    def add_part(self, position):
        new_snake_part = Turtle(shape="square")
        new_snake_part.color(self.snake_color)
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.snake_parts.append(new_snake_part)

    def extend(self):
        #add a new part to the snake
        self.add_part(self.snake_parts[-1].position())

    def move(self):
        '''Moves the snake'''
        for part_of_snake in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_of_snake - 1].xcor() #this tells coordinates where should the previous segment go
            new_y = self.snake_parts[part_of_snake - 1].ycor() #this tells coordinates where should the previous segment go
            self.snake_parts[part_of_snake].goto(new_x, new_y) #the last segment goes to the position of the previous segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        '''Changes the snakes direction'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Changes the snakes direction'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        '''Changes the snakes direction'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        '''Changes the snakes direction'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
