from sys import exit
import math
from random import randint
from textwrap import dedent
from os import system

class Scene(object):

    def enter(self):
        print("Not done yet. Subclass it and implement enter.()")
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

    def enter(self):
        print("You are dead.")


class Map(object):
    scenes = {
            'training_room':TrainingRoom(),
            'death':Death()
            'finished':Finished(),


            }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('training_room')
a_game = Engine(a_map)
a_game.play()
