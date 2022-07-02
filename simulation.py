from multiprocessing import Event
import sys, random, pygame
from pygame.locals import *
import Animals.animal as animal
import globalVars as glb

pygame.init()

WIDTH = 1000 #game window width
HEIGHT = 1000 #game window height
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set the game window

for i in range(400): #generate n cells
    Animal = animal.Animal(environment=screen, size=random.randint(2, 10), dateOfBirth=0, walkSpeed=random.randint(2, 4), runSpeed=random.randint(5, 7))
    glb.Environment.animals.append(Animal)

def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #if pressing the X, quit the program
                pygame.quit() #stop pygame
                sys.exit() #stop the program
        screen.fill((0,0,0)) #clear the screen;
        for animal in glb.Environment.animals: #update all cells
            animal.live()
            animal.draw()
            collisionIdentifier(animal)

        glb.Environment.timeStep()
           
        pygame.display.update() #update display
        pygame.time.Clock().tick(glb.FPS) #limit FPS


def collisionIdentifier(animal):
    for animal_two in glb.Environment.animals:
        if animal is not animal_two and animal.rect.colliderect(animal_two.rect):
            if animal in glb.Environment.animals:
                glb.Environment.animals.remove(animal)
            if animal_two in glb.Environment.animals:
                glb.Environment.animals.remove(animal_two)
mainloop()