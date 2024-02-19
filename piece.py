
class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color

        if color == 'White':
            value_sign = 1
        else:
            value_sign = -1

        self.value = value * value_sign
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

class Pawn(Piece):
    def __init__(self, color):
        if color == 'White':
            self.dir = -1
        else: 
            self.dir = 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.0001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 900000.0)