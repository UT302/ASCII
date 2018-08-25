from sys import exit
from random import randint
from textwrap import dedent 
from os import system


class Scene(object):

    def enter(self):
        print("Not done yet.")
        print("Subclass it and implement enter.()")
        exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()  


class Finished(Scene):

    def enter(self):
        print("Done")
        exit(0)


class Death(Scene):

    quips = [ 
        "You are dead."
        ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        system('clear')
        print(dedent("""
                """))
        print("1.\n2.\n3.\n4.")
        
        action = input(">")
        if action == "1":
            print(dedent("""
                 """))
            return 'death'

        elif action == "2":
             print(dedent(""" 
             """))
             return 'death'

        elif action == "3": 
            print(dedent("""
            """))
            return 'laser_weapon_armory'
        else: 
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(dedent("""
    """))
        print("1: Search the weapon lockers.\n2 :Search the officer workplace.") 
        

        action = input(">")
        
        if action == "1":
            print(dedent("""You found nothing in particular
                """))
        
        elif action == "2":
            print (dedent(f"""You found burnt piece of paper. You can clearly see digit {code[:-2]} in the beggining.
            """))
                             

        print(dedent("""
        """))
        
        guess = input("[keypad]> ")
        guesses = 9

        while guess != code and not guesses == 0:

           print ("BZZZZEDDD!\nYou have ",guesses, "guesses left!" )
           guesses = guesses - 1
           guess = input("[keypad]> ")
            
        if guess == code:

           print(dedent("""
           The container clicks open and the seal brakes, letting gas out.
           You grab the neutron bomb and ran as fast you can to the bridge 
           where you must place it the right spot.
           """))
           return 'the_bridge'
        else:

           print(dedent(""" 
           The locks buzzes one last time, then a sickening melting sound 
           pierse you ears as the mechanism fused together.
           You realize, that it's your final moments, and there's nothing else that could be done.
           You pull out your laser pistol, bringin it to your head, pull the trigger... And that's it.
                """))
           return 'death'

class TheBridge(Scene):

    def enter(self):
        print (dedent("""
           """))
        print("1\n2\n")
            
        
        action = input("> ")
        
        if action == "1":
            print(dedent("""
                """))
            return 'death'
        
        elif action == "2": 
            print(dedent("""
                """))

            return 'escape_pod'
        else:
            
            system('clear')
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent(""" 
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]>")

        if int(guess) != good_pod:
            print(dedent(f""" 
                """))
            return 'death'
        else: 
            print(dedent(f""" 
                """))
            return 'finished'





class Map(object):
    scenes = {
            'central_corridor':CentralCorridor(),
            'laser_weapon_armory':LaserWeaponArmory(),
            'the_bridge':TheBridge(),
            'escape_pod':EscapePod(),
            'death':Death(),
            'finished':Finished(),
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
