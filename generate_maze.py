import pyglet
from pyglet import shapes
from pyglet import window
import random
import numpy
class GenMaze():
    
    def __init__(self):
        self.start_pos = [0,0]
        
    def get_field(self, x ,y):
        pass
    def create_list(self, x, y, val=0):
        z_list = []
        for i in range(y):
            z_list.append([])
            for j in range(x):
                z_list[i].append(val)
        return z_list
    def is_Valide(self):
        for i in range(self.y):
            for j in range(self.x):
                self.get_field_info(j, i)
    def size(self, x_width, y_width):
        self.x, self.y = x_width, y_width
        self.horizontal_walls = self.create_list(self.x, self.y -1)
        self.vertical_walls = self.create_list(self.x -1, self.y)
        self.field_scores = self.create_list(self.x, self.y)

        
        self.generate(self.horizontal_walls)
        self.horizontal_walls = numpy.asarray(self.horizontal_walls)
        horizontal_list_ones = numpy.ones((1,self.x))
        self.horizontal_walls = numpy.append(self.horizontal_walls,horizontal_list_ones,axis=0)
        self.horizontal_walls = numpy.insert( self.horizontal_walls, 0,horizontal_list_ones,axis=0)
        

        self.generate(self.vertical_walls)
        self.vertical_walls = numpy.asarray(self.vertical_walls)
        vertical_list_ones = numpy.ones((self.y,1))
        self.vertical_walls = numpy.append( self.vertical_walls,vertical_list_ones,axis=1)
        self.vertical_walls = numpy.insert( self.vertical_walls, 0,1,axis=1)
        print(self.horizontal_walls)
        
        #self.is_Valide()
    def get_field_info(self, x, y):
        upper_wall = 1
        lower_wall = 1
        right_wall = 1
        left_wall = 1
        field = self.field_scores[y][x]
        
        
        print(field,{"upper": upper_wall, "lower": lower_wall, "left": left_wall, "right": right_wall})
    def generate(self, walls):
        field = 0
        for i in range(len(walls)):
            for j in range(len(walls[0])):
                rand = random.randint(0, 1)
                if rand:
                    field = 0
                else:
                    field = 1
                walls[i][j] = field
    def render(self, field_size=20):
        batch = pyglet.graphics.Batch() 
        self.window_width = int((self.x) * field_size)
        
        self.window_height = int((self.y) * field_size)
        window = pyglet.window.Window(self.window_width, self.window_height, "Maze Solver")
        color = (0, 0, 0)
        border_color = (255, 255, 255)
        border = shapes.BorderedRectangle(0, 0, self.window_width, self.window_height, border=5,color = color, batch = batch, border_color=border_color)
        lines = []
        for i in range(len(self.horizontal_walls)):
            for j in range(len(self.horizontal_walls[0])):
                if self.horizontal_walls[i][j] == 1:
                    lines.append(shapes.Line(field_size * j,i * field_size ,field_size *j + field_size,i * field_size, 1, batch=batch))
        for i in range(len(self.vertical_walls)):
            for j in range(len(self.vertical_walls[0])):
                if self.vertical_walls[i][j] == 1:
                    lines.append(shapes.Line(j * field_size ,field_size * i,j * field_size, field_size *i + field_size, 1, batch=batch))
        @window.event
        def on_draw():
            window.clear() 
            batch.draw()
        pyglet.app.run()


    

if __name__ == "__main__":
    GM = GenMaze()
    GM.size(10, 10)
    GM.render(field_size=100)