import os

class Piece:

    def __init__(self, name, number, value, texture=None, texture_rect=None):
        self.name = name
        self.number = number
        value_sign = 1 if number == 1 else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self):
        self.texture = os.path.join(
            f'images/{self.name}_{self.number}.png')

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []

class Player1(Piece):

    def __init__(self, number):
        super().__init__('player1', number, 1.0)

class Player2(Piece):

    def __init__(self, number):
        super().__init__('player2', number, 1.0)