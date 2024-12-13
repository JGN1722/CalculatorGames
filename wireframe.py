from math import *
from kandinsky import *
from time import *

d = 256
points = [
  [1,1,1+5,0,0],
  [1,1,-1+5,0,0],
  [1,-1,1+5,0,0],
  [-1,1,1+5,0,0],
  [1,-1,-1+5,0,0],
  [-1,-1,1+5,0,0],
  [-1,1,-1+5,0,0],
  [-1,-1,-1+5,0,0],
  [0.5,0,-2+5,0,0],
  [-0.5,0,-2+5,0,0],
  [-1,0.3,0.1+5,0,0],
  [-1,-0.3,0.1+5,0,0],
  [-1,0.3,1+5,0,0],
  [-1,-0.3,1+5,0,0],
]
edges = [
  [0,1],
  [2,4],
  [1,4],
  [6,7],
  [5,7],
  [5,3],
  [3,0],
  [0,2],
  [7,4],
  [5,2],
  [6,1],
  [3,6],
  [1,8],
  [4,8],
  [8,9],
  [6,9],
  [7,9],
  [10,11],
  [10,12],
  [11,13],
]

def proj(x,y,z):
  proj_x = x*d/z
  proj_y = y*d/z
  return int(proj_x) + 320>>1,-int(proj_y) + 222>>1

def rotate():
  r = radians(monotonic())
  for p in points:
    x,y=p[0],p[1]
    rx = x*cos(0.1)-y*sin(0.1)
    ry = y*cos(0.1)+x*sin(0.1)
    #p[0],p[1]=rx,ry
    
    x,z=p[0],p[2]-5
    rx = x*cos(0.1)-z*sin(0.1)
    rz = z*cos(0.1)+x*sin(0.1)
    p[0],p[2]=rx,rz+5
    
    y,z=p[1],p[2]-5
    #ry = y*cos(0.1)-z*sin(0.1)
    #rz = z*cos(0.1)+y*sin(0.1)
    ry = y*cos(cos(monotonic())/20)-z*sin(cos(monotonic())/20)
    rz = z*cos(cos(monotonic())/20)+y*sin(cos(monotonic())/20)
    p[1],p[2]=ry,rz+5

for p in points:
  y,z=p[1],p[2]-5
  ry = y*cos(pi/2)-z*sin(pi/2)
  rz = z*cos(pi/2)+y*sin(pi/2)
  p[1],p[2]=ry,rz+5

def render():
  rotate()
  for p in points:
    x,y=proj(p[0],p[1],p[2])
    set_pixel(x,y,"black")
    p[3],p[4] = x,y
  for e in edges:
    v=[points[e[1]][3]-points[e[0]][3],points[e[1]][4]-points[e[0]][4]]
    
    if v[0] != 0:
      a=v[1]/v[0]
      x,y = points[e[0]][3],points[e[0]][4]
      f=1
      if v[0]<0:
        f=-1
        v[0]=abs(v[0])
      for i in range(v[0]):
        set_pixel(x+i*f,int(y+i*a*f),"black")
#    if v[0] != 0:
#      a=v[1]/v[0]
#      x,y = points[e[0]][3],points[e[0]][4]
#      f=1
#      if a<1:
#        if v[0]<0:
#          f=-1
#          v[0]=abs(v[0])
#        for i in range(v[0]):
#          set_pixel(x+i*f,int(y+i*a*f),"black")
#      else:
#        if v[1]<0:
#          f=-1
#          v[1]=abs(v[1])
#        for i in range(v[1]):
#          set_pixel(int(x+i*f/a),y+i*f,"black")
    elif v[1] != 0:
      a=v[0]/v[1]
      x,y = points[e[0]][3],points[e[0]][4]
      f=1
      if v[1]<0:
        f=-1
        v[1]=abs(v[1])
      for i in range(v[1]):
        set_pixel(int(x+i*a*f),y+i*f,"black")

while True:
  fill_rect(0,0,320,222,(255,255,255))
  render()
  sleep(0.05)
