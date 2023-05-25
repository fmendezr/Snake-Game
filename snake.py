from turtle import Turtle

class Segment:
    def __init__(self, initial_position) -> None:
        self.position = initial_position
        self.turtle = Turtle(shape="square")
        self.turtle.color("FloralWhite")
        self.turtle.penup()
        self.turtle.goto(initial_position)

    # position    

    def get_position(self):
        return self.position
    
    # movement 

    def change_position(self, new_position):
        self.turtle.goto(new_position)
        self.position = new_position

class HeadSegment(Segment):
    def __init__(self, initial_position):
        super().__init__(initial_position)

    # proximity

    def get_distance(self, other_obj_or_coordinates):
        return self.turtle.distance(other_obj_or_coordinates)
    
    # collission 

    def collision_with_wall(self):
        if self.position[0] > 290 or self.position[0] < -290 or self.position[1] > 290 or self.position[1] < -290 :
            return True
        return False
    
    # movement
        
    def move_forward(self):
        self.turtle.forward(20)
        self.position =self.turtle.pos()

    def turn_left(self):
        self.turtle.left(90)
    
    def turn_right(self):
        self.turtle.right(90)

class Snake:
    def __init__(self) -> None:
        self.head = HeadSegment((0,0))
        self.segments = [self.head, Segment((-20,0)), Segment((-40,0))]
        self.previous_tail_position = (-40,0)

    # eat food 
    def eat_food(self):
        self.segments.append(Segment(self.previos_tail_position))

    # detect collissions
    def detect_collission_with_food(self, food):
        if self.head.get_distance(food) <= 15:
            self.eat_food()
            return True
        return False

    def detect_collission_with_self(self):
        for x in range(1, len(self.segments)):
            if self.head.get_distance(self.segments[x].get_position()) <= 10:
                return True
        return False
    
    def detect_collission_with_wall(self):
        return self.head.collision_with_wall()

    # movement
    def move_forward(self):
        self.previos_tail_position = self.segments[-1].get_position() 
        for segment_number in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_number].change_position(self.segments[segment_number - 1].get_position())
        self.segments[0].move_forward()
    
    def turn_left(self):
        self.segments[0].turn_left()
    
    def turn_right(self):
        self.segments[0].turn_right()
