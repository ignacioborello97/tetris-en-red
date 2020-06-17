import pygame

black = (0,0,0)

def text_objects(text,font):
        textSurface = font.render(text,1,black)
        return textSurface , textSurface.get_rect()

def button(surface,msg,x,y,w,h,ic,ac,bs,action=None):

    mx, my = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mx > x and y+h > my > y:
        pygame.draw.rect(surface, ac, (x,y,w,h))
        pygame.draw.rect(surface, black,(x,y,w,h),bs)
        if click[0] == 1 and action!= None:
            action()

    else: 
        pygame.draw.rect(surface, ic, (x,y,w,h))
        pygame.draw.rect(surface, black,(x,y,w,h),bs)

    pygame.font.init()
    buttonText = pygame.font.SysFont("comicsansms",int(w/10))
    textSurf, textRect = text_objects(msg,buttonText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    surface.blit(textSurf,textRect)
