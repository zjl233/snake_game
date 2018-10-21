from random import randint

from pixel import Pixel


class Food(Pixel):
    def __init__(self, x, y, scr, ch='#') -> None:
        super().__init__(x, y, scr, ch)
        self.reset()

    def reset(self):
        self.x = randint(self.scr_board, self.scr_w - self.scr_board)
        self.y = randint(self.scr_board, self.scr_h - self.scr_board)
