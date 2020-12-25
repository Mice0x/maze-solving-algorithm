import pyglet
from pyglet import shapes
from pyglet import window
import random
import numpy
class GenMaze():
    
    def __init__(self):
        self.start_pos = [0,0]
        self.current_dir = "up"
        
    def get_field(self, x ,y):
        pass
    def create_list(self, x, y, val=0):
        z_list = []
        for i in range(y):
            z_list.append([])
            for j in range(x): 
                z_list[i].append(val)
        return z_list

    def move(self):
        if self.current_dir == "down":
            self.v_y -=1
        elif self.current_dir == "up":
            self.v_y +=1
        elif self.current_dir == "left":
            self.v_x -=1
        else:
            self.v_x +=1
    def turn_right(self):
        i = self.turn.index(self.current_dir)
        if i <3: 
            self.current_dir = self.turn[i+1]
        if i==3:
            self.current_dir = self.turn[0]
    def turn_left(self):
        i = self.turn.index(self.current_dir)
        if i == 0: 
            self.current_dir = self.turn[3]
        if i > 0:
            self.current_dir = self.turn[i-1]
    def is_Valide(self):
        self.v_x, self.v_y = 0,0
        self.turn = ["right", "down", "left", "up"]
        self.field_moves = []
        reward = 0
        for i in range(self.x * self.y):
            while True:
                f_info = self.get_field_info(self.v_x,self.v_y)
                if not f_info[1]["right"][0] and not f_info[1]["right"][1] < f_info[1]["upper"][1]:
                    self.turn_right()
                    self.move()
                elif not f_info[1]["upper"][0] and not f_info[1]["upper"][1] < f_info[1]["left"][1]:
                    self.move()
                elif not f_info[1]["left"][0]:
                    self.turn_left()
                    self.move()
                if [self.v_x, self.v_y] in self.field_moves:
                    reward = -(len(self.field_moves))
                    self.v_x, self.v_y = 0,0
                    break
                else:
                    self.field_moves.append([self.v_x, self.v_y])
            for j,val in enumerate(self.field_moves):
                self.field_scores[val[1]][val[0]] += reward
            self.field_moves = []
        
        for i, row in enumerate(self.field_scores):
            if 0 in row:
                self.field_scores = self.create_list(self.x, self.y)
                return False
        self.field_scores = self.create_list(self.x, self.y)
        return True
    def create_field(self):
        self.horizontal_walls = self.create_list(self.x, self.y -1)
        self.vertical_walls = self.create_list(self.x -1, self.y)
        self.field_scores = self.create_list(self.x, self.y)

        
        self.horizontal_walls = numpy.asarray(self.horizontal_walls)
        horizontal_list_ones = numpy.ones((1,self.x))
        self.horizontal_walls = numpy.append(self.horizontal_walls,horizontal_list_ones,axis=0)
        self.horizontal_walls = numpy.insert( self.horizontal_walls, 0,horizontal_list_ones,axis=0)
        self.horizontal_walls = self.horizontal_walls.tolist()
        

        
        self.vertical_walls = numpy.asarray(self.vertical_walls)
        vertical_list_ones = numpy.ones((self.y,1))
        self.vertical_walls = numpy.append( self.vertical_walls,vertical_list_ones,axis=1)
        self.vertical_walls = numpy.insert( self.vertical_walls, 0,1,axis=1)
        self.vertical_walls = self.vertical_walls.tolist()


        self.generate(self.vertical_walls, 'ver')
        self.generate(self.horizontal_walls, 'hor')

    def size(self, x_width, y_width):
        self.x, self.y = x_width, y_width
        self.create_field()
    def get_field_info(self, x, y):
        upper_score = float('-inf')
        lower_score = float('-inf')
        left_score = float('-inf')
        right_score = float('-inf')

        upper_wall = self.horizontal_walls[y + 1][x]
        lower_wall = self.horizontal_walls[y][x]
        right_wall = self.vertical_walls[y][x + 1]
        left_wall = self.vertical_walls[y][x]
        if not upper_wall:
            upper_score = self.field_scores[y + 1][x]
        if not lower_wall:
            lower_score = self.field_scores[y - 1][x]
        if not left_wall:
            left_score = self.field_scores[y][x - 1]
        if not right_wall:
            right_score = self.field_scores[y][x + 1]

        field = self.field_scores[y][x]
        if self.current_dir == "right":
            return field,{"upper": (right_wall,right_score), "lower": (left_wall,left_score), "left":(upper_wall,upper_score), "right": (lower_wall,lower_score)}
        if self.current_dir == "left":
            return field,{"upper":  (left_wall,left_score), "lower": (right_wall,right_score), "left": (lower_wall,lower_score), "right": (upper_wall,upper_score)}
        if self.current_dir == "up":
            return field,{"upper": (upper_wall,upper_score), "lower": (lower_wall,lower_score), "left": (left_wall,left_score), "right": (right_wall,right_score)}
        if self.current_dir == "down":
            return field,{"upper": (lower_wall,lower_score), "lower": (upper_wall,upper_score), "left": (right_wall,right_score), "right": (left_wall,left_score)}
    def generate(self, walls, wall_dir):
        
        field = 0
        i_iter = len(walls)
        j_iter = len(walls[0])
        if wall_dir == 'hor':
            i_iter -=2
        if wall_dir =='ver':
            j_iter -=2
        for i in range(i_iter):
            if wall_dir == 'hor':
                i +=1
            for j in range(j_iter):
                if wall_dir == 'ver':
                    j += 1
                rand = random.randint(0, 5)
                if rand:
                    field = 1
                else:
                    field = 0
                walls[i][j] = field
                if field:
                    valide = self.is_Valide()
                    if not valide:
                        walls[i][j] = 0

    def render(self, field_size=20):
        startpos = int(field_size/2)
        
        batch = pyglet.graphics.Batch() 
        self.window_width = int((self.x) * field_size)
        
        self.window_height = int((self.y) * field_size)
        window = pyglet.window.Window(self.window_width, self.window_height, "Maze Solver")
        
        color = (0, 0, 0)
        border_color = (255, 255, 255)
        border = shapes.BorderedRectangle(0, 0, self.window_width, self.window_height, border=5,color = color, batch = batch, border_color=border_color)
        start_circle = shapes.Circle(startpos, startpos, int(field_size/2), color =(50, 225, 30), batch = batch) 
        lines = []

        for i in range(len(self.horizontal_walls)):
            for j in range(len(self.horizontal_walls[0])):
                if self.horizontal_walls[i][j] == 1:
                    lines.append(shapes.Line(field_size * j,i * field_size ,field_size *j + field_size,i * field_size, 2, batch=batch))
        for i in range(len(self.vertical_walls)):
            for j in range(len(self.vertical_walls[0])):
                if self.vertical_walls[i][j] == 1:
                    lines.append(shapes.Line(j * field_size ,field_size * i,j * field_size, field_size *i + field_size, 2, batch=batch))
        @window.event
        def on_draw():
            window.clear() 
            batch.draw()
        pyglet.app.run()


    

if __name__ == "__main__":
    GM = GenMaze()
    GM.size(20, 20)
    GM.render(field_size=40)