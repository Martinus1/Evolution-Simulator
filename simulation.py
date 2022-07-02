import sys, random, pygame
from pygame.locals import *
import Animals.animal as animal
import environment
pygame.init()

WIDTH = 640 #game window width
HEIGHT = 480 #game window height
FPS = 60 #game's speeds
Pixsize = 2
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set the game window

Environment = environment.Environment( animals=[] )

for i in range(400): #generate n cells
    Animal = animal.Animal(environment=screen)
    Environment.animals.append(Animal)

def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #if pressing the X, quit the program
                pygame.quit() #stop pygame
                sys.exit() #stop the program
        screen.fill((0,0,0)) #clear the screen;
        for animal in Environment.animals: #update all cells
            animal.live(Environment.animals)
            animal.draw()
            collisionIdentifier(animal)

            
        pygame.display.update() #update display
        pygame.time.Clock().tick(FPS) #limit FPS


def collisionIdentifier(animal):
    for animal_two in Environment.animals:
        if animal is not animal_two and animal.rect.colliderect(animal_two.rect):
            if animal in Environment.animals:
                Environment.animals.remove(animal)
            if animal_two in Environment.animals:
                Environment.animals.remove(animal_two)
mainloop()