from kandinsky import *
from time import *
from ion import *
from random import *

blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
bluegreen = (0,180,100)
lightblue = (0,225,225)
deepblue = (0,200,200)
orange = (255,100,0)
red = (255,0,0)
beige = (255,222,198)
darkbeige = (255, 203, 99)
violet = (107, 44, 123)
darkgreen = (0,185,0)
lightred = (255,100,100)
white = (255,255,255)
black = (0,0,0)
black2 = (8,8,8)
grey = (100,100,100)
lightgrey = (200,200,200)
brown = (100,0,0)
grass = (200,255,200)
green2 = (0,240,0)
#lighterblue = (200,200,255)
#lightorange = (255,200,100)

class PokemonReference:
  def __init__(self,color,maxhp,atk):
    self.color = color
    self.maxhp = maxhp
    self.atk = atk

pokemons = {
  "pichu": PokemonReference(yellow,30,5),
  "pikachu": PokemonReference(yellow,60,15),
  "raichu": PokemonReference(yellow,90,20),
  "bulbizarre": PokemonReference(bluegreen,50,10),
  "herbizarre": PokemonReference(bluegreen,70,15),
  "florizarre": PokemonReference(bluegreen,100,25),
  "carapuce": PokemonReference(lightblue,50,10),
  "carabaffe": PokemonReference(deepblue,80,12),
  "tortank": PokemonReference(lightblue,110,20),
  "salameche": PokemonReference(orange,50,10),
  "reptincel": PokemonReference(red,60,20),
  "dracaufeu": PokemonReference(orange,90,30),
  "evoli": PokemonReference(beige,40,8),
  "voltali": PokemonReference(yellow,55,26),
  "aquali": PokemonReference((100,100,255),50,26),
  "pyroli": PokemonReference((255,100,100),55,25),
  "rattata": PokemonReference(violet,30,5),
  "rattatac": PokemonReference(darkbeige,50,15),
  "feuillajou": PokemonReference(darkgreen,40,10),
  "feuilloutan": PokemonReference(darkgreen,70,20),
  "flotajou": PokemonReference(lightblue,40,10),
  "flotoutan": PokemonReference(lightblue,70,20),
  "flamajou": PokemonReference(red,40,10),
  "flamoutan": PokemonReference(red,70,20),
  "darumarond": PokemonReference(lightred,35,10),
  "darumacho": PokemonReference(lightred,80,20),
  "statitik": PokemonReference(yellow,30,8),
  "mygavolt": PokemonReference(yellow,60,16),
  "canartichaut": PokemonReference((200,100,100),45,12),
  "roucool": PokemonReference(beige,30,5),
  "roucoups": PokemonReference(beige,50,15),
  "roucarnage": PokemonReference(beige,90,20),
  "poichigeon": PokemonReference(lightgrey,30,5),
  "colombeau": PokemonReference(lightgrey,55,12),
  "deflaisan": PokemonReference(lightgrey,70,15),
  #"minidraco": PokemonReference(lighterblue,35,8),
  #"draco": PokemonReference(lighterblue,55,18),
  #"dracolosse": PokemonReference(lightorange,100,30),
  "reshiram": PokemonReference(white,165,40),
  "zekrom": PokemonReference(black,165,40),
  "kyurem": PokemonReference(grey,165,40),
}

poke_families = [
  ["pichu","pikachu","raichu"],
  ["bulbizarre","herbizarre","florizarre"],
  ["carapuce","carabaffe","tortank"],
  ["salameche","reptincel","dracaufeu"],
  ["evoli","pyroli"],
  ["evoli","aquali"],
  ["evoli","voltali"],
  ["rattata","rattatac"],
  ["feuillajou","feuilloutan"],
  ["flotajou","flotoutan"],
  ["flamajou","flamoutan"],
  ["darumarond","darumacho"],
  ["statitik","mygavolt"],
  ["canartichaut"],
  ["roucool","roucoups","roucarnage"],
  ["poichigeon","colombeau","deflaisan"],
  ["","","","reshiram"],
  ["","","","zekrom"],
  ["","","","kyurem"],
]

map = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
  [0,0,0,1,0,0,0,0,0,0,0,0,1,0,5,0,0,0],
  [0,0,0,0,0,0,1,0,0,1,0,1,1,5,5,1,0,0],
  [0,0,0,0,0,0,1,0,0,0,0,0,2,5,5,5,0,0],
  [0,0,1,0,0,3,3,3,3,0,2,2,2,0,0,0,0,0],
  [0,0,0,0,0,3,4,4,3,0,2,0,0,0,0,1,0,0],
  [0,0,0,0,0,3,4,4,4,2,2,0,3,3,3,3,0,0],
  [0,0,0,0,0,3,3,3,3,0,2,0,3,4,4,3,0,0],
  [0,0,0,1,0,0,0,0,0,0,2,2,4,4,4,3,0,1],
  [0,0,0,0,0,0,0,1,0,0,0,0,3,3,3,3,0,0],
  [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
]
mapx = len(map[0])
mapy = len(map)

px = 1 + mapx // 2
py = 1 + mapy // 2

def get_poke_color(name):
  return pokemons[name].color

def get_poke_hp(name):
  return pokemons[name].maxhp

def get_poke_atk(name):
  return pokemons[name].atk

def get_poke_family(name):
  for f in poke_families:
    if name in f:
      return f

def get_poke_fam_rank(name):
  f = get_poke_family(name)
  for i in range(len(f)):
    if f[i] == name:
      return i

def get_poke_evo(name):
  if name == "evoli":
    return choice(["pyroli","aquali","voltali"])
  f = get_poke_family(name)
  for i in range(len(f) - 1):
    if f[i] == name:
      return f[i + 1]
  return name

class Pokemon:
  def __init__(self, name, lvl):
    self.name = name
    self.lvl = lvl

equipe = [None,None,None]
reserve = [None,None,None]

def display_pokemon(name,x,y):
  c = get_poke_color(name)
  o = len(name) * 5
  fill_rect(x-10,y-10,20,20,c)
  draw_string(name,x-o,y+20)

def clear_pokemon(x,y):
  fill_rect(x-60,y-20,120,60,green)

def display_health(name,x,hp):
  w = max(len(name)*10+10,70+10)
  x = min(x,320-w)
  fill_rect(x,0,w,50,white)
  draw_string(name,x+5,5)
  
  f = int(70*max(hp,0)/get_poke_hp(name))
  d = 70 - f
  fill_rect(x+5,30,f,10,green)
  fill_rect(x+5+f,30,d,10,red)

def display_ennemy(name,hp):
  display_pokemon(name,250,80)
  display_health(name,320,hp)

def display_player(name,hp):
  display_pokemon(name,70,80)
  display_health(name,0,hp)

def animate_ennemy(name):
  clear_pokemon(250,80)
  display_pokemon(name,250+10,80)
  sleep(0.25)
  clear_pokemon(250+10,80)
  display_pokemon(name,250,80+10)
  sleep(0.25)
  clear_pokemon(250,80+10)
  display_pokemon(name,250-10,80)
  sleep(0.25)
  clear_pokemon(250-10,80)
  display_pokemon(name,250,80-10)
  sleep(0.25)
  clear_pokemon(250,80-10)
  display_pokemon(name,250,80)

def animate_player(name):
  clear_pokemon(70,80)
  display_pokemon(name,70+10,80)
  sleep(0.25)
  clear_pokemon(70+10,80)
  display_pokemon(name,70,80+10)
  sleep(0.25)
  clear_pokemon(70,80+10)
  display_pokemon(name,70-10,80)
  sleep(0.25)
  clear_pokemon(70-10,80)
  display_pokemon(name,70,80-10)
  sleep(0.25)
  clear_pokemon(70,80-10)
  display_pokemon(name,70,80)

# max 3 lines, blocking
# overflow in another box
def dialog_box(a):
  if len(a) < 30 * 3 - 10:
    _dialog_box(a)
  else:
    while len(a) != 0:
      _dialog_box(a[:30*3-10])
      a = a[30*3-10:]
