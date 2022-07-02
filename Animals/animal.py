from ast import walk
import sys, random, pygame
from time import sleep

WIDTH = 640 #game window width
HEIGHT = 480 #game window height
FPS = 60 #game's speeds
Pixsize = 2
#size, growthRate, walkSpeed, runSpeed, gender, age, weight, averageSize, energy, hunger, averageSurvival, activity,
class Animal:
    def __init__(self, environment):
        self.environment = environment
        """""
        #body
        self.averageSize = averageSize
        self.weight = weight
        self.growthRate = growthRate
        self.gender = gender
        self.color = (255, 255, 255)
        #movement
        self.walkSpeed = walkSpeed
        self.runSpeed = walkSpeed
        self.age = age
        
        #limiting factors
        self.averageSurvival = averageSurvival
        #functions
        self.size = size
        self.energy = energy
        self.activity = activity
        self.hunger = hunger
        """
        #other
        self.x = random.randrange(10, WIDTH-10) #x position
        self.y = random.randrange(10, HEIGHT-10) #y position
        self.speed = random.randrange(2,5) #cell speed
        self.move = [None, None] #realtive x and y coordinates to move to
        self.direction = None #movement direction
        
        self.image = pygame.Surface([WIDTH, HEIGHT])

        self.radius = WIDTH // 2  # 25
        center = [WIDTH // 2, HEIGHT // 2]
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400)
        self.rect.y = random.randint(50, 700)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.dir = pygame.math.Vector2(1, 0).rotate(random.randrange(360))
        
    def live(self, animals):
        self.walk()

    def die(self):
        print("Death")

    def draw(self):
        self.rect = pygame.draw.rect(self.environment, (255,255,255), (self.x,self.y,Pixsize,Pixsize),0) #draw the cell


    def walk(self):
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

    def sleep(self):

    def eat(self):
"""