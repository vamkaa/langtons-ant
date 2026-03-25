class Simulator:
    def __init__(self, rule_string):
        self.rule_string = rule_string
        self.state_count = len(rule_string)
        
        
        
        
        self.ant_x = 0
        self.ant_y = 0
        self.direction = 0
        self.step_count= 0
        self.grid = {}

    def get_cell_state(self, x, y):
        return self.grid.get((x, y), 0)

    def set_cell_state(self, x, y, state):
        if state == 0:
            self.grid.pop((x, y), None)
        else:
            self.grid[(x, y)] = state

    def turn_right(self):
        self.direction = (self.direction + 1) % 4
    
    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def move_forward(self):
        if self.direction == 0:
            self.ant_y -= 1
        elif self.direction == 1:
            self.ant_x += 1
        elif self.direction == 2:
            self.ant_y += 1
        elif self.direction == 3:
            self.ant_x -= 1


    def step(self):
        current_state = self.get_cell_state(self.ant_x, self.ant_y)
        turn_instruction = self.rule_string[current_state]

        if turn_instruction == "R":
            self.turn_right()
        elif turn_instruction == "L":
            self.turn_left()

        next_state = (current_state + 1) % self.state_count
        self.set_cell_state(self.ant_x, self.ant_y, next_state)

        
        self.move_forward()
        self.step_count += 1