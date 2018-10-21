from snake.head import Head
from snake.node import Node


class Snake:
    def __init__(self, x, y, scr, head_ch='@') -> None:
        self.head = Head(x, y, scr, head_ch)
        self.body = []
        # the last node of body
        # for grow
        self.tail = None

    def update(self, key):
        h = self.head
        n = Node(h.x, h.y, h.scr)
        # insert head and pop the last node
        self.body.insert(0, n)
        # for grow
        self.tail = self.body.pop()

        self.head.update(key)

    def collid(self):
        return any([self.head.coor == n.coor for n in self.body])

    def grow(self):
        self.body.append(self.tail)

    def render(self):
        self.head.render()
        for n in self.body:
            n.render()
