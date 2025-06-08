from kandinsky import *
from ion import *
from time import *

green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
p1 = (255,210,210)
p2 = (150,100,100)

EMPTY = -1
PAWN = 0b1
BISHOP = 0b10
KNIGHT = 0b11
ROOK = 0b100
QUEEN = 0b101
KING = 0b110
BLACK = 0b1000
WHITE = 0b0000

class Board:
  def __init__(self,f=True):
    fill_rect(0,0,320,222,green)
    self.b = [None] * 64
    self.o = BLACK
    self.f(f)
    
    self.lbx,self.lwx = -1,8
    self.lby,self.lwy = 0,0
  
  def notc(self,c):
    return WHITE if c else BLACK
  
  def display_lost(self,p):
    c = p & 8
    n = p & 7
    a = p2 if c else p1
    if c == WHITE:
      self.piece(n,self.lwx,self.lwy,a)
      self.lwy += 1
      if self.lwy == 8:
        self.lwy = 0
        self.lwx += 1
    if c == BLACK:
      self.piece(n,self.lbx,self.lby,a)
      self.lby += 1
      if self.lby == 8:
        self.lby = 0
        self.lbx -= 1
  
  def get(self,x,y):
    if x < 0 or x >= 8:  return EMPTY
    if y < 0 or y >= 8:  return EMPTY
    return self.b[y * 8 + x]
  
  def get_p(self,x,y):
    p = self.get(x,y)
    if p == EMPTY:  return EMPTY
    else:  return p & 8
  
  def set(self,x,y,v,nodraw=False):
    self.b[y * 8 + x] = v
    if not nodraw:  self.draw_square(x,y)
  
  def f(self,f):
    for i in range(64):
      self.b[i] = EMPTY
    if not f:  return
    for i in range(8):
      self.set(i,1,PAWN + WHITE)
      self.set(i,6,PAWN + BLACK)
    self.set(0,0,ROOK + WHITE);self.set(0,7,ROOK + BLACK)
    self.set(1,0,KNIGHT + WHITE);self.set(1,7,KNIGHT + BLACK)
    self.set(2,0,BISHOP + WHITE);self.set(2,7,BISHOP + BLACK)
    self.set(3,0,KING + WHITE);self.set(3,7,KING + BLACK)
    self.set(4,0,QUEEN + WHITE);self.set(4,7,QUEEN + BLACK)
    self.set(5,0,BISHOP + WHITE);self.set(5,7,BISHOP + BLACK)
    self.set(6,0,KNIGHT + WHITE);self.set(6,7,KNIGHT + BLACK)
    self.set(7,0,ROOK + WHITE);self.set(7,7,ROOK + BLACK)
  
  def draw(self):
    for x in range(8):
      for y in range(8):  self.draw_square(x,y)
  
  def piece(self,n,x,y,c):
    a = 0 if self.o else 1
    nc = black if (x + y + a) % 2 else white
    if x < 0 or x >= 8:  nc = green
    sx,sy = x*20,y*20
    if n == PAWN:
      fill_rect(85+sx,44+sy,10,3,c);fill_rect(87+sx,41+sy,6,3,c)
      fill_rect(88+sx,37+sy,4,6,c);fill_rect(88+sx,32+sy,4,5,c)
      fill_rect(87+sx,33+sy,6,4,c)
    elif n == BISHOP:
      fill_rect(87+sx,43+sy,6,4,c);fill_rect(88+sx,36+sy,4,7,c)
      fill_rect(87+sx,34+sy,6,5,c);fill_rect(88+sx,33+sy,4,1,c)
      fill_rect(89+sx,31+sy,2,2,c)
      for i in range(3):  set_pixel(87+sx+i,34+sy+i,nc)
    elif n == KNIGHT:
      fill_rect(87+sx,45+sy,8,2,c);fill_rect(88+sx,43+sy,6,2,c)
      fill_rect(90+sx,38+sy,3,7,c);fill_rect(88+sx,34+sy,5,4,c)
      fill_rect(86+sx,35+sy,2,3,c);fill_rect(89+sx,33+sy,4,1,c)
      fill_rect(91+sx,31+sy,2,2,c)
    elif n == ROOK:
      fill_rect(87+sx,43+sy,6,4,c);fill_rect(88+sx,36+sy,4,7,c)
      fill_rect(87+sx,34+sy,6,5,c);fill_rect(88+sx,34+sy,1,2,nc)
      fill_rect(91+sx,34+sy,1,2,nc)
    elif n == QUEEN:
      fill_rect(86+sx,45+sy,8,2,c);fill_rect(87+sx,43+sy,6,2,c)
      fill_rect(88+sx,36+sy,4,7,c);fill_rect(87+sx,35+sy,6,1,c)
      fill_rect(86+sx,33+sy,8,2,c);fill_rect(85+sx,34+sy,10,1,c)
      fill_rect(87+sx,32+sy,6,1,c)
    elif n == KING:
      fill_rect(86+sx,45+sy,8,2,c);fill_rect(87+sx,43+sy,6,2,c)
      fill_rect(88+sx,38+sy,4,5,c);fill_rect(87+sx,37+sy,6,1,c)
      fill_rect(86+sx,35+sy,8,2,c);fill_rect(89+sx,31+sy,2,4,c)
      fill_rect(88+sx,32+sy,4,1,c)
  
  def select(self,x,y,c=red):
    if self.o == WHITE:  y = 7 - y
    sx,sy = 20 * x + 80,20 * y + 30
    fill_rect(sx,sy,2,5,c);fill_rect(sx,sy,5,2,c)
    fill_rect(sx+15,sy,5,2,c);fill_rect(sx+18,sy,2,5,c)
    fill_rect(sx,sy+15,2,5,c);fill_rect(sx,sy+18,5,2,c)
    fill_rect(sx+18,sy+15,2,5,c);fill_rect(sx+15,sy+18,5,2,c)
  
  def unselect(self,x,y):
    self.draw_square(x,y)
  
  def draw_square(self,x,y):
    dy = 7 - y if self.o == WHITE else y
    c = black if (x + y) & 1 else white
    p = p2 if self.get_p(x,y) else p1
    fill_rect(x*20+80,dy*20+30,20,20,c)
    self.piece(self.get(x,y) & 7,x,dy,p)
  
  def is_square_checked(self,x,y,c):
    nc = self.notc(c)
    for sx,sy in ((x+2,y-1),(x+2,y+1),
                  (x-2,y-1),(x-2,y+1),
                  (x+1,y-2),(x-1,y-2),
                  (x+1,y+2),(x-1,y+2)):
      if sy < 0 or sy >= 8:       continue
      if sx < 0 or sx >= 8:       continue
      if self.get(sx,sy) == nc + KNIGHT:
        return True
    if c == WHITE:  mod =  1
    else:           mod = -1
    if self.get(x + 1,y + mod) == PAWN + nc:
      return True
    if self.get(x - 1,y + mod) == PAWN + nc:
      return True
    for sx in (x + 1,x,x - 1):
      for sy in (y + 1,y,y - 1):
        if self.get(sx,sy) == nc + KING:
          return True
    for sx in (-1,1):
      for sy in (-1,1):
        i = 1
        while self.get(x+sx*i,y+sy*i) == EMPTY:
          if y+sy*i < 0 or y+sy*i >= 8:  break
          if x+sx*i < 0 or x+sx*i >= 8:  break
          i += 1
        if self.get(x+sx*i,y+sy*i) in (QUEEN+nc,BISHOP+nc):
          return True
    for s in (-1,1):
      i = 1
      while self.get(x+s*i,y) == EMPTY:
        if x+s*i < 0 or x+s*i >= 8:  break
        i += 1
      if self.get(x+s*i,y) in (QUEEN+nc,ROOK+nc):
        return True
    for s in (-1,1):
      i = 1
      while self.get(x,y+s*i) == EMPTY:
        if y+s*i < 0 or y+s*i >= 8:  break
        i += 1
      if self.get(x,y+s*i) in (QUEEN+nc,ROOK+nc):
        return True
    
    return False
  
  def is_king_checked(self,c):
    for sx in range(8):
      for sy in range(8):
        if self.get(sx,sy) == KING + c:
          return self.is_square_checked(sx,sy,c)
  
  def is_checkmate(self,c):
    for sx in range(8):
      for sy in range(8):
        if self.get(sx,sy) == KING + c:
          x,y = sx,sy
        elif self.get_p(sx,sy) == c:
          if self.get_moves(sx,sy) != []:
            return False
    
    if self.is_square_checked(x,y,c):
      if self.get_moves(x,y) == []:  return True
    return False
  
  def move_takes(self,dx,dy,c):
    return self.get_p(dx,dy) not in (c,EMPTY)
  
  def make_move(self,px,py,sx,sy):
    p = self.get(px,py)
    e = self.get(sx,sy)
    if e != EMPTY:  self.display_lost(e)
    self.set(sx,sy,p)
    self.set(px,py,EMPTY)
    
    if p == PAWN + WHITE and sy == 7:
      self.set(sx,sy,QUEEN + WHITE)
    elif p == PAWN + BLACK and sy == 0:
      self.set(sx,sy,QUEEN + BLACK)
    
    c = self.notc(p & 8)
    if self.is_checkmate(c):
      u = "Black" if c == BLACK else "White"
      draw_string("Checkmate for " + u + "!",60,5,black,green)
      return True
    return False
  
  def simulate_moves(self,x,y,dx,dy):
    p,d = self.get(x,y),self.get(dx,dy)
    self.set(x,y,EMPTY,True)
    self.set(dx,dy,p,True)
    m = self.get_moves(dx,dy)
    self.set(x,y,p,True)
    self.set(dx,dy,d,True)
    return m
  
  def get_moves(self,x,y):
    p = self.get(x,y)
    c,p = p & 8,p & 7
    m = []
        
    if p == PAWN:
      if c:  s = -1
      else:  s = 1
      if self.get(x,y+s) == EMPTY:
        m = [(x,y+s)]
        if (c,y) in ((WHITE,1),(BLACK,6)):
          if self.get(x,y+2*s) == EMPTY:
            m.append((x,y+2*s))
      if self.move_takes(x+1,y+s,c):
        m.append((x+1,y+s))
      if self.move_takes(x-1,y+s,c):
        m.append((x-1,y+s))
    if p == ROOK or p == QUEEN:
      for s in (-1,1):
        i = 1
        while self.get(x+s*i,y) == EMPTY:
          if x+s*i < 0 or x+s*i >= 8:  break
          m.append((x+s*i,y))
          i += 1
        if self.move_takes(x+s*i,y,c):
          m.append((x+s*i,y))
      for s in (-1,1):
        i = 1
        while self.get(x,y+s*i) == EMPTY:
          if y+s*i < 0 or y+s*i >= 8:  break
          m.append((x,y+s*i))
          i += 1
        if self.move_takes(x,y+s*i,c):
          m.append((x,y+s*i))
    if p == BISHOP or p == QUEEN:
      for sx in (-1,1):
        for sy in (-1,1):
          i = 1
          while self.get(x+sx*i,y+sy*i) == EMPTY:
            if y+sy*i < 0 or y+sy*i >= 8:  break
            if x+sx*i < 0 or x+sx*i >= 8:  break
            m.append((x+sx*i,y+sy*i))
            i += 1
          if self.move_takes(x+sx*i,y+sy*i,c):
            m.append((x+sx*i,y+sy*i))
    if p == KING:
      for dx in (x-1,x,x+1):
        for dy in (y-1,y,y+1):
          if (dx,dy) == (x,y):  continue
          if dy < 0 or dy >= 8:  continue
          if dx < 0 or dx >= 8:  continue
          if self.get_p(dx,dy) == c:  continue
          if self.is_square_checked(dx,dy,c):
            continue
          m.append((dx,dy))
    if p == KNIGHT:
      for sx,sy in ((x+2,y-1),(x+2,y+1),
                    (x-2,y-1),(x-2,y+1),
                    (x+1,y-2),(x-1,y-2),
                    (x+1,y+2),(x-1,y+2)):
        if sy < 0 or sy >= 8:       continue
        if sx < 0 or sx >= 8:       continue
        if self.get_p(sx,sy) == c:  continue
        m.append((sx,sy))
    
    t = []
    for i in range(len(m)):
      o = self.get(m[i][0],m[i][1])
      self.set(x,y,EMPTY,True)
      self.set(m[i][0],m[i][1],p+c,True)
      if self.is_king_checked(c):
        t.append(i)
      self.set(x,y,p+c,True)
      self.set(m[i][0],m[i][1],o,True)
    t.reverse()
    for i in t:  del m[i]
    
    return m


