import pygame
import pygame.freetype
import sys
import os
from pygame.locals import *
import random

# shape parameters
size = width, height = (800, 800)
road_w = int(width/1.6)
# location parameters
right_lane = width/2 + road_w/2
left_lane = width/2 - road_w/2
# animation parameters
speed = 1.25

#score
score =0
running=True
# initiallize the app
pygame.init()
main=True
blue = (0, 0, 128)
green = (0, 255, 0)
screen = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 35)
mainBody = font.render('PRESS ENTER TO CONTINUE', True, green, blue)
mainRect = mainBody.get_rect()
mainRect.center = ((width // 2), height // 2)
boat = pygame.image.load("boat.png")
boat_loc = boat.get_rect()
boat_loc.center = width/5, height*0.8
boat2 = pygame.image.load("boat1.png")
boat2_loc = boat2.get_rect()
boat2_loc.center = width*2/5, height*0.8
boat3 = pygame.image.load("boat2.png")
boat3_loc = boat3.get_rect()
boat3_loc.center = width*3/5, height*0.8
boat4 = pygame.image.load("boat22.png")
boat4_loc = boat4.get_rect()
boat4_loc.center = width*4/5, height*0.8
boat5 = pygame.image.load("boatside.png")
boat5_loc = boat5.get_rect()
boat5_loc.center = 0, height*0.2
while main:
    screen.fill((135, 206, 235))
    boat5_loc[0] += speed
    if boat5_loc[0] > width:
        boat5_loc.center = -200, height*0.2

    for event in pygame.event.get():
        if event.type == QUIT:
            main=False
            running=False
        if event.type == KEYDOWN:
            print(event.key)
            # move user car to the left
            if event.key in [K_RETURN]:
                main=False
                running=True
            else:
                main=True
    screen.blit(mainBody,mainRect)
    screen.blit(boat, boat_loc)
    screen.blit(boat2, boat2_loc)
    screen.blit(boat3, boat3_loc)
    screen.blit(boat4, boat4_loc)
    screen.blit(boat5, boat5_loc)
    pygame.display.update()
pygame.quit()

    
pygame.init()
#text rendering
blue = (0, 0, 128)
green = (0, 255, 0)
# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("car game")
#score text stuff
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('SCORE : '+str(score), True, green, blue)
textRect = text.get_rect()
textRect.center = ((width // 12), height // 12)
# set background colour
screen.fill((60, 220, 0))
# apply changes
pygame.display.update()

# load player vehicle
boat = pygame.image.load("boat.png")
#resize image
#car = pygame.transform.scale(car, (250, 250))
boat_loc = boat.get_rect()
boat_loc.center = right_lane, height*0.8
#print(car_loc.center[1])
# load enemy vehicle
boat2 = pygame.image.load("boat2.png")
boat2_loc = boat2.get_rect()
boat2_loc.center = left_lane, height*0.2

#trees and trunks
tree = pygame.image.load("tree.png")
tree_loc = tree.get_rect()
tree_loc.center = (width*3/4)+(width//6), height/4
tree_loc2 = tree.get_rect()
tree_loc2.center = (width*3/4)+(width//6), height*3/4
tree_loc3 = tree.get_rect()
tree_loc3.center = (width*1/4)-(width//7), height*4//5
trunk = pygame.image.load("trunk.png")
trunk_loc = tree.get_rect()
trunk_loc.center = (width*1/4)-(width//6), height//3
trunk_loc3 = trunk.get_rect()
trunk_loc3.center = (width*3/4)+(width//7), height/2

#color switch car
boat3=pygame.image.load("boat22.png")
boat4=pygame.image.load("boat1.png")
counter = 0
# game loop
while running:
    counter += 1

    # increase game difficulty overtime
    if counter%2500 == 0:
        speed += 0.25
        print("level up", speed)
    if counter%250==0:
        score+=1
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('SCORE : '+str(score), True, green, blue)
    # animate enemy vehicle
    boat2_loc[1] += speed
    tree_loc[1]+=speed
    tree_loc2[1]+=speed
    tree_loc3[1]+=speed
    trunk_loc3[1]+=speed
    trunk_loc[1]+=speed
    if boat2_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            boat2_loc.center = right_lane, 0
        else:
            boat2_loc.center = left_lane, 0
    if tree_loc[1]>height:
        tree_loc.center = (width*3/4)+(width//6), 0
    if tree_loc2[1]>height:
        tree_loc2.center = (width*3/4)+(width//6), 0
    if tree_loc3[1]>height:
        tree_loc3.center = (width*1/4)-(width//7), 0
    if trunk_loc[1]>(height+25):
        trunk_loc.center = (width*1/4)-(width//6), 0
    if trunk_loc3[1]>(height+25):
        trunk_loc3.center = (width*3/4)+(width//7), 0
        
    # end game logic
    if boat_loc[0] == boat2_loc[0] and boat2_loc[1] > boat_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        endgame=True
        while endgame:
            font = pygame.font.Font('freesansbold.ttf', 26)
            endBody = font.render('GAME OVER!! PRESS ENTER TO EXIT', True, green, blue)
            endRect = endBody.get_rect()
            endRect.center = ((width // 2), height // 8)
            for event in pygame.event.get():
                if event.type == QUIT:
                    endgame=False
                    running=False
                    break
                    
                if event.type == KEYDOWN:
                    print(event.key)
                    if event.key in [K_RETURN]:
                        running=False
                        endgame=False
                screen.fill((60, 220, 0))
                pygame.draw.rect(
                    screen,
                    (   	135, 206, 235),
                    (width/2-road_w/2, 0, road_w, height))
            if score%100<51:
                screen.blit(boat, boat_loc)
                screen.blit(boat2, boat2_loc)
            else:
                screen.blit(boat3, boat_loc)
                screen.blit(boat4, boat2_loc)
            screen.blit(text, textRect)
            screen.blit(tree, tree_loc)
            screen.blit(trunk, trunk_loc)
            screen.blit(trunk, trunk_loc3)
            screen.blit(tree, tree_loc2)
            screen.blit(tree, tree_loc3)
            screen.blit(endBody, endRect)
            pygame.display.update()   
        if running == False:
            break    
        

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False
        if event.type == KEYDOWN:
            # move user boat to the left
            if event.key in [K_a, K_LEFT] and boat_loc.center[0] != left_lane:
                   boat_loc = boat_loc.move([-int(road_w/2), 0])
            # move user boat to the right
            if event.key in [K_d, K_RIGHT] and boat_loc.center[0] != right_lane:
                boat_loc = boat_loc.move([int(road_w/2), 0])
    
    # draw road
    screen.fill((60, 220, 0))
    pygame.draw.rect(
        screen,
        (	135, 206, 235),
        (width/2-road_w/2, 0, road_w, height))
    
    # place images on the screen
    
    if score%100<51:
        screen.blit(boat, boat_loc)
        screen.blit(boat2, boat2_loc)
    else:
        screen.blit(boat3, boat_loc)
        screen.blit(boat4, boat2_loc)
    screen.blit(text, textRect)
    screen.blit(tree, tree_loc)
    screen.blit(trunk, trunk_loc)
    screen.blit(trunk, trunk_loc3)
    screen.blit(tree, tree_loc2)
    screen.blit(tree, tree_loc3)
    
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()
