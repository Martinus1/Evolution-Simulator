
from math import log
import sys, random, pygame
import globalVars as glb

import names
import math

ACTIONS = {0:"Wandering", 1: "Running", 2: "Sleeping", 3: "Idle"}
WIDTH = 1000 #game window width
HEIGHT = 800 #game window height
#size, growthRate, walkSpeed, runSpeed, gender, age, weight, averageSize, energy, hunger, averageSurvival, activity,
class Animal:
    def __init__(self, environment, size, dateOfBirth, runSpeed, walkSpeed):
        self.environment = environment
        
        ###GENERAL
        self.name = names.get_first_name()
        self.dateOfBirth = dateOfBirth
        # 1-Male, 0-Female
        self.gender = random.randrange(0, 1)

        ###BODY
        self.size = size
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        
        ###MOVEMENT
        self.speed = walkSpeed
        self.runSpeed = runSpeed

        ###EMOTIONS
        #From 0-100
        # hapiness increases when they have offspring
        self.happiness = 0
        self.energy = 100
        self.hunger = 0

        ###INFORMATIVE
        self.action = 0
        self.timeAsleep = 0
        self.x = random.randrange(10, WIDTH-10) #x position
        self.y = random.randrange(10, HEIGHT-10) #y position
        self.move = [None, None] #realtive x and y coordinates to move to
        self.direction = None #movement direction

        self.image = pygame.Surface([WIDTH, HEIGHT])
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400)
        self.rect.y = random.randint(50, 700)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.dir = pygame.math.Vector2(1, 0).rotate(random.randrange(360))

        
    def live(self):
        if self.action == 0 or (self.energy == 100):
            self.wander()

        if self.energy <= 10:
            self.sleep()

        if self.energy == 0:
            self.death()

    def death(self):
        glb.Environment.animals.remove(self)

    def sleep(self):
        #function to add energy depending on time asleep
        #this is added every second to energy
        if self.action != 2:
            self.action = 2
            self.energy += (math.log10(math.pow(self.timeAsleep,10) + 1) / 60)
            self.timeAsleep += glb.Environment.minPerSec

    def endSleep(self):
        self.action = 1
        self.timeAsleep = 0

    def draw(self):
        self.rect = pygame.draw.rect(self.environment, self.color, (self.x,self.y,self.size,self.size),0) #draw the cell


    def wander(self):
        self.action = 0
        directions = {"S":((-1,2),(1,self.speed)),"SW":((-self.speed,-1),(1,self.speed)),"W":((-self.speed,-1),(-1,2)),"NW":((-self.speed,-1),(-self.speed,-1)),"N":((-1,2),(-self.speed,-1)),"NE":((1,self.speed),(-self.speed,-1)),"E":((1,self.speed),(-1,2)),"SE":((1,self.speed),(1,self.speed))} #((min x, max x)(min y, max y))
        directionsName = ("S","SW","W","NW","N","NE","E","SE") #possible directions
        if random.randrange(0,5) == 2: #move about once every 5 frames
            if self.direction == None: #if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                a = directionsName.index(self.direction) #get the index of direction in directions list
                b = random.randrange(a-1,a+2) #set the direction to be the same, or one next to the current direction
                if b > len(directionsName)-1: #if direction index is outside the list, move back to the start
                    b = 0
                self.direction = directionsName[b]
            smallOffset = random.random() #Random floating-point number between 0 and 1 ("Tiny number")

            self.move[0] = random.randrange(directions[self.direction][0][0],directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0],directions[self.direction][1][1]) + smallOffset
        if self.x < 5 or self.x > WIDTH - 5 or self.y < 5 or self.y > HEIGHT - 5: #if cell is near the border of the screen, change direction
            if self.x < 5:
                self.direction = "E"
            elif self.x > WIDTH - 5:
                self.direction = "W"
            elif self.y < 5:
                self.direction = "S"
            elif self.y > HEIGHT - 5:
                self.direction = "N"

                
            smallOffset = random.random() #Random floating-point number between 0 and 1 ("Tiny number")

            self.move[0] = random.randrange(directions[self.direction][0][0],directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0],directions[self.direction][1][1]) + smallOffset

            
        if self.move[0] != None: #add the relative coordinates to the cells coordinates
            self.x += self.move[0]
            self.y += self.move[1]

"""    
    def run(self):

    def attack(self):
    
    def breed(self):

    def eat(self):
"""