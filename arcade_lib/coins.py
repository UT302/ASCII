import random
import arcade
import os



# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class MyGame(arcade.Window): # Custom Window Class

    def __init__(self): # Initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example") 

        # Working directory 
        #file_path = os.path.dirname(os.path.abspath("coins"))
        #os.chdir("coins.d")

        # Variables that will hold sprite lists 
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)
       
        arcade.set_background_color(arcade.color.AMAZON)


    def setup(self): # Set up the game and init the variables

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list  = arcade.SpriteList()
        
        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("/home/ponch/.local/lib/python3.6/site-packages/arcade/examples/images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            coin = arcade.Sprite("/home/ponch/.local/lib/python3.6/site-packages/arcade/examples/images/coin_01.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)



    def on_draw(self): # Draw everything

        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_mouse_motion(self, x, y, dx, dy): # Handle mouse motion

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        


    def update(self, delta_time): # Movement and game logic 

        # Call update on all sprites
        self.coin_list.update()


        # Generate a list of all sprites that collided with the player
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1


def main(): # Main function

    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()















