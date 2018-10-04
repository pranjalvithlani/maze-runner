from pathGenerator import *
class DFS:
    x_cord = [0,1,0,-1]
    y_cord = [1,0,-1,0]
    def __init__(self,matrix, startX, startY,goalX,goalY,grid,n,size):
        self.grid = grid
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.matrix = matrix
        self.size = n
        self.grid_size = size

    def dfs(self,visited,x,y,p):
        visited[x][y]=1
        if x==self.goal_x and y==self.goal_y:
            return True
        p.mark_path(x, y)
        for i in range(0,4):
            x_temp = DFS.x_cord[i] + x
            y_temp = DFS.y_cord[i] + y
            if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size
                and visited[x_temp][y_temp] == 0 and self.matrix[x_temp][y_temp]==1):

                if self.dfs(visited,x_temp,y_temp,p):
                    return True
        return False

    def dfsUtil(self):
        visited = [[0 for x in range(self.size)] for y in range(self.size)]
        p = PathGenerator(self.grid,self.grid_size)
        self.dfs(visited,self.x,self.y,p)

    def solve(self):
        self.dfsUtil()



