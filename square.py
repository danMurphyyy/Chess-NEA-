class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
    
    def has_piece(self):
        return self.piece != None
    
    @staticmethod
    # Static Method allows me to call a method without needing an instance of the class 
    def in_range(*args):
    # *args = unlimited arguments
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        
        return True