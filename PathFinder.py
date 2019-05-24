import pygame, random, numpy, math, time

WIDTH = 600
HEIGHT = 600
scale = 100 ## size of blocks in pixels
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLACK = (0,0,0)

goalPos = (0,0)
blocks = {}



class Block():

    def __init__(self, rect, index):

        self.index = index
        self.rect = rect
        self.type = "empty"
        self.color = BLACK
        self.searched = False
        self.parents = None
    
    def becomeSearched(self, parent):
        self.searched = True
        self.color = (100,100,100)
        self.parent = parent
        
    def setPath(self):

        self.color = GREEN
        self.type = "path"
        
    def show(self):
        pygame.draw.rect(screen, self.color, self.rect)
        for event in pygame.event.get():
            pass
        pygame.display.update(self.rect)
        
    def becomeGoal(self):
        self.type = "goal"
        self.color = GREEN

    def becomeStart(self):
        self.type = "start"
        self.color = RED

    def becomeObstacle(self):
        self.type = "obs"
        self.color = WHITE

def getAdjacent(index):
    x , y = index
    left= (x-1 , y)
    right = (x+1 , y)
    down = (x, y+1)
    up = (x, y-1)
    return([up,down,left,right])



def renderScreen():
    
    for event in pygame.event.get():
        pass
    
    pygame.display.update()

    
#searched= []
active = []
def findPath():
    

    ## keys = 1-width / scale etc whereas Value is the actual rect position
    
    for block in blocks.values():
        if block.type == "start":
            active.append(block)
            break
        elif block.type == "goal":
            goal = block

    while len(active) > 0:
        
        current_block = active.pop(0)
        
        blocksAround = getAdjacent(current_block.index)
        
        random.shuffle(blocksAround)
        for i in blocksAround:
            
            if i in blocks.keys():
                
                localBlock = blocks[i]

                if localBlock.type == "goal":

                    while current_block != None:

                        current_block.setPath()

                        current_block.show()
                        
                        current_block = current_block.parent

                        if current_block.type == "start":
                        
                            return 

                
                if localBlock.type == "empty" and not localBlock.searched:

                    localBlock.becomeSearched(current_block)
                    
                    active.append(localBlock)

                    localBlock.show()

                #renderScreen()
                
            

    


    

def initBlocks():
    
    for x in range(math.floor(WIDTH / scale)):
        for y in range(math.floor(HEIGHT / scale)):
            
            local_rect = pygame.Rect(x*scale, y*scale , scale, scale)
            blocks[(x,y)] = (Block(local_rect, (x,y)))

            
            





initBlocks()

over = False
setUp1 = False
setUp2 = False


while not setUp1:

    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    for block in blocks.values():
        if left_click and block.rect.collidepoint(mouse):
            block.becomeObstacle()
            block.show()
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setUp1 = over
            over = True
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                setUp1 = True
     
    
    pygame.display.update()


while not setUp2:

    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    for block in blocks.values():
        if left_click and block.rect.collidepoint(mouse):
            block.becomeStart()
            block.show()
            setUp2 = True
            pygame.display.update()
            time.sleep(.5)
            
            
            
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setUp2 = True
            over = True
    
      
     
    
    pygame.display.update()

setUp3 = False

while not setUp3:

    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    for block in blocks.values():
        if left_click and block.rect.collidepoint(mouse):
            block.becomeGoal()
            goalPos = block.index
            block.show()
            setUp3 = True
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setUp2 = over
            over = True
    
                
     
    
    pygame.display.update()
     

    

findPath()
    
renderScreen()



        
