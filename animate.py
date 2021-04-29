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
anim_type_1 = 'zom_right_idle steve_right_idle'.split()
anim_type_3 = 'steve_left_heal steve_left_hit steve_right_heal steve_right_hit zom_right_heal'.split()
anim_type_4 = 'steve_left_walk steve_right_walk zom_left_walk zom_right_walk'.split()
anim_type_5 = 'steve_left_age steve_right_age steve_lost zom_right_age'.split()
anim_type_6 = 'steve_left_die steve_right_die steve_win zom_right_die'.split()
anim_type_7 = 'steve_left_scan steve_right_scan zom_right_scan'.split()
anim_type_8 = 'steve_left_attack steve_right_attack zom_left_attack zom_right_attack'.split()
anim_objects = {}
anim_rate = 500

if map_width > 20 or map_height > 10 :

    steve_left_standing = pygame.image.load('baby_sprite/steve_left_idle_0.png')
    steve_right_standing = pygame.image.load('baby_sprite/steve_right_idle_0.png')
    zom_left_standing = pygame.image.load('baby_sprite/zom_left_idle_0.png')
    zom_right_standing = pygame.image.load('baby_sprite/zom_right_idle_0.png')
    player_width, player_height = steve_right_standing.get_size()

    for anim in anim_type_1:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(1)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_3:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(3)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

    for anim in anim_type_4:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(4)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_5:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(5)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_6:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(6)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_7:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(7)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_8:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(8)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

else :

    steve_left_standing = pygame.image.load('adult_sprite/steve_left_idle_0.png')
    steve_right_standing = pygame.image.load('adult_sprite/steve_right_idle_0.png')
    zom_left_standing = pygame.image.load('adult_sprite/zom_left_idle_0.png')
    zom_right_standing = pygame.image.load('adult_sprite/zom_right_idle_0.png')
    player_width, player_height = steve_right_standing.get_size()

    for anim in anim_type_1:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(1)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_3:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(3)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

    for anim in anim_type_4:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(4)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_5:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(5)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_6:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(6)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_7:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(7)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_8:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(8)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
# CREATE THE WINDOW

window_width = map_width * player_width
window_height = map_height * player_height
screen = pygame.display.set_mode((window_width, window_height), 0, 32)

default_rect = steve_right_standing.get_rect()
transparent = (0, 0, 0, 0)


LEFT = 'left'
RIGHT = 'right'

direction = RIGHT
rate = 500

simplified_actions = list()
starting_position = dict()

for item in store_actions:
    if item == 'None' :
        continue
    else :
        words = item.split()
        identification = int(words[1])
        x_position = int(''.join(i for i in words[3] if i.isdigit()))
        y_position = int(''.join(i for i in words[4] if i.isdigit()))
        x_and_y = [x_position, y_position]
        if identification not in starting_position.keys() :
            starting_position[identification] = x_and_y
        if 'died!' in words :
            simplified_actions.append([identification, x_and_y, 'died!'])
        if 'aging' in words :
            simplified_actions.append([identification, x_and_y, 'aging'])
        if 'scanning' in words :
            simplified_actions.append([identification, x_and_y, 'scanning'])
        if 'moving' in words :
            x_new = int(''.join(i for i in words[-2] if i.isdigit()))
            y_new = int(''.join(i for i in words[-1] if i.isdigit()))
            x_and_y_new = [x_new, y_new]
            simplified_actions.append([identification, x_and_y, 'moving', x_and_y_new])
        if 'attacking' in words :
            target = int(''.join(i for i in words[-1] if i.isdigit()))
            simplified_actions.append([identification, x_and_y, 'attacking', target])
            # simplified_actions.append([target, x_and_y, 'attacked'])
    
counter = -1

animation = {}

