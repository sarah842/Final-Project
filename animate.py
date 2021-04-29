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
get_map = main.ZombieHunter(main.IGame)
have_map = get_map._world
map_dimensions = have_map.getSize()
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


store_actions = main.main()
print(store_actions)

# FOR TESTING

anim_objects['steve_left_heal'].play()

while True:
    screen.blit(background_image, [0, 0])
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_l:
            # press "L" key to stop looping
            anim_objects['steve_left_heal'].loop = False

    anim_objects['steve_left_heal'].blit(screen, (100, 50))
    
    
    pygame.display.update()
    mainClock.tick(30) # FRAMES PER SECOND
