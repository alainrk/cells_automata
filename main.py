from parameters import *
from Cell import Cell
from Grid import Grid
from random import randint

global cells
global grid
global disturbX
global disturbY

def draw():
  global cells
  global grid
  global disturb

  # Create new grid for this turn
  newGrid = Grid(WIDTH, HEIGHT, GRID_ROWS, GRID_COLS)

  # Update with disturb
  if (disturb is not None):
    amount = MAX_DENSITY_IN_CELL*10000
    # print("Disturbing", disturb["x"], disturb["y"], amount)
    newGrid.incrementDensityInPoint(disturb["x"], disturb["y"], amount)
    disturb["ttl"] -= 1
    if disturb["ttl"] <= 0:
      disturb = None

  # Keep only alive cells
  cells = set(filter(lambda cell: cell.isAlive(), cells))
  newCells = set()

  for cell in cells:
    # Update new grid density
    newGrid.incrementDensityInPoint(cell.x, cell.y)
    # Let live the cells
    newCell = cell.liveAndReplicate(grid.getDensityInPoint(cell.x, cell.y))
    if newCell is not None:
      newCells.add(newCell)

  cells = cells.union(newCells)
  # Apply new grid
  grid = newGrid

  render()

def render():
  global disturb
  fill(0x11000000)
  rect(0, 0, width, height)
  fill(0)
  # print(grid.grid)
  for c in cells:
    c.render()
  if disturb is not None:
    fill(255, 255, 255, 100)
    ellipse(disturb["x"], disturb["y"], WIDTH/5, HEIGHT/5)

def setup():
  global cells
  global grid
  global disturb

  disturb = None
  grid = Grid(WIDTH, HEIGHT, GRID_ROWS, GRID_COLS)
  cells = set()
  for _ in range(START_CELL_COUNT):
    cells.add(Cell(randint(30, 250), randint(30, 250), randint(30, 250), randint(MARGINS, WIDTH-MARGINS), randint(MARGINS, HEIGHT-MARGINS), randint(START_MIN_AGING, START_MAX_AGING)))

  # Graphics
  size(WIDTH, HEIGHT)
  noStroke()

def mouseClicked():
  global disturb
  disturb = { "x": mouseX, "y": mouseY, "ttl": 15 }
  print("Mouse clicked", mouseX, mouseY)
