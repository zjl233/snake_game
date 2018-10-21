from pixel import Pixel
from utils import cycle, log
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN


class Head(Pixel):

    def __init__(self, x, y, scr, ch='#') -> None:
        super().__init__(x, y, scr, ch)
        self.speed = 1
        self.key_dir = {
            KEY_LEFT: (-1, 0),
            KEY_RIGHT: (1, 0),
            KEY_UP: (0, -1),
            KEY_DOWN: (0, 1),
        }
        start_key = KEY_RIGHT
        self.cur_dir = self.key_dir[start_key]

    def update(self, key=None):
        if key in self.key_dir.keys():
            d = self.key_dir[key]
            # reverse direction
            if tuple(x + y for x, y in zip(self.cur_dir, d)) != (0, 0):
                self.cur_dir = self.key_dir[key]

        x_dir, y_dir = self.cur_dir
        self.x = cycle(self.x + x_dir * self.speed,
                       self.scr_board,
                       self.scr_w - self.scr_board)
        self.y = cycle(self.y + y_dir * self.speed,
                       self.scr_board,
                       self.scr_h - self.scr_board)