while True:
    screen.blit(background_image, [0, 0])
    for item in starting_position:
        starting_x = starting_position[item][0] * player_width
        starting_y = starting_position[item][1] * player_height
        if item == 0 :
            # image = steve_right_standing
            animation[item] = anim_objects['steve_right_idle']
        else :
            # image = zom_right_standing
            animation[item] = anim_objects['zom_right_idle']
            
        # screen.blit(image, (starting_x, starting_y))
        animation[item].blit(screen, (starting_x, starting_y))
        animation[item].play()
        time.sleep(0.1)
        animation[item].stop()
    if counter >= 0 and counter < len(simplified_actions):
        frame = simplified_actions[counter]
        ID = frame[0]
        IDPos = [0,0]
        IDPos[0] = frame[1][0]
        IDPos[1] = frame[1][1]
        action = frame[2]
        if action == 'moving':
            newPos = [0,0]
            newPos[0] = frame[3][0]
            newPos[1] = frame[3][1]
        if ID == 0:
            x0 , y0 = IDPos
            xtrue = x0*player_width
            ytrue = y0*player_height
            image = steve_right_standing
            if action == 'healing':
                animation[ID] = anim_objects['steve_right_heal']
            elif action == 'aging':
                animation[ID] = anim_objects['steve_right_age']
            elif action == 'scanning':
                animation[ID] = anim_objects['steve_right_scan']  
            elif action == 'attacking':
                animation[ID] = anim_objects['steve_right_attack']
            elif action == 'moving':
                xnew , ynew = newPos
                xnew = xnew * player_width
                ynew = ynew * player_height
                if x0 > xnew:
                    animation[ID] = anim_objects['steve_left_walk']
                else:
                    animation[ID] = anim_objects['steve_right_walk']
            elif action == 'died!':
                animation[ID] = anim_objects['steve_right_die']
        else:
            x1 , y1 = IDPos
            xtrue = x1*player_width
            ytrue = y1*player_height
            image = zom_right_standing
            if action == 'healing':
                animation[ID] = anim_objects['zom_right_heal']
            elif action == 'aging':
                animation[ID] = anim_objects['zom_right_age']
            elif action == 'scanning':
                animation[ID] = anim_objects['zom_right_scan']
            elif action == 'attacking':
                animation[ID] = anim_objects['zom_right_attack']
            elif action == 'moving':
                xnew , ynew = newPos
                xnew = xnew * player_width
                ynew = ynew * player_height
                if x1 > xnew:
                    animation[ID] = anim_objects['zom_left_walk']
                else:
                    animation[ID] = anim_objects['zom_right_walk']
            elif action == 'died!':
                animation = anim_objects['zom_right_die']  
        
        # screen.blit(background_image, (xtrue, ytrue), pygame.Rect(xtrue, ytrue, player_width, player_height))
        animation[ID].blit(screen, (xtrue, ytrue))
        animation[ID].play()
        time.sleep(0.1)
        animation[ID].stop()
        
        if ID == 0 and action == 'moving':
            # image = steve_right_standing
            # screen.blit(image, (xnew, ynew))
            animation[ID] = anim_objects['steve_right_idle']
            starting_position[item][0] = xnew
            starting_position[item][1] = ynew
            
        elif ID == 0:
            # image = steve_right_standing
            # screen.blit(image, (xtrue, ytrue))
            animation[ID] = anim_objects['steve_right_idle']
            starting_position[item][0] = xtrue
            starting_position[item][1] = ytrue
        elif action == 'moving':
            # image = zom_right_standing
            # screen.blit(image, (xnew, ynew))
            animation[ID] = anim_objects['zom_right_idle']
            starting_position[item][0] = xnew
            starting_position[item][1] = ynew
        else :
            # image = zom_right_standing
            # screen.blit(image, (xtrue, ytrue))
            animation[ID] = anim_objects['zom_right_idle']
            starting_position[item][0] = xtrue
            starting_position[item][1] = ytrue
            
        animation[ID].blit(screen, (xtrue, ytrue))
        animation[ID].play()
        time.sleep(0.1)
        
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_z:
            counter += 1

         
            
            
            
    pygame.display.update()
    mainClock.tick(30) # FRAMES PER SECOND
    
    # IMPORT MODULES AND INITIALIZE


import pygame
from pygame.locals import *
import sys
import time
import pyganim
import copy
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
anim_rate = 200

