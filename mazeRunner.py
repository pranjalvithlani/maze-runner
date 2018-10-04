import random
from DFS import *
from BFS import *
from AStar import *
from GridGenerator import *
from graphics import *

windowsize=600
n=10
rem=windowsize%n
if rem!=0:
    windowsize-=rem
size=windowsize//n
startX = 0
startY = 0


Matrix = [[0 for x in range(n)] for y in range(n)]
p = 0.8
# rect = Rectangle(Point(100, 50), Point(150, 100))
# rect.setFill("orange")
# rect.draw(grid)

for i in range(0, n, 1):
    for j in  range(0,n,1):
        prob = random.random()
        if prob < p:
            Matrix[i][j] = 1

gridObj = GridGenerator(Matrix)
grid = gridObj.generate_grid(n,size, windowsize)
print(Matrix)
#DFS(Matrix, startX, startY ,n-1,n-1,grid,n,size).solve()

BFS(Matrix,startX,startY,n-1,n-1,grid,n,size).solve()
grid.getMouse()
grid.close()
#AStar(Matrix,startX,startY,n-1,n-1,grid,n,size).solve()