def _dialog_box(a):
  b,c,i,x,y,w,h = 3,a,0,10,135,300,77
  t,v = b+3,b+3
  fill_rect(x,y,w,h,black)
  fill_rect(x+b,y+b,w-2*b,h-b*2,white)
  while i < len(c)+1:
    if v + i *10 > w:
      v,c,i = v+20,c[i-1:],0
    if v > 60:
      break
    draw_string(c[:i],x+t,y+v)
    sleep(0.02)
    i += 1
  draw_string("[OK]",x+w-40-t,y+h-20-t)
  while not keydown(KEY_OK):  pass
  while keydown(KEY_OK):  pass
  fill_rect(x+b,y+b,w-b*2,h-b*2,white)

def option_box(a,n,m):
  r = 0
  b,c,i,x,y,w,h = 3,a,0,10,135,300,77
  t,v = b+3,b+3
  fill_rect(x,y,w,h,black)
  fill_rect(x+b,y+b,w-2*b,h-b*2,white)
  while i < len(c)+1 and v + i *10 < w:
    draw_string(c[:i],x+t,y+v)
    sleep(0.02)
    i += 1
  v += 20
  draw_string(">"+n,x+t,y+v)
  v += 20
  draw_string(" "+m,x+t,y+v)
  draw_string("[OK]",x+w-40-t,y+h-20-t)
  while not keydown(KEY_OK):
    if keydown(KEY_UP) or keydown(KEY_DOWN):
      while keydown(KEY_UP) or keydown(KEY_DOWN):  pass
      v = b+3+20
      if not r:
        draw_string(" "+n,x+t,y+v)
        draw_string(">"+m,x+t,y+v+20)
        r = 1
      else:
        draw_string(">"+n,x+t,y+v)
        draw_string(" "+m,x+t,y+v+20)
        r = 0
      draw_string("[OK]",x+w-40-t,y+h-20-t)
  while keydown(KEY_OK):  pass
  fill_rect(x+b,y+b,w-b*2,h-b*2,white)
  return r

def fade(c):
  for i in range(32*23):
    x,y=randint(0,31)*10,randint(0,22)*10
    while get_pixel(x,y) == c:
      x,y=randint(0,31)*10,randint(0,22)*10
    fill_rect(x,y,10,10,c)

def draw_person(shirt,pants,hair,x=160,y=110):
  fill_rect(x-20,y-25,40,50,shirt)
  fill_rect(x-30,y-20,10,30,shirt)
  fill_rect(x+20,y-20,10,30,shirt)
  
  fill_rect(x-30,y+10,10,10,beige)
  fill_rect(x+20,y+10,10,10,beige)
  
  fill_rect(x-20,y+25,40,15,pants)
  fill_rect(x-20,y+25,15,50,pants)
  fill_rect(x+5,y+25,15,50,pants)
  
  fill_rect(x-15,y-50,30,25,beige)
  fill_rect(x-15,y-55,30,5,hair)

