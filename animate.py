# IMPORT MODULES AND INITIALIZE

import pygame
from pygame.locals import *
import sys
import time
import pyganim

import gamelib
import as4
import main
pygame.init()

# GET THE MAP AND BACKGROUND AND CLOCK

pygame.display.set_caption('Zombie Hunter')
background_image = pygame.image.load("scary_floor.jpeg")
map_dimensions, store_actions = main.main()
map_width = map_dimensions[0]
map_height = map_dimensions[1]
mainClock = pygame.time.Clock()

# MAX MAP SIZE IS 40 BY 20

# MAKE ANIMATION OBJECTS FOR THE ZOMBIE HUNTER & ZOMBIES

anim_type_3 = 'steve_left_heal steve_left_hit steve_right_heal steve_right_hit zom_right_heal'.split()
anim_type_4 = 'steve_left_walk steve_right_walk zom_left_walk zom_right_walk'.split()
anim_type_5 = 'steve_left_age steve_right_age steve_lost zom_right_age'.split()
anim_type_6 = 'steve_left_die steve_right_die steve_win'.split()
anim_type_7 = 'steve_left_scan steve_right_scan zom_right_scan'.split()
anim_type_8 = 'steve_left_attack steve_right_attack zom_left_attack zom_right_attack'.split()
anim_objects = {}

if map_width > 20 or map_height > 10 :

    steve_left_standing = pygame.image.load('baby_sprite/steve_left_idle.png')
    steve_right_standing = pygame.image.load('baby_sprite/steve_right_idle.png')
    zom_left_standing = pygame.image.load('baby_sprite/zom_left_idle.png')
    zom_right_standing = pygame.image.load('baby_sprite/zom_right_idle.png')
    player_width, player_height = steve_right_standing.get_size()

    for anim in anim_type_3:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(3)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

    for anim in anim_type_4:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(4)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_5:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(5)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_6:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(6)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_7:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(7)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_8:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(8)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

else :

    steve_left_standing = pygame.image.load('adult_sprite/steve_left_idle.png')
    steve_right_standing = pygame.image.load('adult_sprite/steve_right_idle.png')
    zom_left_standing = pygame.image.load('adult_sprite/zom_left_idle.png')
    zom_right_standing = pygame.image.load('adult_sprite/zom_right_idle.png')    
    player_width, player_height = steve_right_standing.get_size()

    for anim in anim_type_3:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(3)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

    for anim in anim_type_4:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(4)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_5:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(5)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_6:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(6)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_7:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(7)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_8:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), 1) for num in range(8)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
# CREATE THE WINDOW

window_width = map_width * player_width
window_height = map_height * player_height
screen = pygame.display.set_mode((window_width, window_height), 0, 32)


LEFT = 'left'
RIGHT = 'right'

direction = RIGHT
RATE = 4


simplified_actions = list()

for item in store_actions:
    if item == 'None' :
        continue
    else :
        words = item.split()
        identification = words[1]
        x_position = ''.join(i for i in words[3] if i.isdigit())
        y_position = ''.join(i for i in words[4] if i.isdigit())
        x_and_y = [x_position, y_position]
        if 'died!' in words :
            simplified_actions.append([identification, x_and_y, 'died!'])
        if 'aging' in words :
            simplified_actions.append([identification, x_and_y, 'aging'])
        if 'scanning' in words :
            simplified_actions.append([identification, x_and_y, 'scanning'])
        if 'moving' in words :
            x_new = ''.join(i for i in words[-2] if i.isdigit())
            y_new = ''.join(i for i in words[-1] if i.isdigit())
            x_and_y_new = [x_new, y_new]
            simplified_actions.append([identification, x_and_y, 'moving', x_and_y_new])
        if 'attacking' in words :
            target = ''.join(i for i in words[-1] if i.isdigit())
            simplified_actions.append([identification, x_and_y, 'attacking', target])
            # simplified_actions.append([target, x_and_y, 'attacked'])








while True:
    screen.blit(background_image, [0, 0])
    for frame in simplified_actions:
        ID = int(frame[0])
        IDPos = [0,0]
        IDPos[0] = int(frame[1][0])
        IDPos[1] = int(frame[1][1])
        event = frame[2]
        if event == 'moving':
            newPos = [0,0]
            newPos[0] = int(frame[3][0])
            newPos[1] = int(frame[3][1])
        if ID == 0:
            x , y = IDPos
            xtrue = x*player_width
            ytrue = y*player_height
            if event == 'healing':
                anim_objects['steve_right_heal'].blit(screen, (xtrue, ytrue))
            elif event == 'aging':
                anim_objects['steve_right_age'].blit(screen, (xtrue, ytrue))
            elif event == 'scanning':
                anim_objects['steve_right_scan'].blit(screen, (xtrue, ytrue))
                
            elif event == 'attacking':
                anim_objects['steve_right_attack'].blit(screen, (xtrue, ytrue))
                    
            elif event == 'moving':
                xnew , ynew = newPos
                if x > xnew:
                    anim_objects['steve_left_walk'].blit(screen, (xtrue, ytrue))
                else:
                    anim_objects['steve_right_walk'].blit(screen, (xtrue, ytrue))
            elif event == 'died':
                anim_objects['steve_right_die'].blit(screen, (xtrue, ytrue))
        else:
            x , y = IDPos
            xtrue = x*player_width
            ytrue = y*player_height
            if event == 'healing':
                anim_objects['zom_right_heal'].blit(screen, (xtrue, ytrue))
                
            elif event == 'aging':
                anim_objects['zom_right_age'].blit(screen, (xtrue, ytrue))
                
            elif event == 'scanning':
                anim_objects['zom_right_scan'].blit(screen, (xtrue, ytrue))
                
            elif event == 'attacking':
                anim_objects['zom_right_attack'].blit(screen, (xtrue, ytrue))
                    
            elif event == 'moving':
                xnew , ynew = newPos
                if x > xnew:
                    anim_objects['zom_left_walk'].blit(screen, (xtrue, ytrue))
                else:
                    anim_objects['zom_right_walk'].blit(screen, (xtrue, ytrue))
            elif event == 'died':
                anim_objects['zom_right_die'].blit(screen, (xtrue, ytrue))
    
    pygame.display.update()
    mainClock.tick(30) # FRAMES PER SECOND
