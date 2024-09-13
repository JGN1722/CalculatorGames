from math import *
from random import *
from kandinsky import *
from ion import *
from time import monotonic,sleep

def game_over():
  draw_string("GAME OVER",115,60)
  draw_string("Score: "+str(score),115,80)

def check_lose():
  return not 0 <= py <= 222

def check_collision():
  ipy = int(py)
  if get_pixel(px-10,ipy-10) in pipe_colors:
    return True
  if get_pixel(px+10,ipy-10) in pipe_colors:
    return True
  if get_pixel(px-10,ipy+10) in pipe_colors:
    return True
  if get_pixel(px+10,ipy+10) in pipe_colors:
    return True
  return False

def display_background():
  fill_rect(0,0,320,222,SKY_COLOR)

def erase_player():
  fill_rect(px-10,int(py)-10,25,20,SKY_COLOR)

def display_player():
  ipy = int(py)
  fill_rect(px-10+4,ipy-10,20-8,20,(255,255,0))
  fill_rect(px-10,ipy-10+4,20,20-8,(255,255,0))
  fill_rect(px+10,ipy,5,5,(255, 134, 24))
  fill_rect(px+5,ipy-3,3,3,(0,0,0))

def spawn_pipe():
  global pipes
  
  if not randint(0,PIPE_FREQUENCY):
    pipes.append([320,randint(H_GAP_SIZE+10,222-H_GAP_SIZE-10)])
    return True

def move_n_display_pipes(dt):
  global pipes,score
  
  i = 0
  while i < len(pipes):
    pipe = pipes[i]
    
    if pipe[0] < -10:
      del pipes[i]
      if i != 0:
        i -= 1
      score += 1
      fill_rect(pipe[0]-20,0,40,pipe[1]-H_GAP_SIZE,SKY_COLOR)
      fill_rect(pipe[0]-20,pipe[1]+H_GAP_SIZE,40,222-pipe[1]+30,SKY_COLOR)
      fill_rect(pipe[0]-25,pipe[1]-H_GAP_SIZE-20,50,20,SKY_COLOR)
      fill_rect(pipe[0]-25,pipe[1]+H_GAP_SIZE,50,20,SKY_COLOR)
      continue
    
    fill_rect(pipe[0]-20,0,40,pipe[1]-H_GAP_SIZE,SKY_COLOR)
    fill_rect(pipe[0]-20,pipe[1]+H_GAP_SIZE,40,222-pipe[1]+30,SKY_COLOR)
    fill_rect(pipe[0]-25,pipe[1]-H_GAP_SIZE-20,50,20,SKY_COLOR)
    fill_rect(pipe[0]-25,pipe[1]+H_GAP_SIZE,50,20,SKY_COLOR)
    
    pipe[0] -= int(80*dt)
    
    fill_rect(pipe[0]-20,0,40,pipe[1]-H_GAP_SIZE,pipe_colors[0])
    fill_rect(pipe[0]-20,pipe[1]+H_GAP_SIZE,40,222-pipe[1]+30,pipe_colors[0])
    fill_rect(pipe[0]-25,pipe[1]-H_GAP_SIZE-20,50,20,pipe_colors[1])
    fill_rect(pipe[0]-25,pipe[1]+H_GAP_SIZE,50,20,pipe_colors[1])
    
    i += 1

def move_player(dt):
  global py,up_force
  
  if keydown(KEY_UP):
    up_force = JUMP_STRENGTH
  
  py -= up_force*20*dt
  up_force -= 20*dt
  if up_force < -TERMINAL_VELOCITY:
    up_force = -TERMINAL_VELOCITY

def display_clouds():
  fill_rect(100-20,100+30,100,25,(255,255,255))
  fill_rect(125-20,75+30,50,25,(255,255,255))
  
  fill_rect(100+100,100-50,100,25,(255,255,255))
  fill_rect(125+100,75-50,50,25,(255,255,255))

SKY_COLOR = (100,100,255)
JUMP_STRENGTH = 5
TERMINAL_VELOCITY = JUMP_STRENGTH<<1
GAP_SIZE = 80
H_GAP_SIZE = GAP_SIZE>>1
PIPE_FREQUENCY = 100
PIPE_COOLDOWN = 2

t1 = monotonic()

score = 0
px = 30
py = 100
up_force = JUMP_STRENGTH

pipe_colors = (
  (0,255,0),
  (206,255,206),
)
pipe_spawn_cooldown = 0
pipes = []

display_background()
while True:
  t2 = monotonic()
  dt = t2 - t1
  t1 = t2
  
  erase_player()
  move_player(dt)
  display_player()
  
  if pipe_spawn_cooldown <= 0:
    if spawn_pipe():
      pipe_spawn_cooldown = PIPE_COOLDOWN
  else:
    pipe_spawn_cooldown -= dt
  
  display_clouds()
  move_n_display_pipes(dt)
  
  if check_lose() or check_collision():
    game_over()
    break
  
  sleep(0.02)