def fight(name, nocatch=False):
  fade(black2)
  fade(green)
  
  dialog_box("Un " + name + " sauvage apparait !")
  
  ennemy_hp = get_poke_hp(name)
  team_hp = [get_poke_hp(p.name) if p else None for p in equipe]
  
  active_pokemon = 0
  player_name = equipe[active_pokemon].name
  player_hp = team_hp[active_pokemon]
  
  display_ennemy(name,ennemy_hp)
  display_player(player_name,player_hp)
  
  # action loop
  while True:
    if option_box("Que faites vous ?", "Attaquer", "Fuir"):
      dialog_box("Vous fuyez le combat")
      fade(black2)
      return
    else:
      
      # attack
      animate_player(player_name)
      dmg = get_poke_atk(player_name)
      ennemy_hp -= dmg
      display_ennemy(name,ennemy_hp)
      dialog_box("Vous infligez " + str(dmg) + " degats a " + name)
      
      if ennemy_hp <= 0: # if ennemy dies
        ennemy_hp = 0
        dialog_box(name + " est vaincu !")
        break
        
    # ennemy attack
    animate_ennemy(name)
    dmg = get_poke_atk(name)
    player_hp -= dmg
    display_player(player_name,player_hp)
    dialog_box("Vous subissez " + str(dmg) + " degats")
    
    if player_hp <= 0: # if player dies
      dialog_box(player_name + " est vaincu !")
      if active_pokemon == 2 or not team_hp[active_pokemon + 1]:
        break # if no more pokemons
      active_pokemon += 1
      player_name = equipe[active_pokemon].name
      player_hp = team_hp[active_pokemon]
      display_player(player_name,player_hp)
  
  
  # if ennemy is dead
  if ennemy_hp == 0:
    dialog_box("Vous avez gagne !")
    
    for i in range(active_pokemon+1):
      dialog_box(equipe[i].name + " gagne un niveau !")
      equipe[i].lvl += 1
    
      # evolution
      if equipe[i].lvl % 10 == 0:
        evo = get_poke_evo(equipe[i].name)
        if evo != equipe[i].name:
          dialog_box(equipe[i].name + " evolue en " + evo + " !")
          equipe[i].name = evo
          if i == active_pokemon:
            display_player(evo,player_hp)
      else:
        pass # already at maximum
    
    if not nocatch and None in equipe:
      if not option_box("Voulez vous attraper " + name + " ?","Yes","No"):
        lvl = get_poke_fam_rank(name) * 10
        if lvl == 0:  lvl = 1
        
        if not equipe[1]:  i = 1
        else:  i = 2
        equipe[i] = Pokemon(name,lvl)
        dialog_box(name + " a rejoint votre equipe")
  else:
    dialog_box("Vous etes vaincu")
  
  fade(black2)

def text_center(text,y,c=black,bc=white):
  x = 160 - len(text) * 5
  draw_string(text,x,y,c,bc)

def title_screen():
  fill_rect(0,0,320,222,green2)
  text_center("Pokemon",10,bc=green2)
  text_center("Numworks edition",30,bc=green2)
  text_center("Press [XNT] to start",200,bc=green2)
  draw_person(shirt=white,pants=blue,hair=grey,x=220)
  draw_person(shirt=red,pants=blue,hair=brown,x=100)
  display_pokemon("salameche",160,160)
  display_pokemon("carapuce",60,150)
  display_pokemon("bulbizarre",260,150)
  while not keydown(KEY_XNT):
    pass

def start():
  fade(green)
  
  draw_person(shirt=white,pants=blue,hair=grey)
  
  dialog_box("Bonjour et bienvenue ! Je suis le professeur Chen")
  dialog_box("Choisissez votre Pokemon de depart: bulbizarre, salameche ou carapuce ?")
  
  starters = ["bulbizarre","salameche","carapuce"]
  i = 0
  
  while option_box("Voulez vous " + starters[i] + " ?","Oui","Non"):
    i = (i + 1) % len(starters)
  
  dialog_box("Vous avez choisi " + starters[i] + " !")
  equipe[0] = Pokemon(starters[i],1)
  
  dialog_box("Essayons un premier combat")
  fight("evoli", nocatch=True)

def draw_grass(x,y):
  fill_rect(x,y,30,30,grass)

def draw_path(x,y):
  fill_rect(x,y,30,30,(255,180,150))

def draw_tree(x,y):
  fill_rect(x,y,30,30,grass)
  fill_rect(x+10,y+5,10,20,green)
  fill_rect(x+5,y+10,20,15,green)
  fill_rect(x+10,y+25,10,4,brown)

def draw_wall(x,y):
  fill_rect(x,y,30,30,(200,0,0))
  fill_rect(x,y,30,2,grey)
  fill_rect(x,y+8,30,4,grey)
  fill_rect(x,y+18,30,4,grey)
  fill_rect(x,y+28,30,2,grey)
  
  fill_rect(x,y,2,8,grey)
  fill_rect(x+13,y,4,8,grey)
  fill_rect(x+28,y,2,8,grey)
  
  fill_rect(x+8,y+12,4,8,grey)
  fill_rect(x+18,y+12,4,8,grey)
  
  fill_rect(x,y+22,2,8,grey)
  fill_rect(x+13,y+22,4,8,grey)
  fill_rect(x+28,y+22,2,8,grey)

