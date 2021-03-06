import math

from gamelib import *

class ZombieCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)

    def selectBehavior(self):
        prob = random.random()

        # If health is less than 50%, then heal with a 10% probability
        if prob < 0.1 and self.getHealth() < self.getInitHealth() * 0.5:
            return HealEvent(self)

        # Pick a random direction to walk 1 unit (Manhattan distance)
        x_off = random.randint(-1, 1)
        y_off = random.randint(-1, 1)

        # Check the bounds
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0

        return MoveEvent(self, x + x_off, y + y_off)

class PlayerCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)
        # You may add any instance attributes you find useful to save information between frames

    def selectBehavior(self):
        prob = random.random()
        if self.getHealth() < self.getInitHealth()*0.5:
            return HealEvent(self)
        elif prob < 0.6666:
            x , y = self.getPos()
            map_view = self.getMapView()
            size_x , size_y = map_view.getMapSize()
            x_move ,y_move = 1 , 1
            if x + x_move < 0 or x + x_move >= size_x:
                x_move = 0
            if y + y_move < 0 or y + y_move >= size_y:
                y_move = 0
            return MoveEvent(self, x + x_move, y + y_move)
        
        elif 0.6666 <= prob < 0.7:
            return ScanEvent(self)
        else:
            return AttackEvent(self, 1)
