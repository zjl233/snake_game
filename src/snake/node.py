from pixel import Pixel


class Node(Pixel):
    def __init__(self, x, y, scr, ch='#') -> None:
        super().__init__(x, y, scr, ch)
