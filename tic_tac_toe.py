from math import *
from kandinsky import *
from ion import *
from turtle import *

def display_grid():
  fill_rect(85,86,150,1,(0,0,0))
  fill_rect(85,136,150,1,(0,0,0))
  fill_rect(135,36,1,150,(0,0,0))
  fill_rect(185,36,1,150,(0,0,0))

def display_cursor():
  if player == 1:
    c = (0,255,0)
  else:
    c = (0,0,255)
  fill_rect(85+cursor[0]*50+5,36+cursor[1]*50+5,5,50-10,c)
  fill_rect(85+cursor[0]*50+5,36+cursor[1]*50+5,50-10,5,c)
  fill_rect(85+cursor[0]*50-10+50,36+cursor[1]*50+5,5,50-10,c)
  fill_rect(85+cursor[0]*50+5,36+cursor[1]*50-10+50,50-10,5,c)

def erase_cursor():
  fill_rect(85+cursor[0]*50+5,36+cursor[1]*50+5,5,50-10,(255,255,255))
  fill_rect(85+cursor[0]*50+5,36+cursor[1]*50+5,50-10,5,(255,255,255))
  fill_rect(85+cursor[0]*50-10+50,36+cursor[1]*50+5,5,50-10,(255,255,255))
  fill_rect(85+cursor[0]*50+5,36+cursor[1]*50-10+50,50-10,5,(255,255,255))

def wait_key_up(key_code):
  while keydown(key_code):
    pass

def move_cursor():
  global cursor
  if keydown(KEY_UP):
    erase_cursor()
    cursor[1] = (cursor[1]-1)%3
    display_cursor()
    wait_key_up(KEY_UP)
  elif keydown(KEY_DOWN):
    erase_cursor()
    cursor[1] = (cursor[1]+1)%3
    display_cursor()
    wait_key_up(KEY_DOWN)
  if keydown(KEY_LEFT):
    erase_cursor()
    cursor[0] = (cursor[0]-1)%3
    display_cursor()
    wait_key_up(KEY_LEFT)
  elif keydown(KEY_RIGHT):
    erase_cursor()
    cursor[0] = (cursor[0]+1)%3
    display_cursor()
    wait_key_up(KEY_RIGHT)

def place_symbol():
  global grid
  if player == 1:
    color(0,255,0)
    line_len = sqrt(30**2+30**2)
    goto(85+cursor[0]*50-160+10,-(36+cursor[1]*50-111+10))
    pendown()
    
    setheading(-45)
    forward(line_len)
    
    penup()
    goto(85+cursor[0]*50-160+50-10,-(36+cursor[1]*50-111+10))
    pendown()
    
    setheading(-135)
    forward(line_len)
    
    penup()
    
  else:
    color(0,0,255)
    goto(85+cursor[0]*50-145,-(36+cursor[1]*50-96))
    pendown()
    
    circle(14)
    
    penup()
  
  grid[cursor[1]][cursor[0]] = player

def check_win():
  for x in range(3):
    aligned = True
    for y in range(3):
      if grid[y][x] != player:
        aligned = False
    if aligned:
      return True
  
  for y in range(3):
    if grid[y] == [player,player,player]:
      return True
  
  if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
    return True
  
  if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
    return True

def display_win():
  if player == 1:
    draw_string("green wins",120,100,(0,0,0),(0,255,0))
  else:
    draw_string("blue wins",110,100,(0,0,0),(0,0,255))

def display_tie():
    draw_string("no one wins",110,100)

def change_player():
  global player
  player *= -1

player = 1
cursor = [0,0]
grid = [
[0,0,0],
[0,0,0],
[0,0,0],
]

hideturtle()
pensize(3)
penup()
display_grid()
display_cursor()
symbols_placed = 0

while True:
  
  move_cursor()
  
  if keydown(KEY_OK):
    if grid[cursor[1]][cursor[0]] == 0:
      place_symbol()
      symbols_placed += 1
      if check_win():
        display_win()
        break
      if symbols_placed == 9:
        display_tie()
        break
      change_player()
      display_cursor()
    wait_key_up(KEY_OK)
