from math import ceil
from random import randint
from kandinsky import fill_rect,draw_string
from ion import *
from time import monotonic

colors = {}
for i in range(1,8):
  c = ((((i>>2)&1)<<8)-1,(((i>>1)&1)<<8)-1,((i&1)<<8)-1)
  colors[i] = c if c != (255,255,255) else (255,100,100)

def is_moving_key_down():
  return keydown(KEY_LEFT) or keydown(KEY_RIGHT) or keydown(KEY_UP) or keydown(KEY_DOWN)

def load_map():
  #grid size: 10*17
  a = []
  for y in range(17):
    a.append([])
    for x in range(10):
      a[y].append(0) 
  return a

def display_ui():
  fill_rect(0,0,320,222,(100,100,100))
  fill_rect(150,20,100,170,(0,0,0))
  fill_rect(70,30,70,70,(0,0,0))

def display_title():
  draw_string("T",80-5,10,(0,0,255),(100,100,100))
  draw_string("E",90-5,10,(0,255,0),(100,100,100))
  draw_string("T",100-5,10,(0,255,255),(100,100,100))
  draw_string("R",110-5,10,(255,0,0),(100,100,100))
  draw_string("I",120-5,10,(255,0,255),(100,100,100))
  draw_string("S",130-5,10,(255,255,0),(100,100,100))

def check_lose():
  return grid[0] != [0,0,0,0,0,0,0,0,0,0]

def remove_lines():
  global grid
  for y in range(17):
    if not 0 in grid[y]:
      del grid[y]
      grid.insert(0,[0,0,0,0,0,0,0,0,0,0])

def display_grid():
  global current_piece,old_current_piece
  for x in range(10):
    for y in range(17):
      tile_id = grid[y][x]
      if not tile_id:
        if [x,y] in current_piece:
          fill_rect(150+x*10,20+y*10,10,10,colors[p+1])
        #elif [x,y] in old_current_piece:
        else:
          fill_rect(150+x*10,20+y*10,10,10,(0,0,0))
      else:
        r = (((tile_id>>2)&1)<<8)-1
        g = (((tile_id>>1)&1)<<8)-1
        b = ((tile_id&1)<<8)-1
        c = (r,g,b)
        fill_rect(150+x*10,20+y*10,10,10, c if c != (255,255,255) else (255,100,100))

def move_current_piece(left_key_down,right_key_down,up_key_down,down_key_down):
  global current_piece,current_piece_points,can_move
  
  if not right_key_down and not left_key_down and not up_key_down and not down_key_down:
    return
  
  if down_key_down:
    make_current_piece_fall()
  
  if not can_move:
    return
  
  if left_key_down or right_key_down:
    movable = True
    for piece in current_piece:
      if left_key_down:
        if piece[0] == 0 or grid[piece[1]][piece[0]-1]:
          movable = False
          break
      elif right_key_down:
        if piece[0] == 9 or grid[piece[1]][piece[0]+1]:
          movable = False
          break
    
    if movable:
      can_move = False
      if left_key_down:
        for piece in current_piece:
          piece[0] -= 1
      else:
        for piece in current_piece:
          piece[0] += 1
  
  if up_key_down and not p == 2:
    backup_points = current_piece_points
    for point in current_piece_points:
      point[0],point[1] = -point[1],point[0]
    center_point = current_piece[ceil(len(current_piece)/2)-1]
    if not create_shape(center_point[0],current_piece_points,center_point[1],True):
      current_piece_points = backup_points
    can_move = False

def get_grid_cell(x,y):
  if not 0 <= x <= 9 or not 0 <= y <= 16:
    return 0
  return grid[y][x]

def set_grid_cell(x,y,value):
  global grid
  if not 0 <= x <= 9 or not 0 <= y <= 16:
    return
  grid[y][x] = value

def make_current_piece_fall():
  global current_piece,grid,score
  
  hit = False
  for piece in current_piece:
    if piece[1] != 16:
      if get_grid_cell(piece[0],piece[1]+1) == 0:
        continue
    hit = True
  
  if hit:
    for piece in current_piece:
      set_grid_cell(piece[0],piece[1],p+1)
    current_piece = []
    score += 1
  else:
    for piece in current_piece:
      piece[1] += 1