if map_width > 20 or map_height > 10 :

    steve_left_standing = pygame.image.load('baby_sprite/steve_left_idle.png')
    steve_right_standing = pygame.image.load('baby_sprite/steve_right_idle.png')
    zom_left_standing = pygame.image.load('baby_sprite/zom_left_idle.png')
    zom_right_standing = pygame.image.load('baby_sprite/zom_right_idle.png')
    player_width, player_height = steve_right_standing.get_size()

    for anim in anim_type_3:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(3)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

    for anim in anim_type_4:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(4)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_5:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(5)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_6:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(6)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_7:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(7)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_8:
        images_durations = [('baby_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(8)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

else :

    steve_left_standing = pygame.image.load('adult_sprite/steve_left_idle.png')
    steve_right_standing = pygame.image.load('adult_sprite/steve_right_idle.png')
    zom_left_standing = pygame.image.load('adult_sprite/zom_left_idle.png')
    zom_right_standing = pygame.image.load('adult_sprite/zom_right_idle.png')
    player_width, player_height = steve_right_standing.get_size()

    for anim in anim_type_3:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(3)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)

    for anim in anim_type_4:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(4)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_5:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(5)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_6:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(6)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_7:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(7)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
    for anim in anim_type_8:
        images_durations = [('adult_sprite/%s_%s.png' % (anim, str(num)), anim_rate) for num in range(8)]
        anim_objects[anim] = pyganim.PygAnimation(images_durations)
        
# CREATE THE WINDOW

window_width = map_width * player_width
window_height = map_height * player_height
screen = pygame.display.set_mode((window_width, window_height), 0, 32)



simplified_actions = list()
update_actions = list()
starting_position = dict()

for item in store_actions:
    if item == 'None' :
        continue
    else :
        words = item.split()
        identification = int(words[1])
        x_position = int(''.join(i for i in words[3] if i.isdigit()))
        y_position = int(''.join(i for i in words[4] if i.isdigit()))
        x_and_y = [x_position, y_position]
        if identification not in starting_position.keys() :
            starting_position[identification] = x_and_y
        if 'died!' in words :
            simplified_actions.append([identification, x_and_y, 'died!'])
        if 'aging' in words :
            simplified_actions.append([identification, x_and_y, 'aging'])
        if 'scanning' in words :
            simplified_actions.append([identification, x_and_y, 'scanning'])
        if 'moving' in words :
            x_new = int(''.join(i for i in words[-2] if i.isdigit()))
            y_new = int(''.join(i for i in words[-1] if i.isdigit()))
            x_and_y_new = [x_new, y_new]
            simplified_actions.append([identification, x_and_y, 'moving', x_and_y_new])
        if 'attacking' in words :
            target = int(''.join(i for i in words[-1] if i.isdigit()))
            simplified_actions.append([identification, x_and_y, 'attacking', target])
            # simplified_actions.append([target, x_and_y, 'attacked'])
    


number_players = len(starting_position)
number_turns = number_players * 2 - 1
# HUNTER DOES ONLY ONE THING PER TURN

tart = 0
for action in simplified_actions :
    if tart == 0 :
        update_actions.append(action)
    elif tart % number_turns == 0 :
        update_actions.append('update')
        update_actions.append(action)
    else :
        update_actions.append(action)
    tart += 1



counter = -1

while True:
    screen.blit(background_image, [0, 0])

    if counter == -1 :
        for item in starting_position:
            starting_x = starting_position[item][0] * player_width
            starting_y = starting_position[item][1] * player_height
            if item == 0 :
                image = steve_right_standing
            else :
                image = zom_right_standing
            screen.blit(image, (starting_x, starting_y))
            

            
    if counter < len(update_actions) and counter != -1 :
        screen.blit(background_image, [0, 0])
        frame = update_actions[counter]
        if 'update' in frame:
            # for item in starting_position:
            #     starting_x = starting_position[item][0] * player_width
            #     starting_y = starting_position[item][1] * player_height
            #     if item == 0 :
            #         image = steve_right_standing
            #     else :
            #         image = zom_right_standing
            #     screen.blit(image, (starting_x, starting_y))
            pass
        else :
            ID = frame[0]
            IDPos = [0,0]
            IDPos[0] = frame[1][0]
            IDPos[1] = frame[1][1]
            action = frame[2]
            if action == 'moving':
                newPos = [0,0]
                newPos[0] = frame[3][0]
                newPos[1] = frame[3][1]
            if ID == 0:
                x0 , y0 = IDPos
                xtrue = x0*player_width
                ytrue = y0*player_height
                if action == 'healing':
                    animation = anim_objects['steve_right_heal']
                elif action == 'aging':
                    animation = anim_objects['steve_right_age']
                elif action == 'scanning':
                    animation = anim_objects['steve_right_scan']  
                elif action == 'attacking':
                    animation = anim_objects['steve_right_attack']
                elif action == 'moving':
                    xnew , ynew = newPos
                    xnew = xnew * player_width
                    ynew = ynew * player_height
                    if x0 > xnew:
                        animation = anim_objects['steve_left_walk']
                    else:
                        animation = anim_objects['steve_right_walk']
                elif action == 'died!':
                    animation = anim_objects['steve_right_die']
            else:
                x , y = IDPos
                xtrue = x*player_width
                ytrue = y*player_height
                if action == 'healing':
                    animation = anim_objects['zom_right_heal']
                elif action == 'aging':
                    animation = anim_objects['zom_right_age']
                elif action == 'scanning':
                    animation = anim_objects['zom_right_scan']
                elif action == 'attacking':
                    animation = anim_objects['zom_right_attack']
                elif action == 'moving':
                    xnew , ynew = newPos
                    xnew = xnew * player_width
                    ynew = ynew * player_height
                    if x > xnew:
                        animation = anim_objects['zom_left_walk']
                    else:
                        animation = anim_objects['zom_right_walk']
                elif action == 'died!':
                    animation = anim_objects['zom_right_die']  
            
            
            
            animation.play() 
            animation.blit(screen, (xtrue, ytrue))

            if action == 'moving' :
                starting_position[ID] = [xnew, ynew]
            else :
                starting_position[ID] = [xtrue, ytrue]
                
                
                
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN :
            if event.key == K_z:
                counter += 1

        pygame.display.update()
        mainClock.tick(30) # FRAMES PER SECOND