def title_screen():
  b = Board(False)
  b.set(1,1,KING+WHITE);b.set(0,2,PAWN+WHITE)
  b.set(2,3,PAWN+WHITE);b.set(3,2,PAWN+WHITE)
  b.set(3,5,QUEEN+WHITE);b.set(3,6,ROOK+WHITE)
  b.set(0,4,KING+BLACK);b.set(1,4,PAWN+BLACK)
  b.set(0,6,PAWN+BLACK);b.set(7,6,PAWN+BLACK)
  b.draw()
  draw_string("NUMCHESS",120,5,black,green)
  draw_string("By JGN",130,180,black,green)
  draw_string("Press [XNT] to start",60,200,black,green)
  while not keydown(KEY_XNT):  pass
  while     keydown(KEY_XNT):  pass

def instructions():
  global bot,timer
  i = 0
  gm = ["-Casual PvP","-Timed PvP","-Versus bot"]
  
  fill_rect(0,0,320,222,green)
  draw_string("Press [OK] to select a piece",10,5,black,green)
  draw_string("Then, press [OK] to select a\n move",10,30,black,green)
  draw_string("Select a game mode with [OK]",10,90,black,green)
  
  draw_string(gm[0],20,110,green,black)
  for j in range(1,len(gm)):
    draw_string(gm[j],20,110 + j * 20,black,green)
  
  while not keydown(KEY_OK):
    a = [keydown(KEY_UP),keydown(KEY_DOWN)]
    if a != [False,False]:
      if a[0]:  i = (i - 1) % 3
      if a[1]:  i = (i + 1) % 3
      for j in range(len(gm)):
        draw_string(gm[j],20,110 + j * 20,black,green)
      draw_string(gm[i],20,110 + i * 20,green,black)
      while a != [False] * 2:
        a = [keydown(KEY_UP),keydown(KEY_DOWN)]
      if i == 0:  bot,timer = False,False
      if i == 1:  bot,timer = False,True
      if i == 2:  bot,timer = True,False
  while     keydown(KEY_OK):  pass

