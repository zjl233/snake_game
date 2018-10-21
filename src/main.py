import curses

from food import Food
from snake.snake import Snake
from utils import log


def main(stdscr):
    fps = 5
    stdscr.timeout(1000 // fps)
    # hide cursor
    curses.curs_set(0)

    # init head at top left
    border = 2
    stdscr.border(border)
    # h = Head(border, border, stdscr, '@')
    f = Food(border, border, stdscr, '$')
    s = Snake(border, border, stdscr)
    score = 0
    while True:
        stdscr.clear()

        # index of keyboard
        # index = -1 if no key inserted in loop
        stdscr.addstr(1, 10, f'score: {score}      type ESC to exit')
        # h.render()
        f.render()
        s.render()

        key = stdscr.getch()
        log('key:', key)
        s.update(key)
        # ESC == 27
        if s.collid() or key == 27:
            break

        if s.head.coor == f.coor:
            f.reset()
            s.grow()
            score += 1


if __name__ == '__main__':
    # wrapper: auto init and safe exit
    curses.wrapper(main)
