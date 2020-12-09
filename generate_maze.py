import pyglet
from pyglet import shapes

class GenMaze():
    def __init__(self):
        pass
    def create_array(self):
        self.maze = []
        for i in range(self.y):
            self.maze.append([])
            for j in range(self.x):
                self.maze[i].append(0)

    def size(self, x_width, y_width):
        self.x, self.y = x_width * 2, y_width * 2
    def render(self):
        window_width = int((self.x / 2) * 20)
        window_height = int((self.y / 2) * 20)
        self.window = pyglet.window.Window(window_width, window_height, "Maze Solver")
        self.batch = pyglet.graphics.Batch()
        color = (50, 225, 30)
        pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    ('v2i', (10, 15, 30, 35))
)
        pyglet.app.run()
        #self.window.clear()
        #self.batch.draw()

if __name__ == "__main__":
    GM = GenMaze()
    GM.size(30, 20)
    GM.create_array()
    GM.render()