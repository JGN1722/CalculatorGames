from math import *
from kandinsky import *
from ion import *
from time import *
from random import *

px,py = 0,0
pdx,pdy,pa = 0,0,pi/4
shooting = None
bullets = 50

pi2 = pi/2
pi3 = (3*pi)/2
_2pi = 2*pi
shooting_angle = pi/50

map = [
  1,1,2,1,1,1,1,1,1,
  1,0,0,0,0,0,0,0,1,
  1,1,1,0,1,1,5,3,5,
  8,0,0,0,0,0,1,0,1,
  1,1,1,0,1,1,1,0,1,
  1,0,0,0,0,0,0,0,1,
  1,0,1,5,3,5,1,0,1,
  1,0,1,0,0,3,0,0,1,
  1,1,1,0,1,5,1,1,1,
  1,0,0,0,0,0,0,0,1,
  1,0,4,0,0,0,4,0,1,
  1,0,0,0,0,0,0,0,1,
  1,0,4,4,0,4,4,0,1,
  1,0,4,4,0,4,4,0,1,
  1,0,0,0,0,0,0,0,1,
  1,0,4,4,0,4,4,0,1,
  1,0,4,4,0,4,4,0,1,
  1,0,0,0,0,0,0,0,1,
#  1,1,1,1,1,1,1,1,1,
#]
#a=[
  1,1,1,1,1,1,5,3,5,
  1,0,0,0,0,0,0,0,1,
  1,0,4,4,4,4,4,0,1,
  1,0,5,0,0,0,4,0,1,
  1,0,3,0,6,0,4,0,1,
  1,0,5,0,0,0,4,0,1,
  1,0,4,4,4,4,4,0,1,
  1,0,0,0,0,0,0,0,1,
  1,1,7,7,3,7,7,1,1,
  1,1,1,1,0,1,1,1,1,
  1,0,0,0,0,0,0,0,1,
  1,0,1,1,1,1,1,0,1,
  1,0,1,0,0,0,1,0,1,
  1,0,1,0,1,0,1,0,1,
  1,0,1,0,1,0,1,0,1,
  1,0,0,0,0,0,0,0,1,
  1,1,1,1,1,1,1,1,1,
]

mapX=9
mapY=int(len(map)/mapX)
mapS=64
mapL=mapX*mapY

texture_size=8
textures = (
(
  0b01111110,
  0b01111110,
  0b00000000,
  0b11100111,
  0b11100111,
  0b00000000,
  0b01111110,
  0b01111110,
),
(
  0b10011111,
  0b10011011,
  0b11111111,
  0b11110111,
  0b10111101,
  0b10100101,
  0b10111101,
  0b11111111,
),
(
  0b00000000,
  0b11100111,
  0b10100101,
  0b10100101,
  0b00100100,
  0b11100111,
  0b11100111,
  0b00000000,
),
(
  0b11100011,
  0b11110001,
  0b11111000,
  0b01111100,
  0b00111110,
  0b00011111,
  0b10001111,
  0b11000111,
),
(
  0b00000000,
  0b01111110,
  0b00000000,
  0b01111110,
  0b01111110,
  0b00000000,
  0b01111110,
  0b00000000,
),
(
  0b00000000,
  0b00010000,
  0b00110000,
  0b01111110,
  0b01111110,
  0b00110000,
  0b00010000,
  0b00000000,
),
(
  0b00000000,
  0b01111110,
  0b01111110,
  0b01111110,
  0b01111110,
  0b01111110,
  0b01111110,
  0b00000000,
),
(
  0b00000000,
  0b00100100,
  0b00100100,
  0b00000000,
  0b00111100,
  0b01000010,
  0b01000010,
  0b00000000,
),
)
door_texture = 3

