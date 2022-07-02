import sys, random, pygame
from pygame.locals import *
import Animals.animal as animal
pygame.init()

WIDTH = 640 #game window width
HEIGHT = 480 #game window height
FPS = 60 #game's speeds
Pixsize = 2
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set the game window

cells = []
for i in range(20): #generate n cells
    Animal = animal.Animal(environment=screen)
    cells.append(Animal)

def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type== QUIT: #if pressing the X, quit the progra
                pygame.quit() #stop pygame
                sys.exit() #stop the program
        screen.fill((0,0,0)) #clear the screen;
        for i in cells: #update all cells
            i.walk()
            i.draw()
        pygame.display.update() #update display
        pygame.time.Clock().tick(FPS) #limit FPS

mainloop()