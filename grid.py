from spot import Spot
from box import Box
from wall import Wall
import random


class Grid:
    def __init__(self, rows, cols, screen_width, screen_height) -> None:
        self.rows = rows
        self.cols = cols
        self.screen_width = screen_width
        self.screen_height = screen_height
      
    
    def create_grid(self):
        self.grid = [[0 for x in range(self.cols)] in range(self.rows)]
        for row in self.rows:
            for col in self.cols:
                if row % 2 == 0 and col % 2 == 0 or row == 0 or row == self.rows - 1 or col == 0 or col == self.cols -1:
                    self.grid[row][col] = Wall(row, col, self.screen_width / self.cols, self.screen_height / self.rows)
                else:
                    n = random.random()
                    