ennemy_sprites = (
(
  (2,0,1,2),
  (5,0,1,2),
  (2,3,4,1),
  (1,4,1,2),
  (6,4,1,2)
),
(
  (2,0,1,2),
  (5,0,1,2),
  (2,4,4,1),
  (1,5,1,2),
  (6,5,1,2)
),
(
  (2,0,1,2),
  (5,0,1,2),
  (2,5,4,1),
  (1,6,1,2),
  (6,6,1,2)
),
(
  (2,0,1,2),
  (5,0,1,2),
  (2,4,4,1),
  (1,5,1,2),
  (6,5,1,2)
)
)

entities = [
  #[ex,ey,es]
]

def move_player(dt):
  global px,py,pa,pdx,pdy,shooting,bullets
  
  xo,yo=20,20
  if pdx<0:  xo=-20
  if pdy<0:  yo=-20
  ipx,ipx_add_xo,ipx_sub_xo=int(px)>>6,int(px+xo)>>6,int(px-xo)>>6
  ipy,ipy_add_yo,ipy_sub_yo=int(py)>>6,int(py+yo)>>6,int(py-yo)>>6
  
  if keydown(KEY_OK):
    if map[ipy_add_yo*mapX+ipx_add_xo]==door_texture:
      map[ipy_add_yo*mapX+ipx_add_xo] = 0
    else:
      if shooting == None and bullets > 0:
        shooting = True
        bullets -= 1
  
  if shooting == False:
    shooting = None
  
  if keydown(KEY_UP):
    if map[ipy*mapX+ipx_add_xo]==0:  px += pdx*50*dt
    if map[ipy_add_yo*mapX+ipx]==0:  py += pdy*50*dt
  elif keydown(KEY_DOWN):
    if map[ipy*mapX+ipx_sub_xo]==0:  px -= pdx*50*dt
    if map[ipy_sub_yo*mapX+ipx]==0:  py -= pdy*50*dt
  
  if keydown(KEY_LEFT):
    tpa = pa - pi2
    tpdx,tpdy = cos(tpa)*50,sin(tpa)*50
    xo,yo=20,20
    if tpdx<0:  xo=-20
    if tpdy<0:  yo=-20
    ipx,ipx_add_xo,ipx_sub_xo=int(px)>>6,int(px+xo)>>6,int(px-xo)>>6
    ipy,ipy_add_yo,ipy_sub_yo=int(py)>>6,int(py+yo)>>6,int(py-yo)>>6
    if map[ipy*mapX+ipx_add_xo]==0:  px += tpdx*dt
    if map[ipy_add_yo*mapX+ipx]==0:  py += tpdy*dt
  elif keydown(KEY_RIGHT):
    tpa = pa + pi2
    tpdx,tpdy = cos(tpa)*50,sin(tpa)*50
    xo,yo=20,20
    if tpdx<0:  xo=-20
    if tpdy<0:  yo=-20
    ipx,ipx_add_xo,ipx_sub_xo=int(px)>>6,int(px+xo)>>6,int(px-xo)>>6
    ipy,ipy_add_yo,ipy_sub_yo=int(py)>>6,int(py+yo)>>6,int(py-yo)>>6
    if map[ipy*mapX+ipx_add_xo]==0:  px += tpdx*dt
    if map[ipy_add_yo*mapX+ipx]==0:  py += tpdy*dt
  if keydown(KEY_LEFTPARENTHESIS):
    pa = (pa - dt) % _2pi
    pdx = cos(pa)
    pdy = sin(pa)
  elif keydown(KEY_RIGHTPARENTHESIS):
    pa = (pa + dt) % _2pi
    pdx = cos(pa)
    pdy = sin(pa)

def dist(ax,ay,bx,by):
  return sqrt((bx-ax)*(bx-ax)+(by-ay)*(by-ay))

def dist_sq(ax,ay,bx,by):
  return (bx-ax)*(bx-ax)+(by-ay)*(by-ay)

