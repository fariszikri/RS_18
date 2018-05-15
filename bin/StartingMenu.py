import pygame
from pygame.locals import *
import os
from .Events import *

WIDTH = 1280
HEIGHT = 720
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 255)
YELLOW = (250, 250, 0)

fontName = ''
fontSize = 30

imgFolder = os.path.join("asset")

class StartButton(pygame.sprite.Sprite):
    def __init__(self, group=None, windowGroup=None):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.image.load(os.path.join(imgFolder, "Button.png")).convert()
        self.rect = self.image.get_rect()
        self.rect = (500,390,100,50)




        self.text = "START"
        self.font = pygame.font.SysFont(fontName, fontSize)
        self.textSurface = self.font.render(self.text, False, (0, 0, 0))

        self.image.blit(self.textSurface, (100, 23))

        # This attribute is needed to pass the value to windowGroup
        self.windowGroup = windowGroup

    def Clicked(self):
        self.windowGroup.empty()
        StartButton(self.windowGroup)  # The value passed here, the FinanceWindow will instantiate under windowGroup.


class LoadButton(pygame.sprite.Sprite):
    def __init__(self, group=None, windowGroup=None):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.image.load(os.path.join(imgFolder, "Button.png")).convert()
        self.rect = self.image.get_rect()
        self.rect = (500,470,100,50)




        self.text = "LOAD"
        self.font = pygame.font.SysFont(fontName, fontSize)
        self.textSurface = self.font.render(self.text, False, (0, 0, 0))

        self.image.blit(self.textSurface, (100, 23))

        # This attribute is needed to pass the value to windowGroup
        self.windowGroup = windowGroup

    def Clicked(self):
        self.windowGroup.empty()
        LoadButton(self.windowGroup)  # The value passed here, the FinanceWindow will instantiate under windowGroup.

class QuitButton(pygame.sprite.Sprite):
        def __init__(self, group=None, windowGroup=None):
            pygame.sprite.Sprite.__init__(self, group)
            self.image = pygame.image.load(os.path.join(imgFolder, "Button.png")).convert()
            self.rect = self.image.get_rect()
            self.rect = (500, 550, 100, 50)

            self.text = "QUIT"
            self.font = pygame.font.SysFont(fontName, fontSize)
            self.textSurface = self.font.render(self.text, False, (0, 0, 0))

            self.image.blit(self.textSurface, (100, 23))

            # This attribute is needed to pass the value to windowGroup
            self.windowGroup = windowGroup

        def Clicked(self):
            self.windowGroup.empty()
            QuitButton(self.windowGroup)  # The value passed here, the FinanceWindow will instantiate under windowGroup.


#class LogoTitle(pygame.sprite.Sprite):
#    def __init__(self, group=None, windowGroup=None):
 #       pygame.sprite.Sprite.__init__(self, group)
  #      self.image = pygame.image.load(os.path.join(imgFolder, "RT.png")).convert()
   #     self.rect = self.image.get_rect()
    #    self.rect = (500, 0, 100, 50)

     #   self.text = ""
      #  self.font = pygame.font.SysFont(fontName, fontSize)
       # self.textSurface = self.font.render(self.text, False, (0, 0, 0))

        #self.image.blit(self.textSurface, (100, 23))

        # This attribute is needed to pass the value to windowGroup
        #self.windowGroup = windowGroup


class View:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Restaurant Simulator")

        #Sprite Layers and Groups
        self.mainUI = pygame.sprite.LayeredUpdates()
        self.clickUI = pygame.sprite.Group()
        self.windows = pygame.sprite.Group()

        #All sprite start from here.
        #Sprite will carry it group from here.
        self.startButton = StartButton(self.mainUI)
        self.loadButton = LoadButton(self.mainUI)
        self.quitButton = QuitButton(self.mainUI)
        #self.logoTitle = LogoTitle(self.mainUI)



    def Notify(self, event):
        if isinstance(event, TickEvent):
            self.mainUI.update()
            self.windows.update()

            self.screen.fill(WHITE)
            self.mainUI.draw(self.screen)
            self.clickUI.draw(self.screen)
            self.windows.draw(self.screen)

            pygame.display.flip()

        elif isinstance(event, LeftClickEvent):
            for sprite in self.clickUI:
                if sprite.rect.collidepoint(event.pos):
                    sprite.Clicked()
            for sprite in self.windows:
                if sprite.rect.collidepoint(event.pos):
                    sprite.Clicked()

