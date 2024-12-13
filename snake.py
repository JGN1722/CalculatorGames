from kandinsky import *
from time import *
from random import *
from ion import *
ground=[]

class pix():
  def __init__(self):
    self.x=0
    self.y=0
  def appear(self,col,start=0):
    if start==0:
      xr=self.x-5
      yr=self.y-5
      for i in range(11):
        for n in range(11):
          yr=yr+1
          set_pixel(xr,yr,col)
        xr=xr+1
        yr=self.y-5
    else:
      fill_rect(self.x-5,self.y-5,11,11,col)

def s():
  x=15
  y=10
  di=90
  le=10
  ini="f"
  var=True
  arr=[]
  for n in range(29):
    for i in range(20):
      ground.insert(0,pix())
      ground[0].x=10+(n*11)-5
      ground[0].y=10+(i*11)-5
      ground[0].appear("white",1)
  while True:
    draw_string("score: "+str(le-10),0,0)
    if keydown(KEY_XNT):
      sleep(0.5)
      while True:
        sleep(0.05)
        if keydown(KEY_XNT):
          break
    if x<1 or x>27:
      break
    if y<1 or y>19:
      break
    if len(arr) > le*2:
      ground[arr[len(arr)-2]*20+arr[len(arr)-1]].appear("white")
      arr.pop()
      arr.pop()
    arr.insert(0,y)
    arr.insert(0,x)
    if keydown(KEY_LEFT) and di!=90:
      di=-90
      x=x+1
    elif keydown(KEY_RIGHT) and di!=-90:
      di=90
      x=x-1
    elif keydown(KEY_UP) and di!=180:
      di=0
      y=y+1
    elif keydown(KEY_DOWN) and di!=0:
      di=180
      y=y-1
    else:
      if di==90:
        x=x-1
      if di==-90:
        x=x+1
      if di==0:
        y=y+1
      if di==180:
        y=y-1
    if ini=="f":
      ini="t"
      spawn()
    if var==True:
      if get_pixel(ground[x*20+y].x,ground[x*20+y].y) == (0, 0, 248):
        ini="f"
        le=le+1
      if get_pixel(ground[x*20+y].x,ground[x*20+y].y) == (248, 0, 0):
        break
      ground[x*20+y].appear("red")
    sleep(0.05)
  le=le-10
  fill_rect(0,0,330,230,"white")
  draw_string("Game Over!",120,70)
  draw_string("You scored "+str(le)+" points",70,90)
  print("game over!")
  print("score: "+str(le))
  draw_string("Press XNT to play again",50,110)
  arr.clear()
  ground.clear()
  while True:
    if keydown(KEY_XNT):
      s()
    if keydown(KEY_OK):
      break
  
def spawn():
  o=randrange(1,27)
  t=randrange(1,18)
  if get_pixel(ground[o*20+t].x,ground[o*20+t].y)==(248,0,0):
    spawn()
  else:
    ground[o*20+t].appear("blue")
    
s()
