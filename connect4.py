from math import *
from kandinsky import *
from ion import *
from time import *

board=[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]
]

def draw():
  for i in range(7):
    for j in range(7):
      if board[j][i]==0:
        fill_tile(i,j,(0,0,0))
      if board[j][i]==1:
        fill_tile(i,j,(255,0,0))
      if board[j][i]==-1:
        fill_tile(i,j,(255,255,0))

def fill_tile(i,j,c):
  fill_rect(i*24+75,j*24+40,20,20,(0,0,0))
  fill_rect(i*24+75+8,j*24+40,4,20,c)
  fill_rect(i*24+75,j*24+40+8,20,4,c)
  fill_rect(i*24+75+4,j*24+40+2,12,16,c)
  fill_rect(i*24+75+2,j*24+40+4,16,12,c)

def erasecurseur():
  fill_rect(curseur*24+75,0,20,40,(255,255,255))

def drawcurseur():
  if player == 1:
    fill_rect(curseur*24+75,0,20,40,(255,0,0))
  else:
    fill_rect(curseur*24+75,0,20,40,(255,255,0))

def change_player():
  global player
  player *= -1

def place_tile():
  global board
  for y in range(7):
    if board[6-y][curseur] == 0:
      board[6-y][curseur] = player
      return (curseur,6-y)
  return None

def wait_key_up(key_code):
  while keydown(key_code):
    pass

def get_tile(x,y):
  if not 0 <= x < 7 or not 0 <= y < 7:
    return 0
  return board[y][x]

def check_win(tile):
  #horizontal
  aligned = 1
  x,y = tile
  if get_tile(x-1,y) == player:
    aligned += 1
    if get_tile(x-2,y) == player:
      aligned += 1
      if get_tile(x-3,y) == player:
        return True
  if get_tile(x+1,y) == player:
    aligned += 1
    if get_tile(x+2,y) == player:
      aligned += 1
      if get_tile(x+3,y) == player:
        return True
  if aligned >= 4:
    return True
  
  #vertical
  aligned = 1
  if get_tile(x,y+1) == player:
    aligned += 1
    if get_tile(x,y+2) == player:
      aligned += 1
      if get_tile(x,y+3) == player:
        return True
  
  #diagonals
  aligned = 1
  if get_tile(x-1,y-1) == player:
    aligned += 1
    if get_tile(x-2,y-2) == player:
      aligned += 1
      if get_tile(x-3,y-3) == player:
        return True
  if get_tile(x+1,y+1) == player:
    aligned += 1
    if get_tile(x+2,y+2) == player:
      aligned += 1
      if get_tile(x+3,y+3) == player:
        return True
  if aligned >= 4:
    return True
  
  aligned = 1
  if get_tile(x-1,y+1) == player:
    aligned += 1
    if get_tile(x-2,y+2) == player:
      aligned += 1
      if get_tile(x-3,y+3) == player:
        return True
  if get_tile(x+1,y-1) == player:
    aligned += 1
    if get_tile(x+2,y-2) == player:
      aligned += 1
      if get_tile(x+3,y-3) == player:
        return True
  if aligned >= 4:
    return True

def display_win():
  if player == 1:
    draw_string("red wins",120,100,(0,0,0),(255,0,0))
  else:
    draw_string("yellow wins",110,100,(0,0,0),(255,255,0))

def display_tie():
    draw_string("no one wins",110,100)

player = 1
curseur=0
draw()
drawcurseur()
tiles_placed = 0
place = False

wait_key_up(KEY_OK)
while True:
  
  if keydown(KEY_OK):
    wait_key_up(KEY_OK)
    place = True
  if keydown(KEY_EXE):
    wait_key_up(KEY_EXE)
    place = True
  
  if place:
    place = False
    placed_tile = place_tile()
    if placed_tile != None:
      draw()
      tiles_placed += 1
      if check_win(placed_tile):
        display_win()
        break
      if tiles_placed == 49:
        display_tie()
        break
      change_player()
      drawcurseur()
  
  if keydown(KEY_RIGHT):
    erasecurseur()
    curseur=(curseur+1)%7
    drawcurseur()
    wait_key_up(KEY_RIGHT)
  if keydown(KEY_LEFT):
    erasecurseur()
    curseur=(curseur-1)%7
    drawcurseur()
    wait_key_up(KEY_LEFT)
