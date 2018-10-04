import random
from graphics import *
class GridGenerator:
    def __init__(self,matrix):
        self.matrix =  matrix

    def generate_grid(self,n , size, windowsize):
        
        win = GraphWin('Maze Runner', windowsize, windowsize)
        matrix = self.matrix
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                rect = Rectangle(Point(j*size, i*size), Point((j+1)*size, (i+1)*size))
                rect.setWidth(0)
                print(i,j)
                if matrix[i][j] ==0:  # Keeps the block empty if probability is lesser than 0.8
                    rect.setFill("Black")
                else:
                    rect.setFill("White")
                if (i == 0 and j == 0):
                    rect.setFill("Red")
                    #label1 = Text(Point(size / 2, size / 2), "S")

                if (i == n-1 and j == n-1):
                    rect.setFill("Red")
                    #label2 = Text(Point((size * n) - size / 2, (size * n) - size / 2), "G")

                rect.draw(win)
        #label1.draw(win)
        #label2.draw(win)
        # rect = Rectangle(Point(100, 50), Point(150, 100))
        # rect.setFill("orange")
        # rect.draw(win)
        return win
