import pygame,sys
from colores import *
from pygame.locals import *
from buttons import Button
from input_boxes import InputBox
from texts import Text

class Screen:
    def __init__(self,width,height,bg,title='',list_b=[],list_i=[],list_t=[],list_p=[],list_a=[]):
        pygame.init()
        self.width = width
        self.height = height
        self.bg = bg
        self.title = title
        self.list_b = list_b
        self.list_i = list_i
        self.list_t = list_t
        self.list_p = list_p
        self.list_a = list_a
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(title)
        self.screen.fill(self.bg)

    def run(self):
        while True:
            for i in self.list_i:
                i.update()
            self.screen.fill(self.bg)

            for b in self.list_b:
                b.draw(self.screen)

            for i in self.list_i:
                i.draw(self.screen)

            for t in self.list_t:
                t.draw(self.screen)

            for p in self.list_p:
                p.draw(self.screen)

            for a in self.list_a:
                a.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for i in self.list_i:
                    i.handle_event(event)
                
                for b in self.list_b:
                    b.handle_event(event)
            
            pygame.display.update()




# def asa():
#     print('asa')


# pygame.init()

# button = Button('Log In', 100, 200, 100, 50,red,bright_red,2,asa)
# a = InputBox(200,400,50,50)

# t = Text('ss',94,blue,50,10)
# l = [button]
# d=[t]
# ab = [a]


# s = Screen(500,500,silver,'s',l,ab,d)
# s.run()
        