def draw_floor(x,y):
  fill_rect(x,y,30,30,lightgrey)

def draw_water(x,y):
  fill_rect(x,y,30,30,(100,100,255))

def draw_player(x,y):
  fill_rect(x+11,y+2,7,6,beige)
  fill_rect(x+10,y+8,10,10,red)

  fill_rect(x+10,y+15,10,7,blue)

def render_map(dx=0,dy=0):
  for x in range(px-6,px+6):
    for y in range(py-5,py+5):
      sx = 160+(x-px)*30
      sy = 110+(y-py)*30
      if not x in range(1,mapx+1) or not y in range(1,mapy+1):
        draw_tree(sx+dx,sy+dy)
      else:
        t = tile(x,y)
        if t == 0:
          draw_grass(sx+dx,sy+dy)
        elif t == 1:
          draw_tree(sx+dx,sy+dy)
        elif t == 2:
          draw_path(sx+dx,sy+dy)
        elif t == 3:
          draw_wall(sx+dx,sy+dy)
        elif t == 4:
          draw_floor(sx+dx,sy+dy)
        elif t == 5:
          draw_water(sx+dx,sy+dy)
  draw_player(160,110)

def tile(x,y):
  return map[y-1][x-1]

def menu():
  fill_rect(0,0,320,222,white)
  draw_string("[1] Consulter vos pokemons",0,20)
  draw_string("[2] Mettre un pokemon dans la\n    reserve",0,40)
  draw_string("[3] Mettre un pokemon dans\n    l'equipe",0,80)
  draw_string("[4] Relacher un pokemon",0,120)
  
  draw_string("[OK] Fermer le menu",0,200)
  while not keydown(KEY_OK):
    if keydown(KEY_ONE):
      enum_pokemons()
      return
    elif keydown(KEY_TWO):
      while keydown(KEY_TWO):
        pass
      pokemon_to_reserve()
      return
    elif keydown(KEY_THREE):
      while keydown(KEY_THREE):
        pass
      pokemon_to_team()
      return
    elif keydown(KEY_FOUR):
      release_pokemon()
      return
  while keydown(KEY_OK):
    pass

def enum_pokemons():
  fill_rect(0,0,320,222,white)
  draw_string("Equipe:",0,0)
  y = 20
  for p in equipe:
    if p:
      draw_string(p.name + " | lvl " + str(p.lvl),0,y)
      y += 20
  
  draw_string("Reserve:",0,y + 20)
  y += 40
  for p in reserve:
    if p:
      draw_string(p.name + " | lvl " + str(p.lvl),0,y)
      y += 20
  
  draw_string("[OK] Fermer le menu",0,200)
  while not keydown(KEY_OK):
    pass
  while keydown(KEY_OK):
    pass

def release_pokemon():
  fill_rect(0,0,320,222,white)
  draw_string("Pressez le numero du pokemon a\nrelacher:",0,0)
  y = 40
  i = 1
  for p in equipe:
    if p:
      draw_string(str(i) + ". " + p.name,0,y)
      y += 20
      i += 1
  
  draw_string("Vous ne pouvez pas relacher\nvotre dernier pokemon",0,160)
  draw_string("[OK] Fermer le menu",0,200)
  while not keydown(KEY_OK):
    if keydown(KEY_ONE): # if it's the last
      if equipe[1] == None:  return
      equipe[0] = equipe[1]
      equipe[1] = equipe[2]
      equipe[2] = None
      return
    elif keydown(KEY_TWO):
      equipe[1] = equipe[2]
      equipe[2] = None
      return
    elif keydown(KEY_THREE):
      equipe[2] = None
      return
  while keydown(KEY_OK):
    pass

