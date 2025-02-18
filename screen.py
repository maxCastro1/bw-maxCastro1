# import the pygame module, so you can use it
import pygame
 
class Display():
    def __init__(self):
     
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Blocks World")
     
        # create a surface on screen that has the given size
     
        # define a variable to control the main loop
        self.running = True

        IMAGE_SIZE_X = 100
        IMAGE_SIZE_Y = 100
        DEFAULT_IMAGE_SIZE = (IMAGE_SIZE_X, IMAGE_SIZE_Y)
        self.screen = pygame.display.set_mode((4*IMAGE_SIZE_X,6*IMAGE_SIZE_Y))

        self.positions = {1:0,2:IMAGE_SIZE_X,3:2*IMAGE_SIZE_X,4:3*IMAGE_SIZE_X}
        self.heights = {1:2*IMAGE_SIZE_Y,
                        2:IMAGE_SIZE_Y,
                        3:0,
                        4:5*IMAGE_SIZE_Y,
                        5:4*IMAGE_SIZE_Y,
                        6:3*IMAGE_SIZE_Y}
        self.line_begin = (0,3*IMAGE_SIZE_Y)
        self.line_end = (4*IMAGE_SIZE_X,3*IMAGE_SIZE_Y)

        self.a = pygame.image.load("A.png")    
        self.b = pygame.image.load("B.png")    
        self.c = pygame.image.load("C.png")    

        self.a = pygame.transform.scale(self.a, DEFAULT_IMAGE_SIZE)
        self.b = pygame.transform.scale(self.b, DEFAULT_IMAGE_SIZE)
        self.c = pygame.transform.scale(self.c, DEFAULT_IMAGE_SIZE)
        self.initial = ""
        self.target = ""

    def start(self):
        # main loop
        while self.running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    self.running = False

    def step(self,state):
        a_x,a_y,b_x,b_y,c_x,c_y = self.draw(state)
        self.screen.fill((255,255,255))
        self.screen.blit(self.a, (self.positions[a_x],self.heights[a_y]))
        self.screen.blit(self.b, (self.positions[b_x],self.heights[b_y]))
        self.screen.blit(self.c, (self.positions[c_x],self.heights[c_y]))
        
        pygame.draw.line(self.screen,(0,0,0),self.line_begin,self.line_end)

        a_x,a_y,b_x,b_y,c_x,c_y = self.draw(self.target)
        a_y+=3
        b_y+=3
        c_y+=3
        self.screen.blit(self.a, (self.positions[a_x],self.heights[a_y]))
        self.screen.blit(self.b, (self.positions[b_x],self.heights[b_y]))
        self.screen.blit(self.c, (self.positions[c_x],self.heights[c_y]))

        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.running = False

    def initial(self,state):
        a_x,a_y,b_x,b_y,c_x,c_y = self.draw(state)
        a_y+=3
        b_y+=3
        c_y+=3
        self.screen.fill((255,255,255))
        self.screen.blit(self.a, (self.positions[a_x],self.heights[a_y]))
        self.screen.blit(self.b, (self.positions[b_x],self.heights[b_y]))
        self.screen.blit(self.c, (self.positions[c_x],self.heights[c_y]))
        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.running = False
        

    def draw(self,state):
        a_pos = state[0]
        b_pos = state[1]
        c_pos = state[2]
        
        a_x,a_y,b_x,b_y,c_x,c_y = 0,0,0,0,0,0
        if a_pos in ['1','2','3','4']:
          a_y = 1
          a_x = int(a_pos)
        if b_pos in ['1','2','3','4']:
          b_y = 1
          b_x = int(b_pos)
        if c_pos in ['1','2','3','4']:
          c_y = 1
          c_x = int(c_pos)

        for i in [0,1]:
           if a_x == 0:
              if a_pos == 'b':
                 if b_x != 0:
                    a_x = b_x
                    a_y = b_y +1
              elif a_pos == 'c':
                 if c_x != 0:
                    a_x = c_x
                    a_y = c_y +1
           if b_x == 0:
              if b_pos == 'a':
                 if a_x != 0:
                    b_x = a_x
                    b_y = a_y +1
              elif b_pos == 'c':
                 if c_x != 0:
                    b_x = c_x
                    b_y = c_y +1
           if c_x == 0:
              if c_pos == 'a':
                 if a_x != 0:
                    c_x = a_x
                    c_y = a_y +1
              elif c_pos == 'b':
                 if b_x != 0:
                    c_x = b_x
                    c_y = b_y +1

        return a_x,a_y,b_x,b_y,c_x,c_y
 
def main():
   display = Display()
   display.start()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
