from graphics import *
class PathGenerator:
    def __init__(self,grid,size):
        self.grid = grid
        self.size = size

    def generate_path(self):
        print("Gautam")

    def mark_path(self,i,j):
        rect = Rectangle(Point(j*self.size, i*self.size), Point((j+1)*self.size, (i+1)*self.size))
        rect.setFill("orange")
        rect.draw(self.grid)
        print("done")
