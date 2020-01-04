from random import randint
from math import floor
from Cell import Cell

class Grid:

  def __init__(self, width, height, rows, cols):
    self.width, self.height = width, height
    self.rows, self.cols = rows, cols
    # Optimize here
    self.cellWidth = self.width / self.rows
    self.cellHeight = self.height / self.cols

    self.resetGrid()

  def resetGrid(self):
    self.grid = {}
    for row in range(self.rows):
      for col in range(self.cols):
        self.grid[(row, col)] = 0

  def getDensityInPoint(self, x, y):
    return self.grid[(floor(x / self.cellWidth), floor(y / self.cellHeight))]

  def getCellGridCoordinates(self, x, y):
    return (floor(x / self.cellWidth), floor(y / self.cellHeight))

  def incrementDensityInPoint(self, x, y, amount = 1):
    self.grid[(floor(x / self.cellWidth), floor(y / self.cellHeight))] += amount

  # def computeDensity(self, cells):
  #   for cell in cells:
  #     coords = self.getCellGridCoordinates(cell.x, cell.y)
  #     self.grid[coords] += 1

# # TEST
# from parameters import *
# grid = Grid(WIDTH, HEIGHT, 5, 4)
# cells = set()
# for _ in range(1500000):
#   x, y = randint(MARGINS, WIDTH-MARGINS), randint(MARGINS, HEIGHT-MARGINS)
#   cells.add(Cell(randint(30, 250), randint(30, 250), randint(30, 250), x, y))
#   grid.incrementDensityInPoint(x, y)
# print(grid.getDensityInPoint(300, 250))