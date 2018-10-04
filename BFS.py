from pathGenerator import *
class BFS:
    x_cord = [0, 1, 0, -1]
    y_cord = [1, 0, -1, 0]
    def __init__(self,matrix, startX, startY,goalX,goalY,grid,n,size):
        self.grid = grid
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.matrix = matrix
        self.size = n
        self.grid_size = size

    def bfs(self,visited,x,y,p):
        queue = []
        queue.append([x,y])
        visited[x][y] = 1
        while queue:
            d = queue.pop(0)
            for i in range(0,4):
                x_temp = BFS.x_cord[i] + d[0]
                y_temp = BFS.y_cord[i] + d[1]
                if x_temp == self.goal_x and y_temp == self.goal_y:
                    return True
                if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size
                        and visited[x_temp][y_temp] == 0 and self.matrix[x_temp][y_temp]==1):
                        p.mark_path(x_temp,y_temp)
                        visited[x_temp][y_temp]=1
                        queue.append([x_temp,y_temp])
        return False

    def bfsUtil(self):
        visited = [[0 for x in range(self.size)] for y in range(self.size)]
        p = PathGenerator(self.grid,self.grid_size)
        self.bfs(visited,self.x,self.y,p)

    def solve(self):
        self.bfsUtil()