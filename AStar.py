from pathGenerator import *
class AStar:
    def __init__(self,matrix, startX, startY,goalX,goalY,grid,n,size):
        self.grid = grid
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.matrix = matrix
        self.size = n
        self.grid_size = size

    def solve(self):
        path = PathGenerator(map,self.grid,self.current_x,self.current_y)
        path.generate_path()