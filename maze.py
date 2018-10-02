import random
from graphics import *
n = 10 #Assign the size of the grid
size = 20 #Assign the size of each block in the grid
win = GraphWin('Maze Runner', size*n,size*n) 
for i in range(0,size*n,size):
    for j in range(0,size*n,size):
        rect = Rectangle(Point(i,j ), Point(i+size,j+size)) 
        rect.setWidth(3)
        prob=random.random() 
        if prob>0.8: #Keeps the block empty if probability is lesser than 0.8
            rect.setFill("Black")
        else:
            rect.setFill("White")
        if (i==0 and j==0):
            rect.setFill("Red")
            label1=Text(Point(size/2,size/2),"S")
            
        if (i==(size*n)-size and j==(size*n)-size):
            rect.setFill("Red")
            label2=Text(Point((size*n)-size/2,(size*n)-size/2),"G")
            
        rect.draw(win)
label1.draw(win)
label2.draw(win)        
win.getMouse()
win.close()