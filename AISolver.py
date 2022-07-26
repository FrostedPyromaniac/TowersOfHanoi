from processing import *
#Global variables that represent clicking location
xmouse = 0
ymouse = 0
#Number of starting disks
numDisks = 8
#Number of starting towers
numTowers = 3
moves = []
index = 0
count = 0
def setup():
  size(600,600)
  
#Disc class stores size and location
class Disc:
  def __init__ (self,size,x,y):
    self.size = size
    self.x = x
    self.y = y
  #Disc display
  def display(self):
    fill(129,210,190)
    rect(self.x,self.y,self.size,10)
  #Gets size of disc
  def getSize(self):
    return self.size
  #Updates coordinates
  def set_pos(self,x,y):
    self.x=x
    self.y=y
      
  #Tower is responsible for adding disks to certain towers, removing disks, and checking if moves are valid 
class Tower:
  def __init__(self,x,y):
    self.disc_arr = []
    self.x=x
    self.y=y
    
  #Checks if disk move is valid
  def is_valid(self):
    for i in range (0,len(self.disc_arr)-1):
      if i == len(self.disc_arr)-1:
        return True
      if self.disc_arr[i].getSize()<self.disc_arr[i+1].getSize():
        return False
      else:
        return True
  #Displays towers 
  def display(self):
    rect (self.x,self.y,30,200)
    fill(0,255,0)
    
    #Displaying the disks on the Tower
    for i in range(0,len(self.disc_arr)):
      self.disc_arr[i].set_pos(self.x+15-self.disc_arr[i].getSize()/2,self.y+(200-(10*i)))
      self.disc_arr[i].display()
    
  #Add disk to certain tower
  def add_disk (self, d):
    self.disc_arr.append(d) 
    if self.is_valid() == False:
      return self.remove_disc()
    else:
      return None
    
  #Remove disk from certain tower
  def remove_disc (self):
    top_disk= self.disc_arr[len(self.disc_arr)-1]
    disc = self.disc_arr.remove(self.disc_arr[len(self.disc_arr)-1])
    return top_disk
  #Gets coords of tower
  def get_coords(self):
    return (self.x, self.y)
  
#Game engine class is responsible for handling clicks,moving disks
class gameEngine:
  def __init__(self):
    self.tow_arr = [Tower(70,100),Tower(210,100),Tower(350,100)]
    self.is_selected = False
    self.selected = 0
    for i in range(0,numDisks):
      #print "Adding Disk#: "+ str(i)
      self.tow_arr[0].add_disk(Disc((100-(10*i)),1,1))
      #self.tow_arr[0].show_disks()
  #Every time there is a click this function is run and it checks if a tower was clicked on
  def clicked(self,x,y):
    global xmouse, ymouse
    count = 0
    for i in range(0,len(self.tow_arr)):
      x1, y1 = self.tow_arr[i].get_coords()
      if x > x1 and x < x1+30 and y > y1 and y < y1+200:
        self.is_selected = not self.is_selected
        self.selected = i+1
        count = i+1
    if count != self.selected:
      self.is_selected = False
    return self.selected
  
    
   #Responsible for moving disks, removes original disk and adds that disk to the new tower 
  def move(self,tow1,tow2):
    #print "Move" + str(tow1) +" to " +str(tow2)
    top_disk = self.tow_arr[tow1-1].remove_disc()
    #print "Top Disk Size "+ str(top_disk.getSize())
    if self.tow_arr[tow2-1].add_disk(top_disk) != None:
      self.tow_arr[tow1-1].add_disk(top_disk)
  #Calls tower display and has the color change when a tower has been clicked on
  def display(self):
    global xmouse,ymouse
    for i in range(0,len(self.tow_arr)):
      fill(255,0,0)
      if self.is_selected == True:
        if self.selected == 1 and i == 0:
          fill(20,200,150)
        if self.selected == 2 and i == 1:
          fill(20,200,150)
        if self.selected == 3 and i == 2:
          fill(20,200,150)
      self.tow_arr[i].display()

towerNumber = -1
def AI(n , start, end, unused): 
    global moves
    if n == 1: 
      moves.append((start,end))
      return
    AI(n-1, start, unused, end) 
    moves.append((start,end))
    AI(n-1, unused, end, start)
    
  
g = gameEngine()
#Everytime mouse is clicked calls clicked function and sorts out the number click we are on
#The second tower click does not need to change
def mouseClicked():
  global count, moves, index
  count += 1
  if count == 1:
    AI(numDisks,1,3,2)
  else:
    if index < len(moves):
      t1,t2 = moves[index]
      g.move(t1,t2)
      index += 1


def draw():
  background(100,100,100)
  g.display()
  
  

  
run()


