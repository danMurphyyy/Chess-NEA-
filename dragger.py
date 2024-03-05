import pygame
from CONST import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initialRow = 0
        self.initialCol = 0

    def update_blit(self, surface):
        # Texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture

        img = pygame.image.load(texture)

        img_centre = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_centre)

        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # Will store position as a tuple (X,Y)

    def save_initial(self, pos):
        self.initialRow = pos[1] // SQSIZE
        self.initialCol = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False