def cast_rays():
  global mapS,mapX,mapY,map,s,distMax
  r,mx,my,mp,hit = 0,0,0,0,0
  rx,ry,ra,xo,yo = 0,0,0,0,0
  th,tv = 0,0
  ra = (pa - HALFFOV) % _2pi
  
  distMax = 0
  i = 0
  while i < RAYS:
    #horizontal
    if ra==0 or ra==pi:
      rx=px
      ry=py
      hit=True
    else:
      hit=False
      disH,hx,hy=1000000,px,py
      aTan = -1/tan(ra)
      if ra>pi:
        ry=((int(py)>>6)<<6)-0.0001
        rx=(py-ry)*aTan+px
        yo=-64
        xo=-yo*aTan
      if ra<pi:
        ry=((int(py)>>6)<<6)+64
        rx=(py-ry)*aTan+px
        yo= 64
        xo=-yo*aTan
    while not hit:
      mx=int(rx)>>6
      my=int(ry)>>6
      mp=my*mapX+mx
      if mp<0 or mp>=mapL or map[mp]>0:
        if mp>0 and mp<mapL:  th=map[mp]
        hx=rx
        hy=ry
        disH=dist_sq(px,py,hx,hy)
        hit=True
      else:
        rx+=xo
        ry+=yo
    
    #vertical
    if ra==pi2 or ra==pi3:
      rx=px
      ry=py
      hit=True
    else:
      hit=False
      disV,vx,vy=1000000,px,py
      nTan = -tan(ra)
      if ra>pi2 and ra<pi3:
        rx=((int(px)>>6)<<6)-0.0001
        ry=(px-rx)*nTan+py
        xo=-64
        yo=-xo*nTan
      if ra<pi2 or ra>pi3:
        rx=((int(px)>>6)<<6)+64
        ry=(px-rx)*nTan+py
        xo= 64
        yo=-xo*nTan
    while not hit:
      mx=int(rx)>>6
      my=int(ry)>>6
      mp=my*mapX+mx
      if mp<0 or mp>=mapL or map[mp]>0:
        if mp>0 and mp<mapL:  tv=map[mp]
        vx=rx
        vy=ry
        disV=dist_sq(px,py,vx,vy)
        hit=True
      else:
        rx+=xo
        ry+=yo
    
    if disV<disH:
      t=tv
      rx=vx
      ry=vy
      disT = disV
      shade = 0.7
    else:
      t=th
      rx=hx
      ry=hy
      disT = disH
      shade = 0.9
    disT = sqrt(disT)
    
    depth = shade*25600 / disT
    if depth > 128*shade: depth = 128*shade
        
    #draw 3D walls
    lineH = int((mapS<<8)/(disT*cos(pa-ra)))
    
    line8th=lineH/8
    
    tyo = 0
    if lineH>SCREENHEIGHT:
      tyo = int(lineH-SCREENHEIGHT)>>1
      lineH=SCREENHEIGHT
    
    o = int(SCREENHEIGHT-lineH)>>1
    
    if shade == 0.9:
      tx=int(rx%mapS)>>3 #given texture_size is 8
      if ra < pi:
        tx = texture_size-1-tx #flip texture
    else:
      tx=int(ry%mapS)>>3 #given texture_size is 8
      if ra > pi2 and ra < pi3:
        tx = texture_size-1-tx #flip texture
    txo = texture_size-1-tx
    
    s[i][0]       = o
    s[i][1]       = t
    s[i][2]     = txo
    s[i][3]     = tyo
    s[i][4]   = depth
    s[i][5]   = lineH
    s[i][6] = line8th
    
    s[i][7] = disT
    
    if disT > distMax:
      distMax = disT
    
    ra += deltaa
    if ra < 0:
      ra += _2pi
    elif ra > _2pi:
      ra -= _2pi
    i += 1

