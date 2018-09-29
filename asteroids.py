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
        if self.center_x < -100 or self.center_x > 1500 or \
                self.center_y > 1100 or self.center_y < -100:
                    self.kill()


class MyGame(arcade.Window): # Main application class

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.all_sprites_list = None
        self.asteroid_list = None
        self.bullet_list = None
        self.ship_life_list = None

        # Set up the player
        self.score = 0 
        self.player_sprite = ShipSprite("/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/playerShip1_orange.png") 
        self.lives = 3

        # Sounds
        self.laser_sound = arcade.load_sound("/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/sounds/laser1.wav")

    def start_new_game(self): # Set up the game and initialize the variables 

        self.frame_count = 0
        self.game_over = False
        
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = ShipSprite("/home/ponch/.local/lib/python3.5/site-packages/arcade/exam
                ples/images/playerShip1_orange.pngj", SCALE)
        self.all_sprites_list.append(self.player_sprite)
        self.lives = 3

        # Set up liitle icons that represent the player lives
        cur_pos = 10
        for i in range(self.lives):
            life = arcade.Sprite("/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/playerLife1_orange.png", SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.all_sprites_list.append(self.player_sprites)
            self.ship_life_list.append(life)

        # Make the asteroids
        image_list = ("/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_big1.png",
                      "/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_big2.png",
                      "/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_big3.png",
                      "/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_big4.png")
        
        for i in range(STARTING_ASTEROID_COUNT):
            image_no = random.randrange(4)
            enemy_sprite = AsteroidSprite(image_list[image_no], SCALE)
            enemy_sprite.guid = "Asteroid"

            enemy_sprite.center_y = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
            enemy_sprite.center_x = random.randrange(LEFT_LIMIT, RIGHT_LIMIT)

            enemy_sprite.change_x = random.random() * 2 - 1
            enemy_sprite.change_y = random.random() * 2 - 1

            enemy_sprite.change_angle = random.random() - 0.5) * 2
            enemy_sprite.size = 4
            self.all_sprites_list.append(enemy_sprite)
            self.asteroid_list.append(enemy_sprite)

    def on_draw(self): # Render the screen.

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Put the text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 13)
        
        output = f"Asteroid C: {len(self.score)}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13)

    
    def on_key_press(self, symbol, modifiers): # Shoot if the player hit the space bar and we aren't respawning.

        if not self.player_sprite.respawning and symbol == arcade.key.SPACE:
            bullet_sprite = BulletSprite("/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/laserBlue01.png", SCALE)
            bullet_sprite.guid = "Bullet"

            bullet_speed = 13
            bullet_sprite.change_y = \
                    math.cos(math.radians(self.player_sprite.angle)) * bullet_speed
            bullet_sprite.change_x = \
                    -math.sin(math.radians(self.player_sprite.angle)) \
                    * bullet_speed


            bullet_sprite.center_x = self.player_sprite.center_x
            bullet_sprite.center_y = self.player_sprite.center_y
            bullet_sprite.update

            self.all_sprite_list.append(bullet_sprite)
            self.bullet_list.append(bullet_sprite)

            # arcade.play_sound(self.Laser_sound)

       if symbol == arcade.key.LEFT:
           self.player_sprite.change_angle = 3

       elif symbol == arcade.key.RIGHT:
           self.player_sprite.change_angle = -3

       elif symbol == arcade.key.UP:
           self.player_sprite.thrust = 0.15

       elif symbol == arcade.key.DOWN:
           self.player_sprite.change_angle = -.2


    def on_key_release(self, symbol, modifiers):

         if symbol == arcade.key.LEFT:
             self.player_sprite.change_angle = 0

         elif symbol == arcade.key.RIGHT:
             self.player_sprite.change_angle = 0

         elif symbol == arcade.key.UP:
             self.player_sprite.thrust = 0

         elif symbol == arcade.key.DOWN:
             self.player_sprite.thrust = 0


    def split_asteroid(self, astroid: AsteroidSprite): # Split asteroid into chunks
     
          x = asteroid.center_x
          y = asteroid.center_y
          self.score += 1
          
          if asteroid.size == 4:

              for i in range(3):
                  image_no = random.randrange(2)
                  image_list = ["/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_med1.png", 
                                "/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_med2.png"] 

                  enemy_sprite = AsteroidSprite(image_list[image_no],
                                                SCALE * 1.5)

                  enemy_sprite.center_y = y
                  enemy_sprite.center_x = x

                  enemy_sprite.change_x = random.random() * 2.5 - 1.25
                  enemy_sprite.change_y = random.random() * 2.5 - 1.25

                  enemy_sprite.change_angle = (random.random() - 0.5) * 2
                  enemy_sprite.size = 3

                  self.all_sprites_list.append(enemy_sprite)
                  self.asteroid_list.append(enemy_sprite)

          elif asteroid.size == 3:

              for i in range(3):
                  image_no = random.randrange(2)
                  image_list = ["/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_small1.png",
                                "/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_small2.png"]

                  enemy_sprite = AsteroidSprite(image_list[image_no],
                                                SCALE * 1.5)

                  enemy_sprite.center_y = y
                  enemy_sprite.center_x = x

                  enemy_sprite.change_x = random.random() * 3 - 1.5
                  enemy_sprite.change_y = random.random() * 3 - 1.5

                  enemy_sprite.change_angle = (random.random() - 0.5) * 2
                  enemy_sprite.size = 2

                  self.all_sprites_list.append(enemy_sprite)
                  self.asteoid_list.append(enemy_sprite) 

          elif asteroid.size == 2:

              for i in range(3):
                  image_no = random.randrange(2)
                  image_list = ["/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_tiny1.png",
                                "/home/ponch/.local/lib/python3.5/site-packages/arcade/examples/images/meteorGrey_tiny2.png"]

                  enemy_sprite = AsteroidSprite(image_list[image_no],
                                                SCALE * 1.5)

                  enemy_sprite.center_y = y
                  enemy_sprite.center_x = x

                  enemy_sprite.change_x = random.random() * 3.5 - 1.75
                  enemy_sprite.change_y = random.random() * 3.5 - 1.75

                  enemy_sprite.change_angle = (random.random() - 0.5) * 2
                  enemy_sprite.size = 1

                  self.all_sprites_list.append(enemy_sprite)
                  self.asteoid_list.append(enemy_sprite) 
    
    def update(self, x): # Move everything

        self.frame_count += 1 

        if not self.game_over:
            self.all_sprites_list.update()

            for bullet in self.bullet_list:
                self.asteroid_list.use_spatial_hash = False
                asteroids_plain = arcade.check_for_collision_with_list(bullet, self.asteroid_list)
                self.asteroid_list.use_spatial_hash = True
                asteroids_spatial = arcade.check_for_collision_with_list(bullet, self.asteroid_list)
                if len(asteroids_plain) != len(asteroids_spatial):
                    print("ERROR")

                asteroids = asteroids_spatial

                for asteroid in asteroids: 
                    self.split_asteroid(asteroid)
                    asteroid.kill()
                    bullet.kill()

            if not self.player_sprite.respawning:
                asteroids = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)
                if len(asteroids) > 0:
                    if self.lives > 0:
                        self.lives -= 1
                        self.player_sprite.respawn()
                        self.split_asteroid(asteroids[0])
                        asteroids[0].kill()
                        self.ship_life_list.pop().kill()
                        print("Crash")
                    else:
                        self.game_over = True
                        print("Game Over")


def main():
    window = MyGame()
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()























