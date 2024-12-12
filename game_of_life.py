from kandinsky import *
from random import *

def load_grid():
  grid = []
  for x in range(32):
    grid.append([])
    for y in range(22):
      grid[x].append(1 if not randint(0,INITIAL_CELL_PROBABILITY) else 0)
  return grid

def get_grid_cell(x,y):
  if not 0 <= x <= 31 or not 0 <= y <= 21:
    return 0
  return grid[x][y]

def get_surrounding_grid_cell(x,y):
  return get_grid_cell(x+1,y)+get_grid_cell(x-1,y)+get_grid_cell(x+1,y+1)+get_grid_cell(x,y+1)+get_grid_cell(x-1,y+1)+get_grid_cell(x-1,y-1)+get_grid_cell(x,y-1)+get_grid_cell(x+1,y-1)

def update_grid():
  new_grid = []
  for x in range(32):
    new_grid.append([])
    for y in range(22):
      c = get_grid_cell(x,y)
      n = get_surrounding_grid_cell(x,y)
      if c:
        if n == 2 or n == 3:
          new_grid[x].append(1)
        else:
          new_grid[x].append(0)
      else:
        if n == 3:
          new_grid[x].append(1)
        else:
          new_grid[x].append(0)
          
  return new_grid

def display_grid():
  for x in range(32):
    for y in range(22):
      fill_rect(x*10,y*10,10,10,((not get_grid_cell(x,y))*255,)*3)

INITIAL_CELL_PROBABILITY = 3

grid = load_grid()
display_grid()
while True:
  new_grid = update_grid()
  if new_grid == grid:
    break
  grid = new_grid
  display_grid()
