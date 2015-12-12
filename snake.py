import pygame
from pygame.locals import *
while True:
    restart = True
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PAPAYAWHIP = (255,150,233)
    MAHOBURGUNDY = (219, 19, 19)

    segment_width = 15
    segment_height = 15
    segment_margin = 2

    x_change = segment_width + segment_margin
    y_change = 0

    width = 682
    height = 699
    size = [width, height]
    pygame.init()
    screen = pygame.display.set_mode(size)
    background = pygame.Surface(screen.get_size())
    class Dot():
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def gex(self):
            return self.x
        def gey(self):
            return self.y
        def sex(self, x):
            self.x = x
        def sey(self, y):
            self.y = y
    def dropBox(cp, color):
        actualX = segment_margin + cp.gex() * (segment_margin + segment_width)
        actualY = segment_margin + cp.gey() * (segment_margin + segment_width)
        pygame.draw.rect(screen, color, Rect((actualX, actualY),(segment_width,segment_width)))
        pygame.display.update()
    allspriteslist = pygame.sprite.Group()

    dots = []
    dots.append(Dot(15, 15))
    left = False
    right = False
    up = False
    down = False
    vel = Dot(0,0)
    myfont = pygame.font.SysFont("monospace", 15)
    import random
    def otherYummy(test):
        if test.gex() > 39 or test.gex() < 0 or test.gey() > 39 or test.gey() < 0:
            return False
        return True
    def yummy(test):
        for x in range(0, len(dots) - 1):
            #print str(dots[x].gex()) + " " + str(dots[x].gey()) + " " + str(test.gex()) + " " + str(test.gey())
            if (dots[x].gex() == test.gex() and dots[x].gey() == test.gey()):
                return False
        return True
    def bait():
        ret = Dot(random.randint(0, 39), random.randint(0, 39))
        while (not yummy(ret)):
            ret = Dot(random.randint(0, 39), random.randint(0, 39))
        return ret
    def lose():
        pygame.event.get()
        keys=pygame.key.get_pressed()
        while not keys[K_RETURN]:
            pygame.event.get()
            keys=pygame.key.get_pressed()
            myfont = pygame.font.SysFont("monospace", 50)
            label = myfont.render('you lose', 1, MAHOBURGUNDY)
            screen.blit(label, (200, 300))
            againFont = pygame.font.SysFont("monospace", 25)
            label = againFont.render('press enter to play again', 1, MAHOBURGUNDY)
            screen.blit(label, (130, 360))
            pygame.display.update()
    food = bait()
    dropBox(food, PAPAYAWHIP)
    import time
    counter = 0
    temp = Dot(0,0)
    while restart:
        ct = time.time()
        while (time.time() - ct < 0.07):
            pygame.event.get()
            keys=pygame.key.get_pressed()
            if keys[K_LEFT] and not vel.gex() == 1:
                temp.sex(-1)
                temp.sey(0)
            if keys[K_RIGHT] and not vel.gex() == -1:
                temp.sex(1)
                temp.sey(0)
                right = True
            if keys[K_UP] and not vel.gey() == 1:
                temp.sey(-1)
                temp.sex(0)
                up = True
            if keys[K_DOWN] and not vel.gey() == -1:
                temp.sey(1)
                temp.sex(0)
                down = True
        vel.sex(temp.gex())
        vel.sey(temp.gey())    
                #Dot(dots.append(Dot(dots[len(dots)-1].gex() + vel.gex(), dots[len(dots)-1].gey() + vel.gey())))
        square = Dot(dots[len(dots)-1].gex() + vel.gex(), dots[len(dots)-1].gey() + vel.gey())
        if not (vel.gex() == 0 and vel.gey() == 0):
            if not yummy(square):
                dropBox(square, MAHOBURGUNDY)
                lose()
                restart = False
            if not otherYummy(square):
                dropBox(dots[len(dots)-1], MAHOBURGUNDY)
                lose()
                restart = False
        dots.append(Dot(dots[len(dots)-1].gex() + vel.gex(), dots[len(dots)-1].gey() + vel.gey()))
        dropBox(dots[len(dots)-1], WHITE)
        if counter == 0:
            dropBox(dots[0], BLACK)
            del dots[0]
        else:
            counter -= 1
        if dots[len(dots)-1].gex() == food.gex() and dots[len(dots)-1].gey() == food.gey():
            food = bait()
            dropBox(food, PAPAYAWHIP)
            counter = 5
        pygame.draw.rect(screen, WHITE, Rect((0, 682),(682,17)))
        label = myfont.render('scorePlayer = ' + str(len(dots)), 1, BLACK)
        screen.blit(label, (0, 682))