def game_over():
  draw_string("GAME OVER",115,60)
  draw_string("Score: "+str(score),115,80)

def create_shape(x,point_list,y=0,no_recursion=False,depth=0):
  global current_piece,current_piece_points
  if depth >= 10:
    return False
  current_piece_points = point_list
  for point in point_list:
    if not 0 <= x + point[0] or get_grid_cell(point[0]+x,y):
      x += 1
      if not no_recursion:
        create_shape(x,point_list,depth=depth+1)
      return False
    if not x + point[0] <= 9 or get_grid_cell(x,point[1]+y):
      x -= 1
      if not no_recursion:
        create_shape(x,point_list,depth=depth+1)
      return False
  current_piece = []
  for point in point_list:
    current_piece.append([x+point[0],y+point[1]])
  return True

def display_next_piece(piece):
  fill_rect(70,28,70,74,(0,0,0))
  if piece == 0:
    fill_rect(70+1*14,30+2*14,3*14,1*14,(0,0,255))
    fill_rect(70+2*14,30+3*14,1*14,1*14,(0,0,255))
  elif piece == 1:
    fill_rect(70+2*14,30,1*14,5*14,(0,255,0))
  elif piece == 2:
    fill_rect(70+1*14,30+1*14,3*14,3*14,(0,255,255))
  elif piece == 3:
    fill_rect(70+2*14,30+2*14,2*14,1*14,(255,0,0))
    fill_rect(70+1*14,30+3*14,2*14,1*14,(255,0,0))
  elif piece == 4:
    fill_rect(70+1*14,30+2*14,2*14,1*14,(255,0,255))
    fill_rect(70+2*14,30+3*14,2*14,1*14,(255,0,255))
  elif piece == 5:
    fill_rect(70+1*14,30+1*14-3,1*14,1*14,(255,255,0))
    fill_rect(70+2*14,30+1*14-3,1*14,4*14,(255,255,0))
  elif piece == 6:
    fill_rect(70+3*14,30+1*14-3,1*14,1*14,(255,100,100))
    fill_rect(70+2*14,30+1*14-3,1*14,4*14,(255,100,100))

score = 0
grid = load_map()
display_ui()
display_title()

current_piece = []
old_current_piece = []
current_piece_points = []
new_second = False
can_move = True
t_last_second = monotonic()
t = monotonic()
p,nextp=randint(0,6),randint(0,6)
display_next_piece(nextp)

while True:
  
  t = monotonic()
  new_second = t - t_last_second >= 0.5
  
  if new_second:
    t_last_second = t
  
  if not can_move:
    if not is_moving_key_down():
      can_move = True
  
  if len(current_piece) == 0 and new_second:
    x = randint(0,len(grid[0])-1)
    p = nextp
    nextp = randint(0,6)
    if p == 0: #T
      create_shape(x,[[1,0],[0,0],[-1,0],[0,1]])
    elif p == 1: #long
      create_shape(x,[[0,-2],[0,-1],[0,0],[0,1],[0,2]])
    elif p == 2: #square
      create_shape(x,[[1,0],[0,0],[0,1],[1,1]])
    elif p == 3: #squigly
      create_shape(x,[[1,0],[0,0],[0,1],[-1,1]])
    elif p == 4: #reverse squigly
      create_shape(x,[[-1,0],[0,0],[0,1],[1,1]])
    elif p == 5: #L
      create_shape(x,[[-1,-1],[0,-1],[0,0],[0,1],[0,2]])
    elif p == 6: #reverse L
      create_shape(x,[[1,-1],[0,-1],[0,0],[0,1],[0,2]])
    display_next_piece(nextp)
  
  if len(current_piece) != 0:
    move_current_piece(keydown(KEY_LEFT),keydown(KEY_RIGHT),keydown(KEY_UP),keydown(KEY_DOWN))
    if new_second:
      make_current_piece_fall()
  
  remove_lines()
  
  display_grid()
  
  if check_lose():
    game_over()
    break
