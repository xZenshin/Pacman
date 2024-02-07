import pygame
from pygame.locals import *
from vector import Vector2
from constants import *
from entity import Entity

class Ghost(Entity):
    def __init__(self, node, pacman):
        Entity.__init__(self, node)
        self.name = GHOST
        self.pacman = pacman
        self.goal = pacman.position
        self.points = 200
        self.directionMethod = self.fleeingDirection

    def update(self, dt):
        self.goal = self.pacman.position
        Entity.update(self, dt)