def render():
  global s
  
  x,i = 0,0
  while x < SCREENWIDTH:
    o       = s[i][0]
    t       = s[i][1]
    txo     = s[i][2]
    tyo     = s[i][3]
    depth   = s[i][4]
    lineH   = s[i][5]
    line8th = s[i][6]
    i += 1
    
    #if not tyo:  fill_rect(x,0,WIDTH,o,(100,150,255))
    if not tyo:  fill_rect(x,0,WIDTH,o,(75,75,75))
    
    if depth>20:
    #if False:
      off = o - tyo
      ct = -1
      
      if tyo:
        out_of_screen = int(tyo/line8th)
        begin = 1 + out_of_screen
        end = 8 - out_of_screen
        starty = out_of_screen*line8th
      else:
        begin,end = 1,8
        starty = 0
            
      c = (textures[t-1][begin - 1]>>(txo))&1
      l = line8th
      
      for y in range(begin,end):
        ct = (textures[t-1][y]>>(txo))&1
        if ct == c:
          l += line8th
        else:
          if c:  fill_rect(x,int(starty)+off,WIDTH,ceil(l),(depth,depth,depth))
          else:  fill_rect(x,int(starty)+off,WIDTH,ceil(l),(0,0,0))
          c = ct
          starty += l
          l = line8th
      if c:  fill_rect(x,int(starty)+off,WIDTH,ceil(l),(depth,depth,depth))
      else:  fill_rect(x,int(starty)+off,WIDTH,ceil(l),(0,0,0))
    else:
      fill_rect(x,o,WIDTH,lineH,(0,0,0))
      #fill_rect(x,o,WIDTH,lineH,(depth,depth,depth))
    if not tyo:  fill_rect(x,o+lineH,WIDTH,1+o,(100,100,100))
    
    x += WIDTH

def handle_and_render_sprites():
  global score,bullets
  i = 0
  
  while i < len(entities):
    ex,ey = entities[i][0],entities[i][1]
    
    #move
    if px > ex:
      xo = 20
    else:
      xo = -20
    if py > ey:
      yo = 20
    else:
      yo = -20
    ipx,ipx_add_xo=int(ex)>>6,int(ex+xo)>>6
    ipy,ipy_add_yo=int(ey)>>6,int(ey+yo)>>6
    if map[ipy*mapX+ipx_add_xo]==0:  ex += xo>>3
    if map[ipy_add_yo*mapX+ipx]==0:  ey += yo>>3
    entities[i][0] = ex
    entities[i][1] = ey
    
    dsq = (px-ex)**2+(py-ey)**2
    d = sqrt(dsq)
    
    if d > distMax:
      i += 1
      continue
    
    ax = px + pdx*d
    ay = py + pdy*d
    
    a = (ax-ex)**2+(ay-ey)**2
    
    delta = acos(1-a/(2*dsq))
    
    if delta <= HALFFOV:
      dist_to_high = (px+(pdx*COSPI6-pdy*SINPI6)*d-ex)**2+(py+(pdy*COSPI6+SINPI6*pdx)*d-ey)**2
      dist_to_low = (px+(pdx*COSPI6+pdy*SINPI6)*d-ex)**2+(py+(pdy*COSPI6-SINPI6*pdx)*d-ey)**2
      
      if dist_to_low < dist_to_high:
        delta = -delta
      
      #find if it's hidden
      ray = int(HALFRES*delta/HALFFOV)+HALFRES
      if s[ray][7] > d:
        scale = int(1280/d)
        
        projx = tan(delta)*d*COSPI6
        sx = int((projx*SCREENWIDTH)/d+HALFSCREENWIDTH)
        
        if shooting and projx < 10 and projx > -10:
          entities.remove(entities[i])
          score -= 1
          if not score:  win();draw_info()
          i += 1
          continue
        
        t = int(monotonic()%len(ennemy_sprites))
        sprite = ennemy_sprites[t]
        for r in range(len(sprite)):
          fill_rect(
            (sprite[r][0]-4)*scale+sx,
            (sprite[r][1]-4)*scale+HALFSCREENHEIGHT,
            sprite[r][2]*scale,
            sprite[r][3]*scale,
            (0,255,0)
          )
    
    if d < 20:
      game_over()
    
    i += 1