def check_reta(b,px,py,x,y):
  p,e = b.get(px,py),b.get(x,y)
  b.set(px,py,EMPTY,True)
  b.set(x,y,p,True)
  
  r = 0
  if b.is_square_checked(x,y,BLACK):
    r = p - BLACK
  
  b.set(px,py,p,True)
  b.set(x,y,e,True)
  return r

def choose_bot_move(b):
  #print("=================")
  px,py,maxm,maxp = 0,0,0,0
  dx,dy,score = 0,0,EMPTY-1
  fpx,fpy,fcx,fcy = -1,-1,-1,-1
  for sy in range(8):
    for sx in range(8):
      if b.get_p(sx,sy) != BLACK:  continue
      p,m = b.get(sx,sy)-BLACK,b.get_moves(sx,sy)
      #print("p =",p)
      if m != []:
        if (fcx,fcy) == (-1,-1):  fcx,fcy = sx,sy
        if (p,fpx,fpy) == (PAWN,-1,-1):  fpx,fpy = sx,sy
      for x,y in m:
        change = False
        if b.is_square_checked(sx,sy,BLACK):
          s = p
        else:  s = 0
        s += b.get(x,y) - check_reta(b,sx,sy,x,y)
        m2 = b.simulate_moves(sx,sy,x,y)
        if m2 == [(sx,sy)]:  m2 = []
        #print("s:",score,"len(m):",len(m2))
        if s > score:  change = True
        elif s == score:
          if len(m2) > maxm:  change = True
          elif len(m2) == maxm:
            if p > maxp:  change = True
        
        if change:
          px,py,dx,dy = sx,sy,x,y
          score,maxp,maxm = s,p,len(m2)
          #print("new max",s,p,len(m2))
  
  if (px,py,dx,dy) == (0,0,0,0):
    if (fpx,fpy) == (-1,-1):
      m = b.get_moves(fcx,fcy)
      px,py,dx,dy = fcx,fcy,m[-1][0],m[-1][1]
    else:
      m = b.get_moves(fpx,fpy)
      px,py,dx,dy = fpx,fpx,m[-1][0],m[-1][1]
  
  #print("choice s",score,"m",maxm,"p",maxp)
  return px,py,dx,dy

