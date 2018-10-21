from utils import log


class Pixel:

    def __init__(self, x, y, scr, ch='#') -> None:
        self.x = x
        self.y = y
        self.ch = ch
        self.scr = scr
        self.scr_h, self.scr_w = scr.getmaxyx()
        # magic number
        self.scr_board = 2

    def update(self, key=None):
        pass

    def render(self):
        # log('x:', self.x, 'y:', self.y, 'ch:', self.ch)
        self.scr.addstr(self.y, self.x, self.ch)

    @property
    def coor(self):
        return self.x, self.y