def pokemon_to_team():
  next_spot = 0
  while equipe[next_spot]:
    next_spot += 1
    if next_spot == 3:
      next_spot = -1
      break
  
  fill_rect(0,0,320,222,white)
  draw_string("Pressez le numero du pokemon a\nmettre dans l'equipe:",0,0)
  y = 40
  i = 1
  for p in reserve:
    if p:
      draw_string(str(i) + ". " + p.name,0,y)
      y += 20
      i += 1
  
  draw_string("[OK] Fermer le menu",0,200)
  while not keydown(KEY_OK):
    if keydown(KEY_ONE):
      if next_spot == -1:  return # no room
      equipe[next_spot] = reserve[0]
      reserve[0] = reserve[1]
      reserve[1] = reserve[2]
      reserve[2] = None
      return
    elif keydown(KEY_TWO):
      if next_spot == -1:  return # no room
      equipe[next_spot] = reserve[1]
      reserve[1] = reserve[2]
      reserve[2] = None
      return
    elif keydown(KEY_THREE):
      if next_spot == -1:  return # no room
      equipe[next_spot] = reserve[2]
      reserve[2] = None
      return
  while keydown(KEY_OK):
    pass

def pokemon_to_reserve():
  next_spot = 0
  while reserve[next_spot]:
    next_spot += 1
    if next_spot == 3:
      next_spot = -1
      break
  
  fill_rect(0,0,320,222,white)
  draw_string("Pressez le numero du pokemon a\nmettre dans la reserve:",0,0)
  y = 40
  i = 1
  for p in equipe:
    if p:
      draw_string(str(i) + ". " + p.name,0,y)
      y += 20
      i += 1
  
  draw_string("Vous ne pouvez pas y mettre\nvotre dernier pokemon",0,160)
  draw_string("[OK] Fermer le menu",0,200)
  while not keydown(KEY_OK):
    if keydown(KEY_ONE): # if it's the last
      if equipe[1] == None:  return
      if next_spot == -1:  return # no room
      reserve[next_spot] = equipe[0]
      equipe[0] = equipe[1]
      equipe[1] = equipe[2]
      equipe[2] = None
      return
    elif keydown(KEY_TWO):
      if next_spot == -1:  return # no room
      reserve[next_spot] = equipe[1]
      equipe[1] = equipe[2]
      equipe[2] = None
      return
    elif keydown(KEY_THREE):
      if next_spot == -1:  return # no room
      reserve[next_spot] = equipe[2]
      equipe[2] = None
      return
  while keydown(KEY_OK):
    pass

def game():
  global px,py
  
  render_map()
  dialog_box("Pressez [OK] pour acceder au menu")
  render_map()
  
  while True:
    
    # movement
    move_keys = [keydown(KEY_LEFT),keydown(KEY_RIGHT),keydown(KEY_UP),keydown(KEY_DOWN)]
    if move_keys[0]:
      if px == 1 or tile(px-1,py) in [1,3,5]:
        continue
      for dx in range(2,30,2):
        render_map(dx=dx)
      px -= 1
      render_map()
    elif move_keys[1]:
      if px == mapx or tile(px+1,py) in [1,3,5]:
        continue
      for dx in range(2,30,2):
        render_map(dx=-dx)
      px += 1
      render_map()
    elif move_keys[2]:
      if py == 1 or tile(px,py-1) in [1,3,5]:
        continue
      for dy in range(2,30,2):
        render_map(dy=dy)
      py -= 1
      render_map()
    elif move_keys[3]:
      if py == mapy or tile(px,py+1) in [1,3,5]:
        continue
      for dy in range(2,30,2):
        render_map(dy=-dy)
      py += 1
      render_map()
    
    # encounters
    if move_keys != [False]*4:
      if not tile(px,py) in [4,2] and randint(0,5) == 5:
        l = [p for p in pokemons.keys()]
        e = randint(0,len(pokemons)-1)
        r = max(get_poke_fam_rank(p.name) if p else 0 for p in equipe)
        while get_poke_fam_rank(l[e-1]) > r + 1:
          e = randint(0,len(pokemons)-1)
        fight(l[e-1])
        render_map()
    
    # menu
    if keydown(KEY_OK):
      while keydown(KEY_OK):
        pass
      menu()
      render_map()

title_screen()
start()
game()