def clock(x,t,fr,bg):
  t = int(t)
  si = t % 60
  mi = (t // 60)
  s = str(si) if si > 9 else "0" + str(si)
  m = str(mi) if mi > 9 else "0" + str(mi)
  draw_string(m+":"+s,min(x,270),0,fr,bg)

def game():
  turn,sx,sy,px,py,s,m = 0,0,0,0,0,False,[]
  
  b = Board()
  b.o = WHITE
  b.draw()
  b.select(0,0)
  
  draw_string("White's turn",100,5,black,green)
  
  if timer:
    tw,tb = 0,0
    t1 = monotonic()
    limit = 600
    clock(320,limit,white,black)
  
  while True:
    
    if timer:
      t2 = monotonic()
      dt = t2 - t1
      t1 = t2
      if turn & 1:
        tb += dt
        if tb > limit:
          draw_string("Black is out of time!",55,5,black,green)
          break
        clock(320,limit-tb,white,black)
      else:
        tw += dt
        if tw > limit:
          draw_string("White is out of time!",55,5,black,green)
          break
        clock(0,limit-tw,black,white)
    
    if bot and turn & 1:
      draw_string("Loading...",110,195,black,green)
      px,py,x,y = choose_bot_move(b)
      if b.make_move(px,py,x,y):
        fill_rect(110,195,100,20,green)
        break
      fill_rect(110,195,100,20,green)
      draw_string("White's turn",100,5,black,green)
      turn += 1
      b.select(sx,sy)
    
    a = [keydown(KEY_UP),keydown(KEY_DOWN),
        keydown(KEY_LEFT),keydown(KEY_RIGHT)]
    if a != [False] * 4:
      if (sx,sy) in m:  b.select(sx,sy,blue)
      else:  b.unselect(sx,sy)
      mod = 1 if turn & 1 else -1
      if   a[0]:  sy = (sy - 1 * mod) & 7
      elif a[1]:  sy = (sy + 1 * mod) & 7
      elif a[2]:  sx = (sx - 1) & 7
      elif a[3]:  sx = (sx + 1) & 7
      b.select(sx,sy)
      while a != [False] * 4:
        a = [keydown(KEY_UP),keydown(KEY_DOWN),
            keydown(KEY_LEFT),keydown(KEY_RIGHT)]
    
    if keydown(KEY_OK) and not s:
      p = b.get(sx,sy)
      if p & 8 != (turn & 1)<<3 or p == EMPTY:
        continue
      px,py = sx,sy
      m = b.get_moves(sx,sy)
      for x,y in m:  b.select(x,y,blue)
      while keydown(KEY_OK):  pass
      s = m != []
    
    if keydown(KEY_OK) and s:
      if not (sx,sy) in m:  continue
      checkmate = b.make_move(px,py,sx,sy)
      for x,y in m:  b.draw_square(x,y)
      m.clear()
      if checkmate:  break
      s = False
      while keydown(KEY_OK):  pass
      turn += 1
      if not bot:
        b.o = (turn&1)<<3
        b.draw()
      b.select(sx,sy)
      u = "Black" if turn & 1 else "White"
      draw_string(u + "'s turn",100,5,black,green)

bot = True
timer = False

title_screen()
instructions()
game()
