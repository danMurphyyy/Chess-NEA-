import pygame
from CONST import *

class Dragger:

    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # Will store position as a tuple (X,Y)