def draw_gun():
  global shooting
  if shooting:
    fill_rect(140,109,10,3,(255,0,0))
    fill_rect(170,109,10,3,(255,0,0))
    fill_rect(159,91,3,10,(255,0,0))
    fill_rect(159,121,3,10,(255,0,0))
    shooting = False
  else:
    fill_rect(140,109,10,3,(255,255,255))
    fill_rect(170,109,10,3,(255,255,255))
    fill_rect(159,91,3,10,(255,255,255))
    fill_rect(159,121,3,10,(255,255,255))
  
def init():
  global pdx,pdy,s,px,py,pa
  px,py = 64*5.5,64*3.5
  pdx,pdy,pa = 0,0,pi
  pdx,pdy = cos(pa),sin(pa)
  s.clear()
  for i in range(RAYS):
    s.append([0,0,0,0,0,0,0,0])

def spawn_entity():
  ex = randint(0,(mapX-1)<<6)
  ey = randint(0,(mapY-1)<<6)
  while map[(ey>>6)*mapX+(ex>>6)]!=0 or dist(px,py,ex,ey)<128:
    ex = randint(0,(mapX-1)<<6)
    ey = randint(0,(mapY-1)<<6)
  entities.append([ex,ey,0])

def rendergun():
  fill_rect(260,150,60,50,(100,100,150))
  fill_rect(240,140,40,40,(100,100,150))
  fill_rect(250,170,20,20,(100,100,150))
  fill_rect(270,145,40,20,(100,100,150))
  fill_rect(250,125,10,15,(100,100,150))
  fill_rect(280,180,45,40,(100,10,30))
  fill_rect(290,220,35,10,(100,10,30))
  fill_rect(282,170,35,10,(100,10,30))

def game_over():
  global playing
  draw_string("GAME OVER",115,60)
  playing = False

def win():
  global playing
  draw_string("YOU WIN",120,60)
  playing = False

def draw_info():
  draw_string("ennemies left: "+str(score),0,0,(255,255,255),(75,75,75))
  draw_string("bullets: "+str(bullets),0,20,(255,255,255),(75,75,75))

def display_start_screen():
  fill_rect(0,0,320,222,(255,255,255))
  draw_string("BAD GUYS SHOOTER",75,20,(255,0,0))
  draw_string("Numworks FPS",95,50)
  draw_string("Instructions:",95,80)
  draw_string("[ARROWS] move",95,110)
  draw_string("[PARENTHESIS] turn",70,130)
  draw_string("[OK] open doors and shoot",35,150)
  draw_string("[XNT] start the game",60,170)
  draw_string("Shoot all the bad guys!",50,200,(255,0,0))
  while not keydown(KEY_XNT):
    pass

playing = True
level = 1
def main():
  display_start_screen()
  init()
  cast_rays()
  dt = 0
  t1 = monotonic()
  t2 = t1
  f = t1
  c = 0
  level = 1
  for i in range(score):
    spawn_entity()
  i = 0
  while playing:
    t2 = monotonic()
    dt = t2 - t1
    t1 = t2
    move_player(dt)
    cast_rays()
    render()
    draw_info()
    handle_and_render_sprites()
    draw_gun()
    rendergun()

SCREENWIDTH = 320
SCREENHEIGHT = 222
HALFSCREENWIDTH = SCREENWIDTH>>1
HALFSCREENHEIGHT = SCREENHEIGHT>>1
FOV = pi/3
RAYS = 40
HALFRES = RAYS>>1
WIDTH = SCREENWIDTH//RAYS
s = []
distMax = 0
deltaa = FOV/RAYS

HALFFOV = pi/6
COSPI6 = sqrt(3)/2
SINPI6 = 1/2

score = 10

if SCREENWIDTH % RAYS != 0:
  print("Screen resolution not compatible\nwith screen width")
else:
  main()
