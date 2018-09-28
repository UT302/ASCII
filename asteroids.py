import random 
import math
import arcade
import os 


STARTING_ASTEROD_COUNT = 3 
SCALE = 0.5
OFFSCREEN_SPACE = 300
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
LEFT_LIMIT =  -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HIGHT + OFFSCREEN_SPACE



class TurningSprite(arcade.Sprite): # Sprite that sets its angle to the direction it is traveling in.

    def update(self):
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))


class ShipSprite(arcade.Sprite): # Sprite of a space ship from arcade.Sprite

    # Call the parent Sprite constructor
    def __init__(self, filename, scale)

    # Info in where we are going
    # Angle comes in automatically from the parent class
    
    self.thrust = 0
    self.speed = 0
    self.max_speed = 4
    self.drag = 0.05
    self.respawning = 0

    # Mark that we are respawning
    self.respawn()

    def respawn(self): # Called when we die and need to make a new ship, 'respawning' is an invulnerability timer
        # If We are in the middle of respawning, this is non-zero.

        self.respawning = 1
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self): # Update our position and other particulars

        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning / 500.0
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 1
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

class AsteroidSprite(arcade.Sprite):

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale = scale)
        self.size = 0

    def update(self): # Move the asteroid around

        super().update()
        if self.center_x < LEFT_LIMIT:
            self.center_x = RIGHT_LIMIT
        if self.center_x < RIGHT_LIMIT:
            self.center_x = LEFT_LIMIT
        if self.center_y < TOP_LIMIT:
            self.center_y = BOTTOM_LIMIT
        if self.center_y < BOTTOM_LIMIT:
            self.center_y = TOP_LIMIT


class BulletSprite(TurningSprite):

    def update(self):
        super().update()












