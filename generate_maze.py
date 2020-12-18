import pyglet
from pyglet import shapes
from pyglet import window
import random

class GenMaze():
    
    def __init__(self):
        pass
    def create_array(self):
        self.maze = []
        for i in range(self.y):
            self.maze.append([])
            for j in range(self.x):
                self.maze[i].append(0)
    def is_Valide(self):
        for i in range(self.y):
            for j in range(self.x):
                print(2)
    def size(self, x_width, y_width):
        self.x, self.y = x_width * 2, y_width * 2
        self.create_array()
        self.generate()
    def generate(self):
        field = '0'
        for i in range(self.y):
            for j in range(self.x):
                rand = random.randint(0, 1)
                if rand:
                    field = '#'
                else:
                    field = '0'
                self.maze[i][j] = field
        self.is_Valide()
    def render(self, field_size=20):
        batch = pyglet.graphics.Batch() 
        self.window_width = int((self.x / 2) * field_size)
        self.window_height = int((self.y / 2) * field_size)
        window = pyglet.window.Window(self.window_width, self.window_height, "Maze Solver")
        color = (0, 0, 0)
        border_color = (255, 255, 255)
        border = shapes.BorderedRectangle(0, 0, self.window_width, self.window_height, border=5,color = color, batch = batch, border_color=border_color)
        lines = []
        for i in range(self.y):
            for j in range(self.x):
                if (i + 1) % 2 and (j + 1) % 2:
                    if self.maze[i][j] == '#':
                        lines.append(shapes.Line(j * field_size, i * field_size, j * field_size + field_size, i * field_size, 2.5, batch=batch))
                elif not((j + 1) % 2 and (i + 1) % 2):
                    if self.maze[i][j] == '#':
                        lines.append(shapes.Line(j * field_size, i * field_size, j * field_size, i * field_size + field_size, 2.5, batch=batch))
        @window.event
        def on_draw():
            window.clear() 
            batch.draw()
        pyglet.app.run()


    

if __name__ == "__main__":
    GM = GenMaze()
    GM.size(10, 10)
    GM.render(field_size=50)